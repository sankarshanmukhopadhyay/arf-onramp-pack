# Enhancement Summary

## 1.2.0 release objective

Prepare the ARF On-Ramp Pack for a 1.2.0 release by doing three things in one pass:

- synchronize the companion pack with the current public ARF 2.9.0 baseline
- harden the executable governance synchronization control plane so it covers every source type declared in the manifest
- update onboarding and rulebook guidance so implementers can map authority, implementation controls, and evidence more precisely

## Major improvements delivered

### Governance synchronization control plane
- expanded source support from GitHub repositories to GitHub repositories, EUR-Lex documents, and public web pages
- added attestation rulebooks catalog monitoring
- added public EUDI portal monitoring
- preserved issue automation for synchronization work
- preserved persisted state and machine-readable drift reporting

### Legal and upstream re-baseline
- updated the ARF alignment target to 2.9.0
- retained the correct treatment of Regulation (EU) 2024/1183 as an amending regulation
- tightened CIR (EU) 2026/798 onboarding language
- aligned references with the canonical ARF, STS, and attestation rulebooks repositories
- refreshed role-based reading paths, quick reference, implementation checklist, and monitoring documentation

## Assurance outcome

This release materially improves:

- authority clarity
- synchronization discipline
- evidence production for maintenance actions
- implementation-readiness for teams consuming the pack

## Repository impact

The repository is now better positioned as:

- a front-door implementation companion
- a governance-aware synchronization surface
- a documentation layer that is explicit about where authority actually lives
