# Public repository baseline

This record captures controls reviewed under issue #12. It is repository assurance evidence, not external certification.

| Control | State | Evidence | Residual risk |
|---|---|---|---|
| Purpose/maturity/adoption/upstream boundary | PASS | `README.md`, `PROJECT-STATUS.yaml`, `INDEX.md`, `REFERENCES.md` | Upstream ARF remains normative authority. |
| Licensing/release provenance | PASS | `LICENSE`, `CHANGELOG.md` | Publication remains maintainer judgment. |
| Security reporting/supported versions | PASS | `SECURITY.md` | Hosted private-reporting enablement remains platform evidence. |
| Contribution/community/support | PASS | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SUPPORT.md`, issue/PR templates | None identified. |
| Dependency updates | PASS | `.github/dependabot.yml` | Hosted Dependabot enablement remains platform evidence. |
| Default-branch protection | EVIDENCE REQUIRED | rulesets API returned no active ruleset on 2026-09-05 | Tracked separately as a repository-setting control. |
| Docs/examples/Pages validation | PASS / bounded | workflows and published on-ramp surfaces | Repository-local examples do not redefine upstream ARF. |
| Authority boundary | PASS | README/references/contributing | Guidance must remain traceable to upstream sources. |

## Completion boundary

Repository-owned baseline gaps are closed by the remediation PR. Default-branch protection remains a GitHub-hosted residual tracked separately.
