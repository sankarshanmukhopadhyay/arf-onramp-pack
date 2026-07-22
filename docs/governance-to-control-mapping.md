---
layout: default
title: "Governance to Control Mapping"
parent: "Governance and Assurance"
grand_parent: "Documentation Home"
nav_order: 1
permalink: /docs/governance-to-control-mapping/
authority_level: companion-guidance
last_reviewed: 2026-07-22
upstream_dependencies:
  - arf
  - sts
previous_page:
  title: "Architecture Layer Map"
  url: "/docs/architecture-layer-map/"
next_page:
  title: "Assurance Evidence"
  url: "/docs/governance-assurance/assurance-evidence/"
---
# Governance to Control Mapping

This document maps governance requirements and upstream authority sources to concrete implementation and assurance controls.

## Scope note

The purpose here is not to restate the legal texts. It is to help teams ask the right implementation question:

**What control, process, evidence artifact, or operational mechanism makes a given governance requirement real?**

## Updated source model

Use these source layers when building control mappings:

- primary law
- implementing act
- upstream ARF
- upstream STS
- local implementation decision

## Mapping pattern

| Governance source | Example concern | Control class | Evidence class |
|---|---|---|---|
| primary law | lawful framework, user rights, trust model | legal and governance controls | legal mapping, policy approval |
| implementing regulation | operational requirement or procedure | system/process control | test result, procedure record |
| ARF | architectural decomposition, interaction model | design and engineering control | architecture decision record |
| STS | evolving technical specification detail | technical implementation control | conformance evidence, protocol tests |

## High-value mapping areas

### 1. Onboarding and enrollment
The control question is not just how a user enrolls, but how enrollment proves the right assurance and identity-binding properties under the current legal and technical baseline.

### 2. Relying-party registration and ecosystem trust
The control question is how relying-party registration, validation, and lifecycle events are enforced and evidenced.

### 3. Incident and breach handling
The control question is how the system detects, classifies, escalates, and reports security breaches in a way that aligns with both legal obligations and local operational reality.

### 4. Certification readiness
The control question is what evidence package demonstrates conformance for the relevant wallet solution scope.

### 5. Upstream synchronization
The control question is how the repository and local implementation teams know when upstream movement invalidates a local interpretation or reference.

## Control-plane addition in 1.1.0

This repository now includes one explicit governance control for itself:

- **upstream drift monitoring and issue automation**

That is a repository-maintenance control, but it is also a governance control because it turns authority drift into a tracked remediation process.

## Recommended output for implementation teams

For each major governance requirement, maintain:

- source reference
- interpretation owner
- control owner
- evidence owner
- review cadence

That division of responsibility is more durable than a single narrative document.

{% include page-nav.html %}
