# ARF On-Ramp Pack
### EU Digital Identity Wallet Architecture & Reference Framework (ARF) Implementation Companion

This repository provides **structured orientation, implementation guidance, and conformance interpretation support** for the EU Digital Identity Wallet Architecture and Reference Framework (ARF).

The on-ramp is **not a fork** of the upstream ARF repository—it is a companion documentation and guidance project designed to help implementers, architects, policy leaders, and assurance teams navigate the ARF landscape more effectively.

---

## What is This?

The **ARF On-Ramp Pack** distills the upstream ARF into role-oriented reading paths, architectural decompositions, and implementation-facing guidance. Use it to:

- **Understand the landscape** → Start with role-specific reading paths
- **Navigate the ARF** → Use architecture layer maps and quick-reference guides
- **Interpret conformance** → Translate normative requirements into testable behaviors
- **Track progress** → Monitor upstream releases and changes against your implementation
- **Find governance patterns** → Map governance constructs to control implementations

---

## Upstream Synchronization Status

| Resource | Latest Version | Release Date | On-Ramp Coverage | Status |
|----------|-----------------|--------------|-----------------|--------|
| **ARF Main Document** | 2.8.0 | 2026-02-02 | Aligned with v2.8.0 | ✅ Current |
| **Technical Specifications** | Active (see[Technical Specs Roadmap](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/technical-specifications)) | Ongoing | Referenced | 📝 Partial |
| **Discussion Topics** | Multiple active topics | Ongoing | Topic F, P, Q, R, S, T, AA mapped | 📝 In progress |
| **High-Level Requirements (Annex 2)** | CSV + Markdown formats | Updated 2025-11-10 | Structured for conformance | ✅ Current |
| **Rulebooks Catalog** | Moved to [separate repo](https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog/) | 2025-09-12 | Linked & referenced | ✅ Linked |

**Repository Links:**
- **Upstream ARF:** https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework
- **Rulebooks:** https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog/
- **Discussion Topics:** https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/discussion-topics

---

## How to Use This Pack

### For Different Roles

Start with the path that matches your primary responsibility:

- **Policy / Program Leadership** → [reading-path-policy-leadership.md](./docs/reading-paths/reading-path-policy-leadership.md)  
  *Focus: regulatory intent, ecosystem governance, stakeholder roles*

- **Architects / System Designers** → [reading-path-architect.md](./docs/reading-paths/reading-path-architect.md)  
  *Focus: reference architecture, design patterns, trust boundaries*

- **Implementers / Engineering Teams** → [reading-path-implementer.md](./docs/reading-paths/reading-path-implementer.md)  
  *Focus: protocols, data flows, implementation requirements*

- **Security / Privacy / Assurance** → [reading-path-security-assurance.md](./docs/reading-paths/reading-path-security-assurance.md)  
  *Focus: threat models, security controls, compliance evidence*

### For Understanding the Landscape

1. **[ARF Explained](./docs/arf-explained.md)** — Structural walkthrough of the ARF (layers, trust boundaries, governance)
2. **[Architecture Layer Map](./docs/architecture-layer-map.md)** — Decomposition into governance, trust, wallet, protocol, and interop layers
3. **[Upstream Alignment Guide](./docs/upstream-alignment-guide.md)** — Track ARF changes and map them to your implementation
4. **[Conformance Interpretation Companion](./docs/conformance-interpretation-companion.md)** — Translate normative requirements into testable behaviors
5. **[Governance to Control Mapping](./docs/governance-to-control-mapping.md)** — Map governance constructs to technical controls
6. **[Quick Reference & Glossary](./docs/quick-reference.md)** — Regulatory links, key terms, abbreviations, and resources

---

## Key Concepts at a Glance

### The ARF Covers

The **Architecture and Reference Framework** (ARF) is the technical blueprint for EU Digital Identity Wallets. It specifies:

- **Wallet roles and responsibilities** — Wallet Provider, Wallet Instance, Wallet Unit, Wallet Solution
- **Trust model** — PID Provider, Attestation Provider, Relying Party, Supervisory Bodies
- **Data flows** — Proximity (NFC), Remote (same-device, cross-device), and registration flows
- **Protocol requirements** — OpenID4VCI, OpenID4VP, HAIP, and other standards
- **Governance & compliance** — Conformance profiles, certification rules, and supervisory oversight
- **Security, integrity & accessibility** — Controls, assurance evidence, and accessible design

### What This On-Ramp Adds

| Document | Purpose | Use Case |
|----------|---------|----------|
| Reading Paths | Role-oriented entry points | "Where do I start?" |
| ARF Explained | Simplified structural guide | "What are the main layers?" |
| Architecture Layer Map | Logical decomposition | "How does X relate to Y?" |
| Conformance Companion | Implementation-facing interpretation | "What does this requirement mean for my code?" |
| Governance to Control Mapping | Links governance to technical controls | "How do I implement policy requirement Z?" |
| Upstream Alignment Guide | Track ARF changes and impact | "What changed and how does it affect us?" |
| Quick Reference | Glossary, links, regulations | "What does WSCA mean? What's the latest CIR?" |

---

## Repository Structure

```
arf-onramp-pack/
├── README.md                                 (this file)
├── docs/
│   ├── arf-explained.md                      Structural walkthrough
│   ├── architecture-layer-map.md             Logical decomposition
│   ├── conformance-interpretation-companion.md  Requirement interpretation
│   ├── governance-to-control-mapping.md      Governance → Technical controls
│   ├── upstream-alignment-guide.md           Track ARF versions and changes
│   ├── quick-reference.md                    Glossary, links, resources
│   └── reading-paths/
│       ├── README.md                         Reading path overview
│       ├── reading-path-policy-leadership.md
│       ├── reading-path-architect.md
│       ├── reading-path-implementer.md
│       └── reading-path-security-assurance.md
└── .github/
    └── CHANGELOG.md                          On-ramp release notes
```

