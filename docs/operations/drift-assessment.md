---
layout: default
title: "Drift Assessment"
parent: "Operations"
grand_parent: "Documentation Home"
nav_order: 3
permalink: /docs/operations/drift-assessment/
authority_level: companion-guidance
last_reviewed: 2026-07-22
upstream_dependencies:
  - arf
  - sts
  - attestation-rulebooks
previous_page:
  title: "Upstream Monitoring"
  url: "/docs/upstream-monitoring/"
next_page:
  title: "June 2026 Review"
  url: "/docs/upstream-sync-review-2026-06/"
---
# Drift Assessment

Use this procedure after the monitor reports a change.

| Step | Question | Evidence |
|---|---|---|
| classify | What source changed and what authority does it carry? | monitor report and source snapshot |
| scope | Which local interpretations or links depend on it? | impact list |
| decide | Is a content, control, or test update required? | approved assessment |
| implement | What files and artifacts change? | patch and test results |
| close | What proves alignment has been restored? | commit, report, and issue closure |

```mermaid
flowchart TD
  M[Monitor detects drift] --> C[Classify authority]
  C --> I[Assess local impact]
  I --> D{Change required?}
  D -- Yes --> P[Patch docs or controls]
  D -- No --> N[Record no-change rationale]
  P --> V[Validate and preserve evidence]
  N --> V
```

{% include page-nav.html %}
