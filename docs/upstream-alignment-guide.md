# Upstream Alignment Guide

This guide explains how to keep the on-ramp synchronized with upstream legal and technical sources.

## Alignment principle

Treat synchronization as executable governance.

A high-quality update process should answer four questions:

1. **What changed upstream?**
2. **Which local documents are affected?**
3. **What evidence shows the change?**
4. **What local action closes the drift?**

## Current upstream sources to watch

### Legal and regulatory layer
- Regulation (EU) No 910/2014 in consolidated form
- Regulation (EU) 2024/1183
- wallet-core implementing regulations adopted in 2024, 2025, and 2026

### Technical layer
- ARF repository
- STS repository
- attestation rulebooks catalog repository where relevant
- public EUDI documentation portal at `https://eudi.dev/`

## Typical drift classes

### 1. Release drift
Example: a new ARF release changes annex structure or main-document references.

### 2. Repository-structure drift
Example: a technical-specification path moves out of the ARF repo and into the STS repo.

### 3. Legal drift
Example: a new implementing regulation adds a new operational obligation that should be reflected in the companion pack.

### 4. Interpretation drift
Example: a local guide still frames an older legal or repository model after upstream authority has moved.

## Recommended review cadence

- **Automated:** daily or weekly through the control plane
- **Human review:** monthly for documentation quality, or immediately when a drift issue is opened
- **Release review:** before every tagged release of this repository

## Local impact assessment matrix

| Drift type | Likely impacted files | Typical action |
|---|---|---|
| ARF release change | `README.md`, reading paths, companion docs | update references, summaries, and affected guidance |
| STS change | implementation docs, quick reference, reading paths | repoint technical-specification references |
| attestation rulebook change | implementation checklist, architecture map, quick reference | update credential-specific guidance and evidence expectations |
| new implementing regulation | legal baseline, checklist, governance mapping | add legal inventory entry and revise affected guidance |
| EUR-Lex content or metadata change | legal baseline, references, role FAQs | escalate for human legal review before changing interpretation |
| file move / renamed upstream path | all docs with direct links | repair links and note in changelog |

## Maintainer checklist

- confirm the upstream change
- capture evidence in the drift issue or report
- update all impacted docs or explain a no-change outcome
- update `CHANGELOG.md`
- include release-note language if the change materially affects users of the pack

## Semantic re-audit trigger conditions

Run a broader semantic re-audit when:

- an amending regulation changes the legal structure
- a new wallet-core implementing act is adopted
- the canonical upstream repository changes
- the public documentation portal changes current ARF version or discovery structure
- ARF integrates discussion topics that materially change the interpretation surface

## Release note expectation

Synchronization updates should not be hidden as editorial noise when they materially change the authority model or implementation posture of the repository.
