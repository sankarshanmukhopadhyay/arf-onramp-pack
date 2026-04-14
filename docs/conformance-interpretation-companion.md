# Conformance Interpretation Companion

This document helps teams translate the legal and upstream technical landscape into implementation and evidence-planning work.

## Scope note

This is a **companion interpretation document**. It is not a certification artifact and it is not a legal opinion.

## Current authority order for conformance work

When a conformance question arises, use this escalation path:

1. **Primary law** — Regulation (EU) No 910/2014 as amended by Regulation (EU) 2024/1183
2. **Relevant implementing regulation** — especially the wallet-core acts
3. **Upstream ARF and annexes**
4. **Upstream STS material**
5. **This repository's implementation interpretation**

## Why this matters

A common failure mode is treating all wallet requirements as if they come from a single source. They do not.

Some obligations are legal. Some are procedural. Some are architectural. Some are implementation guidance. Conformance planning improves when those sources are separated.

## Conformance workstreams to plan explicitly

### 1. Core functionality and integrity
Anchor this work first in the implementing acts governing integrity, core functionality, protocols, and certification.

### 2. Identity and attribute handling
Anchor this work in the implementing act covering PID and EAAs, then use ARF and STS for the technical narrative and implementation paths.

### 3. Registration, notification, and ecosystem operations
Anchor this work in the implementing acts on notifications, relying-party registration, and the list of certified wallets.

### 4. Incident and breach response
Anchor this work in the implementing act on reactions to security breaches and connect it to local operational runbooks.

### 5. Onboarding and user enrollment
Anchor this work in the April 2026 onboarding implementing regulation and test how it changes enrollment assumptions in local documentation and architecture.

## Evidence planning model

For each requirement cluster, produce at least four things:

- source reference
- local interpretation
- implementation control or design decision
- evidence or test artifact

A lightweight pattern looks like this:

| Source | Local interpretation | Implementation artifact | Evidence |
|---|---|---|---|
| implementing regulation / ARF clause | what the team believes must be true | code, config, process, or architecture decision | test result, review record, report, or certification evidence |

## Interpretation guardrails

### Guardrail 1
Do not cite Regulation (EU) 2024/1183 as if it were itself the implementing-act layer.

### Guardrail 2
Do not assume the ARF alone answers procedural questions now addressed in later implementing acts.

### Guardrail 3
Do not treat STS tracking as decorative. It is part of the moving implementation surface.

## Recommended next step

Pair this guide with:

- [implementation-checklist.md](./implementation-checklist.md)
- [governance-to-control-mapping.md](./governance-to-control-mapping.md)
- [upstream-alignment-guide.md](./upstream-alignment-guide.md)
