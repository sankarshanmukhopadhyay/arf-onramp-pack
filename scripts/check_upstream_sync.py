from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests
import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "governance" / "upstream-sources.yaml"
STATE_PATH = ROOT / "state" / "upstream-state.json"
REPORT_PATH = ROOT / "reports" / "upstream-drift-report.json"

TOKEN = os.environ["GITHUB_TOKEN"]
TARGET_REPOSITORY = os.environ["REPOSITORY"]
API_ROOT = "https://api.github.com"

SESSION = requests.Session()
SESSION.headers.update(
    {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "arf-onramp-pack-upstream-monitor",
    }
)


@dataclass
class DriftEvent:
    source_id: str
    severity: str
    previous: dict[str, Any]
    current: dict[str, Any]
    reasons: list[str]
    labels: list[str]


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def gh_get(path: str, params: dict[str, Any] | None = None) -> Any:
    response = SESSION.get(f"{API_ROOT}{path}", params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def gh_post(path: str, payload: dict[str, Any]) -> Any:
    response = SESSION.post(f"{API_ROOT}{path}", json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def gh_patch(path: str, payload: dict[str, Any]) -> Any:
    response = SESSION.patch(f"{API_ROOT}{path}", json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def get_latest_release(owner: str, repo: str) -> dict[str, Any] | None:
    response = SESSION.get(
        f"{API_ROOT}/repos/{owner}/{repo}/releases/latest",
        timeout=30,
        headers=SESSION.headers,
    )
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return response.json()


def get_head_commit(owner: str, repo: str, branch: str) -> dict[str, Any]:
    return gh_get(f"/repos/{owner}/{repo}/commits/{branch}")


def get_content_sha(owner: str, repo: str, path: str, ref: str) -> str | None:
    response = SESSION.get(
        f"{API_ROOT}/repos/{owner}/{repo}/contents/{path}",
        params={"ref": ref},
        timeout=30,
        headers=SESSION.headers,
    )
    if response.status_code == 404:
        return None
    response.raise_for_status()
    data = response.json()
    if isinstance(data, list):
        # Directory listing: use the directory response sha where available, otherwise hash children shas.
        children = sorted(item.get("sha", "") for item in data)
        return "dir:" + "|".join(children)
    return data.get("sha")


def get_repo_snapshot(source: dict[str, Any]) -> dict[str, Any]:
    owner = source["owner"]
    repo = source["repo"]
    repo_meta = gh_get(f"/repos/{owner}/{repo}")
    branch_name = repo_meta["default_branch"]
    head_commit = get_head_commit(owner, repo, branch_name)
    release = get_latest_release(owner, repo)
    path_shas = {}
    for watched_path in source.get("watch", {}).get("paths", []):
        path_shas[watched_path] = get_content_sha(owner, repo, watched_path, branch_name)
    return {
        "owner": owner,
        "repo": repo,
        "html_url": repo_meta["html_url"],
        "default_branch": branch_name,
        "default_branch_sha": head_commit["sha"],
        "latest_release": None if release is None else release.get("tag_name"),
        "path_shas": path_shas,
    }


def compare_states(source: dict[str, Any], previous: dict[str, Any], current: dict[str, Any]) -> DriftEvent | None:
    reasons: list[str] = []
    severity = "low"
    rules = source.get("severity_rules", {})

    if previous.get("latest_release") != current.get("latest_release"):
        reasons.append("latest_release_changed")
        severity = rules.get("release_change", severity)

    if previous.get("default_branch_sha") != current.get("default_branch_sha"):
        reasons.append("default_branch_sha_changed")
        if severity == "low":
            severity = rules.get("branch_change", severity)

    previous_paths = previous.get("path_shas", {})
    current_paths = current.get("path_shas", {})
    changed_paths = sorted(
        path for path, value in current_paths.items() if previous_paths.get(path) != value
    )
    if changed_paths:
        reasons.append("watched_paths_changed:" + ", ".join(changed_paths))
        if severity == "low":
            severity = rules.get("path_change", severity)

    if not reasons:
        return None

    return DriftEvent(
        source_id=source["id"],
        severity=severity,
        previous=previous,
        current=current,
        reasons=reasons,
        labels=source.get("labels", []),
    )


def issue_title(source_id: str) -> str:
    return f"Upstream sync: {source_id} drift detected"


def render_issue_body(event: DriftEvent) -> str:
    lines = [
        f"## Upstream drift detected for `{event.source_id}`",
        "",
        f"**Severity:** {event.severity}",
        f"**Detected:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%SZ')}",
        "",
        "### Evidence",
        f"- Previous release: `{event.previous.get('latest_release')}`",
        f"- Current release: `{event.current.get('latest_release')}`",
        f"- Previous default branch SHA: `{event.previous.get('default_branch_sha')}`",
        f"- Current default branch SHA: `{event.current.get('default_branch_sha')}`",
        "",
        "### Reasons",
    ]
    for reason in event.reasons:
        lines.append(f"- {reason}")

    path_shas = event.current.get("path_shas", {})
    if path_shas:
        lines.extend(["", "### Watched paths", *[f"- `{p}`" for p in sorted(path_shas.keys())]])

    lines.extend(
        [
            "",
            "### Suggested actions",
            "- [ ] review upstream change",
            "- [ ] update local references or guidance if needed",
            "- [ ] update changelog if the drift is user-visible",
            "- [ ] close this issue when synchronization is complete",
        ]
    )
    return "\n".join(lines)


def find_open_issue(source_id: str) -> dict[str, Any] | None:
    params = {
        "state": "open",
        "creator": "github-actions[bot]",
        "per_page": 100,
    }
    issues = gh_get(f"/repos/{TARGET_REPOSITORY}/issues", params=params)
    target = issue_title(source_id)
    for issue in issues:
        if issue.get("title") == target:
            return issue
    return None


def ensure_issue(event: DriftEvent) -> None:
    title = issue_title(event.source_id)
    body = render_issue_body(event)
    existing = find_open_issue(event.source_id)
    labels = sorted(set([*event.labels, "upstream-sync"]))
    if existing:
        gh_patch(
            f"/repos/{TARGET_REPOSITORY}/issues/{existing['number']}",
            {"body": body, "labels": labels},
        )
    else:
        gh_post(
            f"/repos/{TARGET_REPOSITORY}/issues",
            {"title": title, "body": body, "labels": labels},
        )


def main() -> None:
    manifest = load_yaml(MANIFEST_PATH)
    previous_state = load_json(STATE_PATH, {})
    current_state: dict[str, Any] = {}
    drift_events: list[DriftEvent] = []

    for source in manifest.get("sources", []):
        snapshot = get_repo_snapshot(source)
        current_state[source["id"]] = snapshot
        previous_snapshot = previous_state.get(source["id"], {})
        event = compare_states(source, previous_snapshot, snapshot)
        if event is not None:
            drift_events.append(event)

    report = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "drift": [
            {
                "source_id": event.source_id,
                "severity": event.severity,
                "previous": event.previous,
                "current": event.current,
                "reasons": event.reasons,
                "labels": event.labels,
            }
            for event in drift_events
        ],
    }

    save_json(STATE_PATH, current_state)
    save_json(REPORT_PATH, report)

    for event in drift_events:
        ensure_issue(event)


if __name__ == "__main__":
    main()
