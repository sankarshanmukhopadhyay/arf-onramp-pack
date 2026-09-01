---
layout: default
title: "Implementation Checklist"
parent: "Implementation"
grand_parent: "Documentation Home"
nav_order: 2
permalink: /docs/implementation-checklist/
authority_level: companion-guidance
last_reviewed: 2026-09-01
upstream_dependencies:
  - arf
  - sts
previous_page:
  title: "Conformance Interpretation Companion"
  url: "/docs/conformance-interpretation-companion/"
next_page:
  title: "Implementation Workbook"
  url: "/docs/implementation/implementation-workbook/"
---
# Implementation Checklist

Use this checklist to convert the current legal and upstream baseline into work items.

## 1. Authority inventory

- [ ] confirm the project uses the consolidated eIDAS text as amended by Regulation (EU) 2024/1183
- [ ] confirm the project has identified which wallet-core implementing regulations apply to its scope
- [ ] check whether CIR (EU) 2026/1730, 2026/1731, or 2026/1735 amend an implementing regulation relied on by the project; use consolidated text when available
- [ ] confirm the project uses the current canonical ARF, STS, and attestation rulebooks repositories
- [ ] confirm whether the public documentation view being used is the current EUDI portal at `https://eudi.dev/`

## 2. Repository and standards alignment

- [ ] update all internal bookmarks and documentation to the current ARF repository
- [ ] route standards and technical-specification references to the STS repository
- [ ] route PID, mDL, and credential-specific rulebook references to the attestation rulebooks catalog
- [ ] identify any local documents still pointing to deprecated upstream paths
- [ ] for Wallet Provider implementations, verify support for attestations listed in the Commission-managed catalogue of attestation schemes and retain evidence of issuance, display, and presentation interoperability decisions

## 3. Onboarding and enrollment

- [ ] assess whether remote onboarding assumptions need revision in light of CIR (EU) 2026/798
- [ ] identify where assurance level substantial eID means are combined with additional remote procedures to meet assurance level high
- [ ] identify enrollment, assurance-level, or identity-binding changes that affect implementation or local evidence plans

## 4. Relying-party ecosystem operations

- [ ] assess relying-party registration impacts under CIR (EU) 2025/848
- [ ] track the current STS TS5 and TS6 specifications when implementing relying-party registration information, Wallet-Relying Party Service data, schemas, and registration lifecycle behaviour
- [ ] for implementations based on the August 2026 TS5/TS6 maintenance line, re-check service-scoped trade-name/contact mappings, plural collection names such as `entitlements`, `subEntitlements`, and `usesIntermediaries`, and intermediary-service identifiers against the current upstream schemas before deployment
- [ ] map local registrar, trust-list, or metadata-lifecycle responsibilities
- [ ] retain conformance evidence showing which TS5/TS6 revision, exact upstream commit or tag, schema artifacts, and registration assumptions were implemented and tested

## 5. Incident and breach response

- [ ] align security-breach runbooks with CIR (EU) 2025/847
- [ ] identify responsible parties, evidence outputs, and notification workflows

## 6. Certification and evidence

- [ ] map scope for certification under CIR (EU) 2024/2981
- [ ] build an evidence register for conformance testing, operational controls, and audit artifacts

## 7. Synchronization discipline

- [ ] enable the upstream synchronization control plane
- [ ] review source manifest coverage
- [ ] verify GitHub, EUR-Lex, and portal monitoring source types are covered
- [ ] test issue automation and drift reporting
- [ ] assign an owner for synchronization remediation

## 8. Release readiness for this repository

- [ ] update changelog
- [ ] verify links
- [ ] validate workflow syntax
- [ ] validate JSON and YAML artifacts
- [ ] confirm the legal baseline document remains accurate at release time

{% include page-nav.html %}
