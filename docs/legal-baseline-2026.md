---
layout: default
title: "Legal Baseline 2026"
parent: "Foundations"
grand_parent: "Documentation Home"
nav_order: 2
permalink: /docs/legal-baseline-2026/
authority_level: companion-guidance
last_reviewed: 2026-07-22
upstream_dependencies:
  - arf
  - sts
previous_page:
  title: "ARF Explained"
  url: "/docs/arf-explained/"
next_page:
  title: "Quick Reference"
  url: "/docs/quick-reference/"
---
# Legal Baseline 2026

This document states the legal and upstream baseline used for the 1.2.0 refresh of the ARF On-Ramp Pack.

## Purpose

The repository previously mixed three layers too loosely:

- the amended eIDAS regulation
- the implementing regulations
- the upstream ARF narrative

This document tightens those boundaries.

## Baseline used in this refresh

### 1. Primary law
The legal foundation is **Regulation (EU) No 910/2014**, in its consolidated form after amendment by **Regulation (EU) 2024/1183**.

### 2. Wallet-core implementing-act layer
For this repository, the wallet-core implementing-act layer currently includes:

- CIR (EU) 2024/2977
- CIR (EU) 2024/2979
- CIR (EU) 2024/2980
- CIR (EU) 2024/2981
- CIR (EU) 2024/2982
- CIR (EU) 2025/846
- CIR (EU) 2025/847
- CIR (EU) 2025/848
- CIR (EU) 2025/849
- CIR (EU) 2026/798, covering reference standards and specifications for remote onboarding of wallet users by assurance level substantial electronic identification means in conjunction with additional remote onboarding procedures where the combination meets assurance level high

### 3. Upstream technical-documentation layer
The current canonical upstream repositories are:

- `eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework`
- `eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications`
- `eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog`

The public rendered documentation portal is:

- `https://eudi.dev/`

The current ARF alignment target for this pack is **ARF 2.9.0**.

## Key interpretation rules adopted here

### Rule 1
**Regulation (EU) 2024/1183 is not a Commission implementing regulation.**

### Rule 2
**ARF is authoritative as upstream technical guidance and structure, but not as a substitute for the legal acts.**

### Rule 3
**STS work belongs to the STS repository, not the old technical-specifications path inside legacy ARF repository assumptions.**

### Rule 4
**Attestation rulebook work belongs to the attestation rulebooks catalog when credential-specific data models or rulebook requirements are in scope.**

### Rule 5
**Companion interpretations in this repository must be framed as implementation guidance, not binding legal conclusions.**

## Implications for maintainers

When updating this repository:

- check whether a claim comes from primary law, an implementing act, ARF, STS, or local interpretation
- cite the right layer
- do not back-port stale legacy repo paths into new documentation
- prefer explicit update notes when upstream terminology or repository structure changes

## Scope boundary

This repository does not attempt to reproduce all legal texts in full. It provides a working implementation companion anchored to the authority stack above.

{% include page-nav.html %}
