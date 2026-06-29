# Release Notes 1.2.0

## Summary

Release 1.2.0 synchronizes the ARF On-Ramp Pack with the current public EUDI Wallet documentation baseline and strengthens the repository's upstream drift control plane.

The pack now targets **ARF 2.9.0**, treats `https://eudi.dev/` as the public EUDI documentation portal, and adds the attestation rulebooks catalog as a monitored upstream source.

## What Changed

### Upstream synchronization

- updated the release-facing baseline from ARF 2.8.0 to ARF 2.9.0
- added `eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog` to the monitored source manifest
- updated the EUDI portal reference from the legacy GitHub Pages URL to `https://eudi.dev/`
- clarified the distinct roles of ARF, STS, attestation rulebooks, and this companion pack

### Control-plane hardening

- extended `scripts/check_upstream_sync.py` beyond GitHub repositories
- added support for `eurlex_document` and `web_page` source snapshots
- added content-hash and watched-fragment evidence for legal and public web sources
- made local snapshot/report execution possible without requiring issue-creation credentials
- retained GitHub issue creation/update when `REPOSITORY` and `GITHUB_TOKEN` are available

### Legal and assurance guidance

- tightened CIR (EU) 2026/798 language around remote onboarding
- clarified that the regulation concerns assurance level substantial eID means used with additional remote onboarding procedures where the combination meets assurance level high
- refreshed legal baseline, quick reference, implementation checklist, FAQ, and role-based reading paths
- updated architecture guidance to avoid local shorthand that could be mistaken for authoritative assurance levels

## Validation

- YAML manifest validated
- JSON state and report artifacts validated
- Python script compiled successfully
- internal Markdown links checked
- stale ARF 2.8.0 release posture removed from current release-facing documentation
- synchronization review captured in `docs/upstream-sync-review-2026-06.md`

## Compatibility Notes

This remains a companion implementation and governance pack. It does not replace EU law, implementing regulations, conformity assessment, national implementation decisions, or upstream ARF/STS/rulebook sources.

Legal and EUR-Lex drift remains a human-review trigger. The automation detects drift and produces evidence; it does not make legal interpretation decisions.
