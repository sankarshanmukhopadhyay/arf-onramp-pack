# ARF On-Ramp Pack
### EU Digital Identity Wallet ARF implementation companion

This repository is a **companion pack** for the European Digital Identity Wallet Architecture and Reference Framework (ARF). It is designed to help architects, implementers, policy teams, and assurance teams move from reading the upstream material to building, testing, governing, and maintaining against it.

It is **not** the authoritative source of law, specification, or conformance. The source of truth remains:

- the consolidated **eIDAS Regulation (EU) No 910/2014**, as amended by **Regulation (EU) 2024/1183**
- the adopted wallet-focused implementing regulations
- the upstream **ARF** repository
- the upstream **STS** repository for standards and technical specifications

## Release status

**On-ramp version:** 1.2.0  
**Previous release:** 1.1.0  
**ARF alignment target:** 2.9.0  
**Re-audit basis:** June 2026 upstream synchronization refresh

## What changed in 1.2.0

This release does three substantive things:

1. **Updates the upstream baseline**
   - aligns the pack to the current public ARF 2.9.0 documentation surface
   - treats `https://eudi.dev/` as the public EUDI documentation portal
   - keeps the ARF, STS, and attestation rulebooks repositories distinct

2. **Hardens the governance synchronization control plane**
   - monitors GitHub repositories, EUR-Lex documents, and public web pages declared in the manifest
   - adds the attestation rulebooks catalog to the monitored source inventory
   - makes local validation possible without requiring GitHub issue credentials

3. **Tightens onboarding and assurance language**
   - reflects the fuller title and scope of **CIR (EU) 2026/798**
   - clarifies that remote onboarding can combine assurance level substantial eID means with additional remote procedures where the combination meets assurance level high
   - keeps companion interpretation separate from legal or certification authority

## Current authority stack

Use this ordering when interpreting the pack:

1. **Law**
   - Regulation (EU) No 910/2014, as amended by Regulation (EU) 2024/1183
2. **Adopted implementing acts**
   - wallet-focused implementing regulations and related trust-service measures
3. **Upstream technical documentation**
   - ARF repository
   - STS repository
4. **This on-ramp pack**
   - orientation, synthesis, implementation checklists, and governance tooling

## Core legal and upstream baseline

### Primary law
- **Regulation (EU) No 910/2014**, consolidated after amendment by **Regulation (EU) 2024/1183**

### Wallet-core implementing regulations currently reflected here
- **CIR (EU) 2024/2977** — person identification data and electronic attestations of attributes issued to wallets
- **CIR (EU) 2024/2979** — integrity and core functionalities of wallets
- **CIR (EU) 2024/2980** — notifications to the Commission concerning the wallet ecosystem
- **CIR (EU) 2024/2981** — certification of wallet solutions
- **CIR (EU) 2024/2982** — protocols and interfaces
- **CIR (EU) 2025/846** — cross-border identity matching
- **CIR (EU) 2025/847** — reactions to security breaches of wallets
- **CIR (EU) 2025/848** — registration of wallet relying parties
- **CIR (EU) 2025/849** — list of certified wallets
- **CIR (EU) 2026/798** — reference standards and specifications for remote onboarding of wallet users by assurance level substantial eID means combined with additional remote procedures where the combination meets assurance level high

### Current upstream repositories
- **ARF:** `eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework`
- **STS:** `eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications`
- **Rulebooks catalog:** `eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog`
- **Public documentation portal:** `https://eudi.dev/`

## What this pack does

This repository helps teams answer practical questions such as:

- Which upstream sources are authoritative for a given implementation decision?
- What changed upstream, and what local documentation or controls need to move?
- How should a team structure implementation, evidence, and governance work around ARF?
- How should a program office distinguish legal obligation from technical guidance from companion interpretation?

## Documentation map

### Start here
- [docs/legal-baseline-2026.md](./docs/legal-baseline-2026.md) — current legal and repository baseline used for the 1.2.0 refresh
- [docs/arf-explained.md](./docs/arf-explained.md) — plain-language structural orientation to ARF
- [docs/upstream-alignment-guide.md](./docs/upstream-alignment-guide.md) — how to track and assess upstream drift
- [docs/upstream-monitoring.md](./docs/upstream-monitoring.md) — automation design and operating model
- [docs/upstream-sync-review-2026-06.md](./docs/upstream-sync-review-2026-06.md) — synchronization review evidence for 1.2.0