---

## Key ARF Resources

### Regulatory Foundation
- **EU Digital Identity Regulation:** https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18
- **Commission Implementing Regulations (CIRs):** Latest CIRs listed in [upstream README](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/README.md)

### Official ARF Documentation
- **Architecture & Reference Framework (main document):** [docs/architecture-and-reference-framework-main.md](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md)
- **Annexes (High-Level Requirements):** [docs/annexes/](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/annexes)
- **Discussion Topics (open consultation):** [docs/discussion-topics/](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/discussion-topics)

### Technical Specifications
- **Specifications Roadmap:** [docs/technical-specifications/](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/technical-specifications)
- **Attestation Rulebooks:** https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog/

### Community & Governance
- **European Digital Identity Cooperation Group (EDICG):** https://digital-strategy.ec.europa.eu/en/policies/european-digital-identity-cooperation-group
- **EUDI Wallet Official Website:** https://ec.europa.eu/digital-building-blocks/sites/spaces/EUDIGITALIDENTITYWALLET/

---

## For ARF Implementers

### Common Implementation Scenarios

**Implementing a Wallet Provider?**
1. Read [reading-path-architect.md](./docs/reading-paths/reading-path-architect.md) for system design
2. Review [conformance-interpretation-companion.md](./docs/conformance-interpretation-companion.md) for normative mapping
3. Use [governance-to-control-mapping.md](./docs/governance-to-control-mapping.md) to plan your controls
4. Check [upstream-alignment-guide.md](./docs/upstream-alignment-guide.md) for recent ARF changes

**Building a Relying Party Service?**
1. Start with [reading-path-implementer.md](./docs/reading-paths/reading-path-implementer.md)
2. Review ARF Sections 4.5 (Relying Party) and 6.4 (Remote Authentication)
3. Map protocol requirements to your tech stack via [conformance-interpretation-companion.md](./docs/conformance-interpretation-companion.md)
4. Use [quick-reference.md](./docs/quick-reference.md) for protocol links and standards

**Ensuring Security & Compliance?**
1. Read [reading-path-security-assurance.md](./docs/reading-paths/reading-path-security-assurance.md)
2. Review ARF Chapter 6 (Security, Integrity, and Accessibility)
3. Use [governance-to-control-mapping.md](./docs/governance-to-control-mapping.md) to align governance to controls
4. Track ARF security changes in [upstream-alignment-guide.md](./docs/upstream-alignment-guide.md)

---

## Contributing to This On-Ramp

This is a companion documentation project, not the authoritative ARF. Contributions are welcome:

1. **Suggest improvements** via GitHub Issues
2. **Clarify guidance** that has proven confusing to implementers
3. **Expand examples** with real-world patterns and case studies
4. **Track upstream changes** and update alignment documents

See [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

---

## Staying Synchronized with Upstream

The upstream ARF updates regularly. To stay current:

1. **Monitor releases:** [ARF Releases](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/releases)
2. **Read the CHANGELOG:** [ARF CHANGELOG.md](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/CHANGELOG.md)
3. **Track Discussion Topics:** New topics guide upcoming ARF changes
4. **Use our alignment guide:** [upstream-alignment-guide.md](./docs/upstream-alignment-guide.md) maps recent changes to on-ramp docs

The on-ramp will be updated quarterly to reflect ARF changes. When major versions shift, we will release companion migration guides.

---

## Versioning

This on-ramp follows [Semantic Versioning](https://semver.org/):

- **MAJOR** version increases align with **upstream ARF major versions**
- **MINOR** version increases reflect **expanded guidance or new documents**
- **PATCH** version increases reflect **clarifications, fixes, or upstream tracking updates**

See [CHANGELOG.md](./.github/CHANGELOG.md) for release notes.

---

## License

This on-ramp pack is provided under the same license as the upstream ARF. See [LICENSE](./LICENSE) for details.

---

## Questions or Feedback?

- **ARF questions:** See the [upstream repository](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework)
- **On-ramp guidance questions:** File an issue in this repository
- **Official EUDI contacts:** https://commission.europa.eu/about-european-commission/contact_en

---

## Quick Links by Role

| Role | Start Here | Then Read |
|------|------------|-----------|
| **Policy / Leadership** | [reading-path-policy-leadership.md](./docs/reading-paths/reading-path-policy-leadership.md) | [arf-explained.md](./docs/arf-explained.md) → [ARF main](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) Chapters 1–3 |
| **Architect** | [reading-path-architect.md](./docs/reading-paths/reading-path-architect.md) | [architecture-layer-map.md](./docs/architecture-layer-map.md) → [ARF main](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) Chapters 2–5 |
| **Implementer** | [reading-path-implementer.md](./docs/reading-paths/reading-path-implementer.md) | [conformance-interpretation-companion.md](./docs/conformance-interpretation-companion.md) → [ARF main](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) Chapter 6 + [Technical Specs](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/technical-specifications) |
| **Security / Assurance** | [reading-path-security-assurance.md](./docs/reading-paths/reading-path-security-assurance.md) | [governance-to-control-mapping.md](./docs/governance-to-control-mapping.md) → [ARF main](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) Chapter 6 |

---

**Last Updated:** March 2026  
**ARF Alignment:** v2.8.0 (2026-02-02)
