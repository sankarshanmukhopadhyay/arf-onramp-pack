# ARF Explained

This document is a simplified orientation to the upstream Architecture and Reference Framework (ARF).

## Before you read

This guide is explanatory. It does not replace:

- the legal texts
- the adopted implementing regulations
- the upstream ARF repository
- the upstream STS repository

## What ARF is

The ARF is the main upstream architectural narrative for the European Digital Identity Wallet ecosystem. It explains roles, flows, security architecture, interoperability structure, and annexed requirements.

## What changed in the current baseline

For this repository, the important current-state correction is that the surrounding authority stack has become more layered:

- **Regulation (EU) 2024/1183** established the amended legal framework
- wallet-focused implementing regulations now carry a larger share of directly operative detail
- the **ARF** remains the main architectural narrative
- the **STS** repository now carries standards and technical-specification tracking that should not be collapsed back into older ARF path assumptions

## Practical reading model

Read ARF through four lenses.

### 1. Legal lens
Ask: which obligations are coming from law or implementing regulation, and which are being explained through ARF structure?

### 2. Ecosystem lens
Ask: which actors exist, what do they control, and what trust assumptions sit between them?

### 3. Technical lens
Ask: which protocols, data models, interfaces, and security controls are in play?

### 4. Assurance lens
Ask: what would need to be tested, evidenced, audited, certified, or reported?

## Structural mental model

A useful way to read ARF is as a bridge between:

- legal obligation
- architectural decomposition
- implementation detail
- conformance and assurance activity

That is why companion repositories like this one matter. ARF is readable, but teams still need help turning it into implementation work, evidence planning, and change management.

## Where ARF stops

ARF is not the entire operating system of the framework.

It does not replace:

- each implementing regulation
- STS tracking and technical-specification work
- national implementation choices
- certification body judgment

## What this on-ramp adds

This repository adds:

- role-based entry points
- implementation-oriented checklists
- governance-to-control mapping
- synchronization guidance for moving upstream references

## Read next

- [legal-baseline-2026.md](./legal-baseline-2026.md)
- [conformance-interpretation-companion.md](./conformance-interpretation-companion.md)
- [implementation-checklist.md](./implementation-checklist.md)
