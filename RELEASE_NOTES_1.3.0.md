## v1.3.0 - Trust and Reuse Hardening

This release strengthens adoption readiness for teams that need explicit reuse rights, verifiable synchronization controls, and structured contribution paths.

### Added

- `LICENSE` with CC BY 4.0 for documentation and Apache-2.0 for automation code.
- Fixture-based tests for upstream drift classification in `scripts/check_upstream_sync.py`.
- Pull-request CI workflow for the drift-monitor test suite.
- `CODE_OF_CONDUCT.md`.
- Misclassification report issue template for authority, legal-status, and interpretation defects.
- README sync-status and license guidance.

### Fixed

- Removed a committed `.DS_Store` file and added `.gitignore` hygiene.

### Compatibility

No changes were made to `governance/upstream-sources.yaml`, the drift report shape, or the script interface. Existing consumers of `state/upstream-state.json` and `reports/upstream-drift-report.json` remain compatible.
