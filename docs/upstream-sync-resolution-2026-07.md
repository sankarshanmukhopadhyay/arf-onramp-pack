---
layout: default
title: "Upstream Sync Resolution — July 2026"
parent: "Operations"
grand_parent: "Documentation Home"
nav_order: 5
permalink: /docs/upstream-sync-resolution-2026-07/
authority_level: assurance-evidence
last_reviewed: 2026-07-27
upstream_dependencies:
  - arf
  - eidas_regulation_2024_1183
  - onboarding_ir_2026_798
  - eudi_wallet_portal
previous_page:
  title: "June 2026 Review"
  url: "/docs/upstream-sync-review-2026-06/"
next_page:
  title: "Reference"
  url: "/docs/reference/"
---
# Upstream Sync Resolution — July 2026

This record closes the four monitor-generated drift findings after human review. It distinguishes accepted upstream movement from transport or presentation noise and records the evidence used to re-baseline the monitor.

## Disposition register

| Issue | Source | Finding | Disposition | Local action | Closure evidence |
|---|---|---|---|---|---|
| #1 | `arf` | Default-branch and `CHANGELOG.md` SHA changed; release remained `v3.0.0`. | **Accepted upstream maintenance drift.** No watched architecture, annex, discussion-topic, or technical-specification path changed. | Re-baselined the repository to the observed ARF `v3.0.0` state and updated current-facing alignment statements. | State snapshot records release `v3.0.0`; local documentation now identifies ARF 3.0.0 as the current alignment target. |
| #2 | `eidas_regulation_2024_1183` | EUR-Lex returned HTTP 202 with an empty body, causing all fragments to appear removed. | **False positive caused by an unusable transport response.** | Restored the last-known-good legal snapshot. Monitor now rejects non-200 or substantively empty responses and preserves accepted evidence. | Regression tests cover 202/interstitial rejection and state preservation. |
| #3 | `onboarding_ir_2026_798` | EUR-Lex returned HTTP 202 with an empty body, causing all fragments to appear removed. | **False positive caused by an unusable transport response.** Human review also confirmed a corrigendum limited to German and Estonian versions. | Restored the last-known-good snapshot; documented corrigendum scope; no English guidance change required. | Legal baseline includes corrigendum relationship and language scope. |
| #4 | `eudi_wallet_portal` | ETag and `Last-Modified` changed while the content hash and watched fragments did not. | **Presentation-layer metadata noise.** | Portal monitoring now ignores volatile response metadata and full-page hash churn, retaining semantic fragment checks. | Tests confirm metadata-only portal changes do not create drift while fragment changes remain detectable. |

## Control improvements

1. **Evidence admission:** only HTTP 200 responses containing substantive content may replace the last-known-good snapshot.
2. **Failure containment:** fetch anomalies are reported as monitor errors and do not become authority drift or overwrite accepted evidence.
3. **Source-sensitive comparison:** legal sources retain metadata monitoring; the public portal is assessed through semantic fragment presence rather than volatile delivery metadata.
4. **Human disposition:** legal drift remains non-automated. Closure requires a recorded no-change rationale or an attributable documentation update.

## Assurance conclusion

The four open issues do not represent four substantive upstream changes. One is accepted ARF maintenance drift, two are EUR-Lex response-quality false positives, and one is portal metadata noise. The payload resolves the immediate findings and removes the failure modes that would otherwise recreate them.

{% include page-nav.html %}
