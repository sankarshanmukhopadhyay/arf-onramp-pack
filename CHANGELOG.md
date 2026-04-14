# Changelog

All notable changes to this project are documented here.

## [1.1.0] - 2026-04-14

### Added
- governance synchronization control plane for upstream monitoring
- machine-readable source manifest at `governance/upstream-sources.yaml`
- scheduled GitHub Actions workflow for upstream drift checks
- automated issue creation/update flow for detected upstream drift
- evidence outputs via `state/upstream-state.json` and `reports/upstream-drift-report.json`
- new documentation:
  - `docs/legal-baseline-2026.md`
  - `docs/upstream-monitoring.md`

### Changed
- re-baselined the repository against the current canonical ARF repository
- re-pointed technical specification references to the dedicated STS repository
- refreshed role-based reading paths to reflect the post-2024 implementing-act landscape
- revised README, references, and implementation guidance for a 1.1.0 release posture

### Fixed
- corrected repeated misclassification of **Regulation (EU) 2024/1183** as a Commission implementing regulation
- corrected outdated repository paths and stale technical-specification links
- corrected related-legislation metadata where descriptions drifted from the underlying legal acts
- corrected the wallet-core legal inventory to reflect the 2024, 2025, and April 2026 adopted measures now relevant to the companion pack

### Assurance note
This release includes a semantic re-audit of the companion guidance against the latest available legal and upstream material used as of April 14, 2026. The pack remains implementation guidance and does not substitute for legal advice, certification decisions, or national competent authority interpretation.

## [1.0.2] - Prior release

Previous published release referenced by the repository owner. This release served as the base for the 1.1.0 synchronization and semantic re-audit.