### Companion guidance
- [docs/conformance-interpretation-companion.md](./docs/conformance-interpretation-companion.md)
- [docs/governance-to-control-mapping.md](./docs/governance-to-control-mapping.md)
- [docs/implementation-checklist.md](./docs/implementation-checklist.md)
- [docs/quick-reference.md](./docs/quick-reference.md)
- [docs/faq-by-role.md](./docs/faq-by-role.md)
- [docs/architecture-layer-map.md](./docs/architecture-layer-map.md)

### Reading paths
- [docs/reading-paths/README.md](./docs/reading-paths/README.md)
- [docs/reading-paths/reading-path-policy-leadership.md](./docs/reading-paths/reading-path-policy-leadership.md)
- [docs/reading-paths/reading-path-architect.md](./docs/reading-paths/reading-path-architect.md)
- [docs/reading-paths/reading-path-implementer.md](./docs/reading-paths/reading-path-implementer.md)
- [docs/reading-paths/reading-path-security-assurance.md](./docs/reading-paths/reading-path-security-assurance.md)

## Governance synchronization control plane

The repository now includes an executable monitoring layer for upstream drift.

### Added components
- `governance/upstream-sources.yaml` — machine-readable list of monitored upstream sources
- `.github/workflows/upstream-sync.yml` — scheduled monitoring workflow
- `scripts/check_upstream_sync.py` — drift detection and issue automation
- `.github/ISSUE_TEMPLATE/upstream_drift.md` — issue template for synchronization work
- `state/upstream-state.json` — persisted tracking state
- `reports/upstream-drift-report.json` — evidence output from checks

### What it monitors
- upstream releases and tags
- default branch SHA drift
- selected watched paths
- legal/reference drift that maintainers explicitly configure in the source manifest
- content hashes and watched fragments for EUR-Lex and public web sources

### What it produces
- machine-readable state
- machine-readable drift report
- GitHub issue creation or update when synchronization action is needed

## Re-audit posture for 1.2.0

The semantic re-audit in this release follows four rules:

1. **Do not treat companion guidance as law.**
2. **Do not collapse Regulation (EU) 2024/1183 into the implementing-act layer.**
3. **Do not treat ARF as the sole source of truth where implementing regulations now speak directly.**
4. **Do treat the ARF and STS repos as moving operational references that require active synchronization.**

## Known scope boundaries

This repository does **not** replace:

- legal advice
- conformity assessment activity
- national implementation decisions
- upstream ARF or STS issue triage
- certification decisions by competent bodies

## Recommended usage model

### For policy and program teams
Start with:
- [docs/legal-baseline-2026.md](./docs/legal-baseline-2026.md)
- [docs/reading-paths/reading-path-policy-leadership.md](./docs/reading-paths/reading-path-policy-leadership.md)
- [docs/upstream-alignment-guide.md](./docs/upstream-alignment-guide.md)

### For architecture teams
Start with:
- [docs/arf-explained.md](./docs/arf-explained.md)
- [docs/architecture-layer-map.md](./docs/architecture-layer-map.md)
- [docs/reading-paths/reading-path-architect.md](./docs/reading-paths/reading-path-architect.md)

### For implementation teams
Start with:
- [docs/conformance-interpretation-companion.md](./docs/conformance-interpretation-companion.md)
- [docs/implementation-checklist.md](./docs/implementation-checklist.md)
- [docs/reading-paths/reading-path-implementer.md](./docs/reading-paths/reading-path-implementer.md)

### For security and assurance teams
Start with:
- [docs/governance-to-control-mapping.md](./docs/governance-to-control-mapping.md)
- [docs/reading-paths/reading-path-security-assurance.md](./docs/reading-paths/reading-path-security-assurance.md)
- [docs/upstream-monitoring.md](./docs/upstream-monitoring.md)

## Maintenance model

This on-ramp should be updated when any of the following occur:

- a new ARF release is published
- the STS repository materially changes tracked technical specifications
- a new implementing act or amendment materially affects wallet implementation or governance
- upstream file moves or renames break local references
- a synchronization issue is opened by the control plane

## Repository discipline

Every synchronization change should include:

- updated docs or explicit no-change rationale
- evidence of upstream drift
- changelog entry
- commit metadata
- release note language where applicable

## Versioning

- `1.0.2` — prior release baseline
- `1.1.0` — adds control plane and April 2026 legal re-baseline
- `1.2.0` — synchronizes to ARF 2.9.0, adds rulebooks monitoring, and hardens non-GitHub upstream checks

See [CHANGELOG.md](./CHANGELOG.md) for release details.
