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
