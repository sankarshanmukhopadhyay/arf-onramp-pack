---
layout: default
title: "Upstream Sync Resolution — August 2026"
parent: "Operations"
grand_parent: "Documentation Home"
nav_order: 6
permalink: /docs/upstream-sync-resolution-2026-08/
authority_level: assurance-evidence
last_reviewed: 2026-08-21
upstream_dependencies:
  - arf
  - sts
  - eudi_wallet_portal
  - eidas_regulation_2024_1183
  - onboarding_ir_2026_798
previous_page:
  title: "July 2026 Resolution"
  url: "/docs/upstream-sync-resolution-2026-07/"
next_page:
  title: "Reference"
  url: "/docs/reference/"
---
# Upstream Sync Resolution — August 2026

This record provides the human-review evidence for monitor-generated issues #5 through #10. The review separates substantive upstream changes that require local companion updates from monitoring-state transitions and source-representation volatility that do not represent authority drift.

## Disposition register

| Issue | Source | Finding | Disposition | Local action | Closure evidence |
|---|---|---|---|---|---|
| #5 | `arf` | Default branch moved from `299b7da` to `6373eee`; the watched annex set changed while the authoritative release remained `v3.0.0`. | **Accepted ARF 3.0.0 maintenance drift with local impact.** The interval adds notice of CIR (EU) 2026/1730, 2026/1731, and 2026/1735 and revises HLR `ISSU_33b` so Wallet Providers support attestations in the Commission-managed catalogue of attestation schemes. | Updated the legal/reference baseline and implementation checklist; retained ARF 3.0.0 as the synchronization target because no new tagged release was detected. | `REFERENCES.md`, `docs/legal-baseline-2026.md`, and `docs/implementation-checklist.md` expose the amendment check and catalogue-support implementation obligation. |
| #6 | `sts` | Default branch moved from `b53874f` to `230cd75d`; `docs/technical-specifications/` changed. | **Accepted substantive STS maintenance drift.** The detected interval updates TS5 and TS6 around relying-party registration information, Wallet-Relying Party Service structures, schemas, metadata, and related lifecycle semantics. | Kept STS as the authoritative technical-specification source and added an explicit TS5/TS6 implementation/evidence checkpoint rather than copying volatile schemas into this companion repository. | `docs/architecture-layer-map.md` and `docs/implementation-checklist.md` require current TS5/TS6 alignment and evidence of the implemented revision/schema set. |
| #7 | `eudi_wallet_portal` | The monitor reported `content_hash_changed` when the configured portal policy had already disabled full-page hashing (`page_hash: false`), causing the legacy stored hash to transition to `null`. Watched semantic fragments did not change. | **Monitoring-state transition; not portal content drift.** | Changed drift classification so a disabled page hash is never compared as content evidence. Added a regression test covering legacy-hash → disabled-hash transition. | `scripts/check_upstream_sync.py` and `tests/test_check_upstream_sync.py` prevent recurrence; the state snapshot is already re-baselined with `content_hash: null`. |
| #8 | `sts` | Default branch moved from `bdc9780` to `456310d`; the watched technical-specification directory changed. The reviewed delta is confined to TS8, the common interface for reporting Wallet Relying Party information to Data Protection Authorities, plus its architecture diagrams. | **Accepted STS maintenance drift with no current companion semantic impact.** | No local TS8 schema or interface text is duplicated in this repository. Retained STS as the authoritative source and accepted the new upstream state. | Exact upstream compare `bdc9780..456310d` shows two commits affecting TS8 and associated SVGs only; no current companion guidance requires semantic remediation. |
| #9 | `eidas_regulation_2024_1183` | The monitor raised `content_hash_changed`, while every watched legal-semantic fragment remained present. | **Rendered EUR-Lex page volatility; no demonstrated normative legal drift.** | Disabled volatile full-page hashing for EUR-Lex legal sources while retaining fragment checks, source identity, retrieval admission controls, metadata review, and mandatory human legal review. | `governance/upstream-sources.yaml` now sets `page_hash: false` for EUR-Lex documents; regression tests require that policy and verify legacy-hash transition does not create legal drift. |
| #10 | `onboarding_ir_2026_798` | The monitor raised `content_hash_changed`, while every watched onboarding fragment remained present and the existing legal baseline already records the language-limited corrigendum. | **Rendered EUR-Lex page volatility; no new English-language semantic change identified.** | Applied the same stable legal-source monitoring policy as #9; retained the existing human-reviewed onboarding interpretation. | `governance/upstream-sources.yaml`, monitor regression tests, and `docs/legal-baseline-2026.md` provide the control and prior legal-review evidence. |

## Authority and assurance conclusion

The ARF and STS findings are real upstream maintenance changes, but they do not automatically justify copying upstream specifications into this companion repository. The companion pack absorbs only implementation-facing consequences that fall within its scope and records no-change dispositions where the authoritative source remains upstream.

The portal and EUR-Lex findings are monitoring-quality findings. A rendered HTTP representation is transport evidence, not itself proof of normative change. Full-page hashing is therefore disabled for the volatile portal and EUR-Lex pages, while semantic-fragment monitoring, stable source identity, response-admission checks, metadata review, and required human legal review remain in force. This reduces false positives without changing the authority ordering or allowing automated legal interpretation.

## Closure criteria satisfied

- local documentation synchronized to reviewed ARF and STS changes where companion impact exists
- no-change rationale recorded for STS issue #8
- human legal-source review recorded for issues #9 and #10
- volatile EUR-Lex full-page hashing removed as a critical drift signal
- semantic fragment monitoring and mandatory legal review retained
- regression tests added for the false-positive class
- commit metadata and issue comments provide traceable closure evidence

{% include page-nav.html %}
