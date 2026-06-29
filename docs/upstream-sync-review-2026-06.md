# Upstream Synchronization Review: June 2026

## Purpose

This note records the release review used to prepare ARF On-Ramp Pack 1.2.0.

## Findings

| Area | Finding | Repository action |
|---|---|---|
| ARF public documentation | Public EUDI documentation identifies ARF 2.9.0 as the current baseline. | Updated release-facing documentation from ARF 2.8.0 to ARF 2.9.0. |
| Public portal | EUDI documentation is discoverable through `https://eudi.dev/`. | Updated portal references and added portal monitoring. |
| STS | Standards and technical specifications remain a distinct upstream surface. | Preserved STS separation in references, reading paths, and quick reference. |
| Attestation rulebooks | Credential-specific rulebooks are a distinct implementation surface. | Added rulebooks catalog to references, checklist, reading paths, and source manifest. |
| CIR (EU) 2026/798 | The onboarding act is specifically about remote onboarding using assurance level substantial eID means with additional remote procedures where the combination meets assurance level high. | Tightened onboarding language across legal baseline, checklist, quick reference, and conformance companion. |
| Monitoring implementation | The manifest declared legal and web sources, but the script only supported GitHub repositories. | Extended the script to support GitHub repositories, EUR-Lex documents, and public web pages. |

## Validation Performed

- Python syntax validation for `scripts/check_upstream_sync.py`
- YAML parse validation for `governance/upstream-sources.yaml`
- JSON parse validation for `state/upstream-state.json` and `reports/upstream-drift-report.json`
- internal Markdown link validation across repository documentation
- stale current-release references scan for ARF 2.8.0 and 1.1.0 watchpoint language

## Operational Note

The packaged archive does not contain a live GitHub Actions state snapshot. Maintainers should run the `Upstream Sync Monitor` workflow manually after publishing the repository so GitHub-hosted execution can initialize `state/upstream-state.json` and `reports/upstream-drift-report.json` from live upstream APIs.
