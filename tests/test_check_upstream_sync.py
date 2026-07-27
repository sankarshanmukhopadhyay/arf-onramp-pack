from scripts import check_upstream_sync as monitor
from scripts.check_upstream_sync import compare_states


def test_github_repository_release_drift_is_reported():
    source = {
        "id": "arf",
        "type": "github_repo",
        "labels": ["arf"],
        "severity_rules": {"release_change": "high"},
    }
    previous = {"latest_release": "v2.8.0", "default_branch_sha": "abc", "path_shas": {}}
    current = {"latest_release": "v2.9.0", "default_branch_sha": "abc", "path_shas": {}}

    event = compare_states(source, previous, current)

    assert event is not None
    assert event.source_id == "arf"
    assert event.severity == "high"
    assert event.reasons == ["latest_release_changed"]
    assert event.labels == ["arf"]


def test_github_repository_watched_path_drift_is_reported():
    source = {
        "id": "sts",
        "type": "github_repo",
        "severity_rules": {"path_change": "medium"},
    }
    previous = {"path_shas": {"docs/index.md": "old"}}
    current = {"path_shas": {"docs/index.md": "new"}}

    event = compare_states(source, previous, current)

    assert event is not None
    assert event.severity == "medium"
    assert event.reasons == ["watched_paths_changed:docs/index.md"]


def test_web_page_content_and_fragment_drift_are_reported():
    source = {
        "id": "eudi-portal",
        "type": "web_page",
        "severity_rules": {"content_change": "medium", "fragment_change": "high"},
    }
    previous = {
        "content_hash": "old",
        "content_fragments": {"Architecture and Reference Framework": True},
        "etag": "a",
        "last_modified": "Mon",
        "fetched_url": "https://eudi.dev/",
    }
    current = {
        "content_hash": "new",
        "content_fragments": {"Architecture and Reference Framework": False},
        "etag": "a",
        "last_modified": "Mon",
        "fetched_url": "https://eudi.dev/",
    }

    event = compare_states(source, previous, current)

    assert event is not None
    assert event.severity == "high"
    assert event.reasons == [
        "content_hash_changed",
        "content_fragments_changed:Architecture and Reference Framework",
    ]


def test_metadata_only_drift_is_low_by_default():
    source = {"id": "eurlex", "type": "eurlex_document"}
    previous = {"etag": "old", "last_modified": "Mon", "fetched_url": "https://example.test/a"}
    current = {"etag": "new", "last_modified": "Mon", "fetched_url": "https://example.test/a"}

    event = compare_states(source, previous, current)

    assert event is not None
    assert event.severity == "low"
    assert event.reasons == ["etag_changed"]


def test_identical_snapshots_do_not_report_drift():
    source = {"id": "no-drift", "type": "web_page"}
    previous = {"content_hash": "same", "content_fragments": {"wallet": True}}
    current = {"content_hash": "same", "content_fragments": {"wallet": True}}

    assert compare_states(source, previous, current) is None


def test_empty_previous_state_initializes_without_drift():
    source = {"id": "new-source", "type": "github_repo"}
    current = {"latest_release": "v1.0.0", "default_branch_sha": "abc"}

    assert compare_states(source, {}, current) is None


def test_upstream_manifest_is_valid_and_conflict_free():
    text = monitor.MANIFEST_PATH.read_text(encoding="utf-8")
    assert "<<<<<<<" not in text
    assert "=======" not in text
    assert ">>>>>>>" not in text

    manifest = monitor.load_yaml(monitor.MANIFEST_PATH)
    assert manifest["version"] == 1
    source_ids = [source["id"] for source in manifest["sources"]]
    assert len(source_ids) == len(set(source_ids))
    assert {"arf", "rulebooks_catalog", "sts"}.issubset(source_ids)


def test_manifest_sources_have_required_fields():
    manifest = monitor.load_yaml(monitor.MANIFEST_PATH)
    for source in manifest["sources"]:
        assert source["id"]
        assert source["type"] in {"github_repo", "eurlex_document", "web_page"}
        assert source["canonical_url"].startswith("https://")
        if source["type"] == "github_repo":
            assert source["owner"]
            assert source["repo"]

class FakeResponse:
    def __init__(self, status_code=200, text="x" * 250, url="https://example.test/"):
        self.status_code = status_code
        self.text = text
        self.url = url
        self.headers = {"Content-Type": "text/html"}

    def raise_for_status(self):
        # requests does not treat 202 as an error; admission policy must.
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")


class FakeSession:
    def __init__(self, response):
        self.response = response

    def get(self, *args, **kwargs):
        return self.response


def test_fetch_text_rejects_accepted_but_non_authoritative_202(monkeypatch):
    monkeypatch.setattr(monitor, "SESSION", FakeSession(FakeResponse(status_code=202, text="")))

    try:
        monitor.fetch_text("https://eur-lex.example/document")
    except RuntimeError as exc:
        assert "non-authoritative HTTP status 202" in str(exc)
    else:
        raise AssertionError("HTTP 202 must not be admitted as an authority snapshot")


def test_fetch_text_rejects_substantively_empty_200(monkeypatch):
    monkeypatch.setattr(monitor, "SESSION", FakeSession(FakeResponse(status_code=200, text="  ")))

    try:
        monitor.fetch_text("https://eur-lex.example/document")
    except RuntimeError as exc:
        assert "insufficient response content" in str(exc)
    else:
        raise AssertionError("empty interstitial content must not be admitted")


def test_portal_metadata_only_change_is_ignored_when_disabled():
    source = {
        "id": "eudi_wallet_portal",
        "type": "web_page",
        "watch": {"metadata_changes": False},
    }
    previous = {
        "etag": "old",
        "last_modified": "Mon",
        "fetched_url": "https://eudi.dev/",
        "content_fragments": {"European Digital Identity Wallet": True},
    }
    current = {
        "etag": "new",
        "last_modified": "Tue",
        "fetched_url": "https://eudi.dev/",
        "content_fragments": {"European Digital Identity Wallet": True},
    }

    assert compare_states(source, previous, current) is None
