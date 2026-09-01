---
layout: default
title: "Upstream Sync Resolution — September 2026"
parent: "Operations"
grand_parent: "Documentation Home"
nav_order: 7
permalink: /docs/upstream-sync-resolution-2026-09/
authority_level: assurance-evidence
last_reviewed: 2026-09-01
upstream_dependencies:
  - sts
previous_page:
  title: "August 2026 Resolution"
  url: "/docs/upstream-sync-resolution-2026-08/"
next_page:
  title: "Reference"
  url: "/docs/reference/"
---
# Upstream Sync Resolution — September 2026

This record provides the human-review evidence for monitor-generated issue #13.

## Disposition register

| Issue | Source | Finding | Disposition | Local action | Closure evidence |
|---|---|---|---|---|---|
| #13 | `sts` | Default branch moved from `456310d` to `ee91a29`; the watched `docs/technical-specifications/` directory changed. The exact compare contains four commits and changes only TS5/TS6 relying-party-registration artifacts. | **Accepted substantive STS maintenance drift with bounded companion impact.** The interval refines TS5 service-level registration structures and API/schema artifacts, then publishes TS6 `1.2.2` naming and mapping corrections. | Keep STS authoritative; do not copy volatile schemas locally. Tighten implementation guidance so adopters verify current service-scoped trade-name/contact mappings, plural collection names, intermediary-service identifiers, and the exact upstream revision used for conformance evidence. | Upstream compare `456310dfa10e99f356976a97996b0068d9d6f5a9..ee91a294c833af5188726fd8c302c641212192aa`; `docs/implementation-checklist.md`; this disposition record; `CHANGELOG.md`. |

## Reviewed upstream impact

The reviewed interval changes nine files, all under the TS5/TS6 relying-party-registration surface. TS5 updates its main specification, OpenAPI, XSD, UML, JSON/data-model artifacts, and related image material. The TS5 maintenance work explicitly clarifies trade-name purpose, makes `serviceIdentifier` optional in the relevant service context, adds service-level `email` and `phone`, adjusts served-wallet-relying-party data, and corrects API behaviour.

The final TS6 `1.2.2` update aligns the textual mapping to the current TS5 model. Material implementation-facing corrections include:

- `tradeName` plus `WalletRelyingPartyService.serviceTradeName` for the trade-name mapping
- service-scoped contact mappings for `supportURI`, `phone`, and `email`
- plural collection names `entitlements`, `subEntitlements`, and `usesIntermediaries`
- intermediary associations expressed through service identifiers rather than the earlier `servedWRPS` representation

These are sufficiently concrete to matter to implementers, but they do not justify creating a second local schema authority.

## Authority and assurance conclusion

The issue is not a false positive. Upstream technical meaning moved inside the monitored STS surface. The correct synchronization action is therefore **accept + expose implementation checkpoints**, not schema duplication.

The repository remains a companion layer. STS owns the current TS5/TS6 technical specification and schemas; this repository owns the obligation to make revision-sensitive implementation and evidence expectations visible.

## Closure criteria satisfied

- upstream delta inspected at commit and file level
- local impact classified as bounded but substantive
- implementation checklist updated with revision-sensitive TS5/TS6 checks
- changelog records the accepted drift
- September disposition record preserves the human judgment and exact upstream evidence
- no upstream schema or normative text duplicated locally

{% include page-nav.html %}
