# Contributing

Thank you for helping improve the ARF On-Ramp Pack.

## Project posture

This repository is a **companion documentation and governance-support project**. It is not the authoritative source of law, certification criteria, or upstream technical specification text.

Contributions should improve one or more of the following:

- orientation and navigability
- implementation clarity
- traceability to upstream authority
- synchronization with upstream repositories and legal texts
- evidence and auditability for repository maintenance

## Contribution principles

### 1. Preserve authority boundaries
Do not present companion interpretation as if it were binding law or upstream normative text.

### 2. Prefer machine-verifiable maintenance where possible
If a synchronization problem can be detected automatically, prefer improving the control plane rather than relying on memory.

### 3. Keep ARF and STS distinct
Use the ARF repository for architecture narrative and annexes. Use the STS repository for standards and technical-specification tracking.

### 4. Cite legal instruments correctly
- cite **Regulation (EU) 2024/1183** as an amending regulation
- cite wallet-core implementing regulations individually where they are the legal basis for a process or requirement

## Typical contribution types

- documentation corrections
- upstream-link repairs
- release synchronization updates
- new examples and implementation guidance
- issue template or workflow improvements for the upstream control plane
- glossary and quick-reference updates

## File-level expectations

A strong synchronization or legal-refresh PR should usually include:

- affected doc updates
- `CHANGELOG.md` update
- evidence of what changed upstream
- release-note language if the change is substantive

## Writing style

- be explicit about what is authoritative and what is interpretive
- write for implementation teams, architects, policy leads, and assurance teams
- prefer concrete operational language over abstract commentary
- mark uncertainty where the repository is extrapolating from upstream structure rather than quoting it directly

## Validation expectations

Where relevant, contributors should validate:

- internal relative links
- canonical upstream repository paths
- affected legal instrument identifiers
- workflow syntax for GitHub Actions
- JSON/YAML validity for machine-readable artifacts


## Documentation architecture requirements

Pages published through GitHub Pages must include valid YAML front matter, an authority classification, upstream dependencies where applicable, and a stable permalink. Sequenced pages must render `{% include page-nav.html %}` and define `previous_page` and/or `next_page` metadata.

Run before submitting documentation changes:

```bash
python scripts/validate_docs.py
bundle exec jekyll build --trace
```

## Synchronization workflow

If your change is driven by upstream drift:

1. record the drift source
2. update impacted docs or explain why no doc changes are required
3. update release notes or changelog if the change is non-trivial
4. close or reference the associated synchronization issue

## Pull request guidance

Include:

- what changed
- why it changed
- what upstream or legal source triggered the change
- what validation you performed

## Scope guardrails

Please do not use this repository to publish:

- new normative wallet requirements
- conflicting interpretations that ignore the current legal and upstream baseline
- stale repository URLs after a canonical upstream move has been identified
