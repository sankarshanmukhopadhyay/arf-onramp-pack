# Changelog

All notable changes to this project are documented here.

## [1.2.0] - 2026-06-28

### Added
- monitoring support for `eurlex_document` and `web_page` sources in `scripts/check_upstream_sync.py`
- attestation rulebooks catalog source in `governance/upstream-sources.yaml`
- public EUDI documentation portal monitoring through `https://eudi.dev/`
- local snapshot/report execution path that does not require issue-creation credentials
- release notes for the 1.2.0 synchronization refresh

### Changed
- updated the repository alignment target from ARF 2.8.0 to ARF 2.9.0
- tightened CIR (EU) 2026/798 language to reflect remote onboarding by assurance level substantial eID means plus additional remote procedures where the combination meets assurance level high
- expanded quick reference, legal baseline, reading paths, and implementation checklist to include attestation rulebook governance
- updated upstream monitoring documentation to describe supported source types and evidence outputs

### Fixed
- corrected the upstream monitor so the manifest no longer declares source types that the script cannot process
- removed stale ARF 2.8.0 release posture from current release-facing documentation
- corrected architecture-map terminology that implied non-authoritative local assurance levels

### Assurance note
This release synchronizes the companion pack with the June 2026 public ARF 2.9.0 documentation baseline and improves the evidence-producing control plane. Legal and EUR-Lex drift remains a human-review trigger; the automation detects drift, but does not create legal interpretation.

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
