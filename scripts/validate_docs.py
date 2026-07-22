#!/usr/bin/env python3
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
errors = []

for required in [ROOT / "_config.yml", ROOT / "Gemfile", ROOT / "_includes/page-nav.html", DOCS / "index.md"]:
    if not required.exists():
        errors.append(f"missing required file: {required.relative_to(ROOT)}")

for path in sorted(DOCS.rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    if any(marker in text for marker in ("<<<<<<<", "=======", ">>>>>>>")):
        errors.append(f"merge marker: {path.relative_to(ROOT)}")
    if not text.startswith("---\n"):
        errors.append(f"missing front matter: {path.relative_to(ROOT)}")
        continue
    try:
        _, raw, body = text.split("---", 2)
        data = yaml.safe_load(raw) or {}
    except Exception as exc:
        errors.append(f"invalid front matter {path.relative_to(ROOT)}: {exc}")
        continue
    for key in ("layout", "title", "authority_level", "last_reviewed"):
        if key not in data:
            errors.append(f"missing {key}: {path.relative_to(ROOT)}")
    if data.get("nav_exclude") is not True:
        if "{% include page-nav.html %}" not in body:
            errors.append(f"missing Previous/Next include: {path.relative_to(ROOT)}")
        if not data.get("previous_page") and not data.get("next_page"):
            errors.append(f"missing Previous/Next metadata: {path.relative_to(ROOT)}")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
        target = target.split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:", "{{", "/")):
            continue
        candidate = (path.parent / target).resolve()
        candidates = [candidate]
        if candidate.suffix == "":
            candidates += [candidate.with_suffix(".md"), candidate / "index.md"]
        if not any(c.exists() for c in candidates):
            errors.append(f"broken link in {path.relative_to(ROOT)}: {target}")

if errors:
    print("\n".join(f"ERROR: {error}" for error in errors))
    sys.exit(1)
print(f"Documentation validation passed for {len(list(DOCS.rglob('*.md')))} Markdown pages.")
