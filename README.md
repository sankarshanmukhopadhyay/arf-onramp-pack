# ARF On-Ramp Pack
### EU Digital Identity Wallet Architecture & Reference Framework (ARF) Implementation Companion

This repository provides **structured orientation, implementation guidance, and conformance interpretation support** for the EU Digital Identity Wallet Architecture and Reference Framework (ARF) — the technical blueprint for implementing the [EU Digital Identity Regulation](https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18).

The on-ramp is **not a fork** of the upstream ARF repository—it is a companion documentation and guidance project designed to help implementers, architects, policy leaders, and assurance teams navigate the ARF landscape more effectively.

**ARF Version Alignment:** 2.8.0 (February 2, 2026)  
**Regulatory Basis:** [eIDAS Regulation 2014/910/EU](https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18) (as amended by [Regulation 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj))

---

## What is This?

The **ARF On-Ramp Pack** distills the upstream ARF into role-oriented reading paths, architectural decompositions, and implementation-facing guidance. Use it to:

- **Understand the landscape** → Start with role-specific reading paths anchored to ARF chapters and regulatory requirements
- **Navigate the ARF** → Use architecture layer maps and quick-reference guides with full citation trails
- **Interpret conformance** → Translate normative requirements into testable behaviors with evidence collection strategies
- **Track progress** → Monitor upstream releases and changes against your implementation using systematic alignment guides
- **Find governance patterns** → Map governance constructs to control implementations with security control frameworks

---

## Upstream Synchronization Status

| Resource | Latest Version | Release Date | On-Ramp Coverage | Regulatory Authority | Status |
|----------|-----------------|--------------|-----------------|--------|--------|
| **ARF Main Document** | 2.8.0 | 2026-02-02 | Aligned with v2.8.0 | [ARF Repo](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | ✅ Current |
| **Technical Specifications** | Active | Ongoing | Referenced | [Tech Specs Roadmap](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/technical-specifications) | 📝 Partial |
| **Discussion Topics** | Multiple active | Ongoing | Topics F, P, Q, R, S, T, AA mapped | [GitHub Discussions](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/discussion-topics) | 📝 In progress |
| **High-Level Requirements (Annex 2)** | Current | 2025-11-10 | Structured for conformance | [ARF Annexes](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/annexes) | ✅ Current |
| **Rulebooks Catalog** | Active | 2025-09-12 | Linked & referenced | [Rulebooks Repo](https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog/) | ✅ Linked |
| **CIR 2024/1183 Implementation** | Final | 2024-10-18 | Governance and control mappings | [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) | ✅ Mapped |

**Repository Links:**
- **Upstream ARF (authoritative):** https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework
- **ARF Main Document (v2.8.0):** https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md
- **Attestation Rulebooks Catalog:** https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog/
- **Discussion Topics & Consultation:** https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/discussion-topics
- **Technical Specifications Roadmap:** https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/technical-specifications

---

## How to Use This Pack

### For Different Roles

Start with the path that matches your primary responsibility:

- **Policy / Program Leadership** → [reading-path-policy-leadership.md](./docs/reading-paths/reading-path-policy-leadership.md)  
  *Focus: regulatory intent (eIDAS, CIRs), ecosystem governance, stakeholder roles, conformance certification*

- **Architects / System Designers** → [reading-path-architect.md](./docs/reading-paths/reading-path-architect.md)  
  *Focus: five-layer reference architecture, design patterns, trust boundaries, assurance levels*

- **Implementers / Engineering Teams** → [reading-path-implementer.md](./docs/reading-paths/reading-path-implementer.md)  
  *Focus: OpenID4VCI/4VP protocols, SD-JWT/CWT data formats, cryptographic implementation, testing strategies*

- **Security / Privacy / Assurance** → [reading-path-security-assurance.md](./docs/reading-paths/reading-path-security-assurance.md)  
  *Focus: threat models, security controls (ARF Chapter 6), GDPR alignment, assurance level evidence*

### For Understanding the Landscape

1. **[ARF Explained](./docs/arf-explained.md)** — Structural walkthrough of the ARF (layers, trust boundaries, governance, regulatory foundation)
2. **[Architecture Layer Map](./docs/architecture-layer-map.md)** — Five-layer decomposition (Governance → Trust → Infrastructure → Protocol → Interop) with ARF chapter mappings
3. **[Upstream Alignment Guide](./docs/upstream-alignment-guide.md)** — Track ARF changes, version-by-version impact assessments, quarterly sync checklist
4. **[Conformance Interpretation Companion](./docs/conformance-interpretation-companion.md)** — Translate normative requirements (ARF Annex 2: HLRs) into testable behaviors with evidence types
5. **[Governance to Control Mapping](./docs/governance-to-control-mapping.md)** — Map governance requirements (eIDAS, CIRs) to technical security controls with patterns
6. **[Quick Reference & Glossary](./docs/quick-reference.md)** — 100+ searchable glossary entries, regulatory links (EUR-Lex), standards (OpenID, ISO/IEC), resources

---

## Key Concepts at a Glance

### The ARF Covers (ARF v2.8.0 Scope)

The **Architecture and Reference Framework** (ARF) is the technical blueprint mandated by [Regulation 2014/910/EU](https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18) and implemented through [Commission Implementing Regulations](https://eur-lex.europa.eu/search.html?queryText=digital%20identity&qf=eurovoc:32268&type=reg&subject=all&lang=en&page=1). It specifies:

- **Wallet roles and responsibilities** — Wallet Provider, Wallet Instance, Wallet Unit, Wallet Solution (ARF Ch. 3)
- **Trust model** — PID Provider, Attestation Provider, Relying Party, Supervisory Bodies (ARF Ch. 3–4)
- **Data flows** — Proximity (NFC), Remote (same-device, cross-device), registration flows (ARF Ch. 4)
- **Protocol requirements** — [OpenID4VCI v1.0](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html), [OpenID4VP v1.0](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html), [HAIP](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/technical-specifications/), and other standards (ARF Ch. 5)
- **Governance & compliance** — Conformance profiles (AL1–AL4), certification rules, supervisory oversight (ARF Ch. 7)
- **Security, integrity & accessibility** — Controls (ARF Ch. 6), assurance evidence, accessible design (ARF Ch. 8)

**Regulatory Implementation:**
- **eIDAS Regulation 2014/910/EU** (amended by [Regulation 2024/1183/EU](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)): Articles 5–6 define the wallet
- **Commission Implementing Regulation (EU) 2023/1411**: Technical specifications for pilot phase
- **Commission Implementing Regulation (EU) 2024/1183**: Final technical specifications and conformance rules
- **Digital Identity Cooperation Group (DICG)**: Governance and interoperability oversight

### What This On-Ramp Adds

| Document | Purpose | Regulatory Basis | Use Case |
|----------|---------|-----------------|----------|
| Reading Paths | Role-oriented entry points | ARF structure alignment | "Where do I start?" |
| ARF Explained | Simplified structural guide | ARF Chapters 1–8 summary | "What are the main layers?" |
| Architecture Layer Map | Logical decomposition | ARF Ch. 3–5, 7 architecture refs | "How does X relate to Y?" |
| Conformance Companion | Implementation-facing interpretation | ARF Annex 2 (HLRs 1–55) | "What does this requirement mean for my code?" |
| Governance to Control Mapping | Links governance to technical controls | eIDAS + CIR 2024/1183 + ARF Ch. 6 | "How do I implement policy requirement Z?" |
| Upstream Alignment Guide | Track ARF changes and impact | ARF versioning, CIR amendments | "What changed and how does it affect us?" |
| Quick Reference | Glossary, links, regulations | All referenced standards/CIRs | "What does WSCA mean? What's the latest CIR?" |

---

## Repository Structure

```
arf-onramp-pack/
├── README.md                                 (this file, overview & quick links)
├── CHANGELOG.md                              (release notes with version history)
├── CONTRIBUTING.md                           (community guidelines & style guide)
├── INDEX.md                                  (complete file index & navigation)
├── ENHANCEMENT_SUMMARY.md                    (what was improved & why)
└── docs/
    ├── arf-explained.md                      (simplified structural walkthrough)
    ├── architecture-layer-map.md             (five-layer decomposition with patterns)
    ├── conformance-interpretation-companion.md  (requirements→evidence planning)
    ├── governance-to-control-mapping.md      (policy→controls with frameworks)
    ├── upstream-alignment-guide.md           (ARF version tracking & migration)
    ├── quick-reference.md                    (100+ glossary entries, links, resources)
    ├── implementation-checklist.md           (task-oriented implementation guide)
    ├── faq-by-role.md                        (40+ common questions with answers)
    └── reading-paths/
        ├── README.md                         (reading path overview & navigation)
        ├── reading-path-policy-leadership.md (policy leaders: 40 KB, 30–45 min)
        ├── reading-path-architect.md         (architects: 50 KB, 45–60 min)
        ├── reading-path-implementer.md       (developers: 60 KB, 60–90 min)
        └── reading-path-security-assurance.md (security teams: 55 KB, 60–90 min)
```

---

## Key ARF Resources

### Regulatory & Governance Foundation

- **[eIDAS Regulation 2014/910/EU](https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18)** (as amended)
  - Articles 5–6 define EU Digital Identity Wallet requirements
  - Enforced through Commission Implementing Regulations (CIRs)

- **[Commission Implementing Regulation (EU) 2023/1411](https://eur-lex.europa.eu/eli/reg/2023/1411/oj)**
  - Technical specifications for the pilot phase (Articles 1–5)
  - Wallet conformance requirements

- **[Commission Implementing Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)** ← **CURRENT**
  - Final technical specifications (Articles 1–8)
  - Governance and certification rules (Articles 9–13)
  - Attestation rulebooks and compliance framework
  - Adopted October 18, 2024; application date: October 18, 2025

### Official ARF Documentation

- **[Architecture & Reference Framework Main Document (v2.8.0, Feb 2026)](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md)**
  - 389 KB comprehensive reference document
  - Chapters 1–8: Scope, Overview, Roles, Flows, Protocols, Security, Governance, Accessibility
  
- **[ARF Annexes (High-Level Requirements & Mappings)](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/annexes)**
  - Annex 1: Acronyms and Definitions
  - Annex 2: High-Level Requirements (HLRs 1–55) with traceability
  - Annex 3: ARF-to-CIR Mapping
  - Annex 4: Member State Declarations & Governance

- **[Discussion Topics (Open Consultation)](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/discussion-topics)**
  - Topic F: Trust Registry Query Protocol (TRQP)
  - Topic P: Device Binding and Hardware Security
  - Topic Q: Relying Party Federation Models
  - Topic R: Cross-Border Interoperability
  - Topic S: Attestation Rulebook Extensibility
  - Topics T, AA, etc.: Emerging requirements

### Technical Specifications

- **[Technical Specifications Roadmap](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/technical-specifications)**
  - OpenID4VCI binding specifications
  - OpenID4VP binding specifications
  - SD-JWT and CWT serialization
  - HAIP (HTTP Authentication Interop Protocol) specifications
  - Cryptographic algorithms and key management

- **[Attestation Rulebooks Catalog](https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog/)**
  - Structured attestation schemas by credential type
  - JSON Schema definitions for each credential rulebook
  - PID (Personal Identification Data) rulebook
  - Attestation Provider rulebooks (driving license, etc.)
  - Community contributions and extensibility patterns

### Community & Governance

- **[European Digital Identity Cooperation Group (EDICG)](https://digital-strategy.ec.europa.eu/en/policies/european-digital-identity-cooperation-group)**
  - Multi-stakeholder governance body
  - Quarterly meetings and working groups
  - Public consultation on discussion topics

- **[EUDI Wallet Official Website](https://ec.europa.eu/digital-building-blocks/sites/spaces/EUDIGITALIDENTITYWALLET/)**
  - Implementation guidance
  - Pilot phase outcomes
  - Community resources

- **[ARF GitHub Repository](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework)** — Issues, discussions, release notes

---

## For ARF Implementers

### Common Implementation Scenarios

**Implementing a Wallet Provider?**
1. Read [reading-path-architect.md](./docs/reading-paths/reading-path-architect.md) for system design (ARF Ch. 3, 5)
2. Review [conformance-interpretation-companion.md](./docs/conformance-interpretation-companion.md) for normative mapping (ARF Annex 2: HLRs)
3. Use [governance-to-control-mapping.md](./docs/governance-to-control-mapping.md) to plan your controls (ARF Ch. 6, CIR 2024/1183)
4. Check [upstream-alignment-guide.md](./docs/upstream-alignment-guide.md) for recent ARF changes and migration impact
5. Reference [quick-reference.md](./docs/quick-reference.md) for protocol specs (OpenID4VCI/4VP, SD-JWT, CWT)

**Building a Relying Party Service?**
1. Start with [reading-path-implementer.md](./docs/reading-paths/reading-path-implementer.md) (ARF Ch. 4.5, 6.4)
2. Study OpenID4VP spec and HAIP protocol (linked in [quick-reference.md](./docs/quick-reference.md))
3. Map protocol requirements to your tech stack via [conformance-interpretation-companion.md](./docs/conformance-interpretation-companion.md)
4. Review threat model in [reading-path-security-assurance.md](./docs/reading-paths/reading-path-security-assurance.md)
5. Plan certification evidence using governance and control mappings

**Ensuring Security & Compliance?**
1. Read [reading-path-security-assurance.md](./docs/reading-paths/reading-path-security-assurance.md) (ARF Ch. 6)
2. Review ARF Chapter 6 (Security, Integrity, Accessibility) and [CIR 2024/1183 Article 9](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) (Conformance Rules)
3. Use [governance-to-control-mapping.md](./docs/governance-to-control-mapping.md) to align governance requirements to controls
4. Track ARF security changes in [upstream-alignment-guide.md](./docs/upstream-alignment-guide.md)
5. Prepare assurance evidence using [conformance-interpretation-companion.md](./docs/conformance-interpretation-companion.md) Evidence Types section

**Planning Member State Wallet Governance?**
1. Read [reading-path-policy-leadership.md](./docs/reading-paths/reading-path-policy-leadership.md) (regulatory foundation)
2. Review [eIDAS Regulation Articles 5–6](https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18) and [CIR 2024/1183 Articles 9–13](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
3. Use [governance-to-control-mapping.md](./docs/governance-to-control-mapping.md) to map governance domains
4. Set up quarterly ARF monitoring using [upstream-alignment-guide.md](./docs/upstream-alignment-guide.md) checklist
5. Reference [quick-reference.md](./docs/quick-reference.md) for CIR and regulatory links

---

## Contributing to This On-Ramp

This is a companion documentation project, not the authoritative ARF. Contributions are welcome:

1. **Suggest improvements** via GitHub Issues (cite ARF version and section)
2. **Clarify guidance** that has proven confusing to implementers (reference real implementation scenarios)
3. **Expand examples** with real-world patterns and case studies (include protocol/tech stack details)
4. **Track upstream changes** and update alignment documents (reference ARF release notes and CIR updates)
5. **Add regulatory citations** and cross-references (EUR-Lex links, CIR articles)

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed contribution guidelines, citation style, and review process.

---

## Staying Synchronized with Upstream

The upstream ARF updates regularly, and Commission Implementing Regulations are amended through the legislative process. To stay current:

1. **Monitor ARF releases:** [ARF Releases Page](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/releases)
2. **Read the ARF CHANGELOG:** [CHANGELOG.md](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/CHANGELOG.md)
3. **Track CIR amendments:** [EUR-Lex Search](https://eur-lex.europa.eu/search.html?queryText=2024/1183&type=reg) for updates to CIR 2024/1183
4. **Monitor Discussion Topics:** [GitHub Discussions](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/discussion-topics) guide upcoming ARF changes
5. **Use our alignment guide:** [upstream-alignment-guide.md](./docs/upstream-alignment-guide.md) maps recent changes to on-ramp docs

**On-Ramp Update Cadence:**
- The on-ramp will be updated **quarterly** to reflect ARF changes (ARF release cycle)
- When ARF major versions shift (e.g., v3.0), **migration guides** will be released
- When CIRs are amended, governance and control mappings will be updated within one month

---

## Versioning

This on-ramp follows [Semantic Versioning](https://semver.org/):

- **MAJOR** version increases align with **upstream ARF major versions** (v2→v3)
- **MINOR** version increases reflect **expanded guidance, new documents, or significant regulatory updates**
- **PATCH** version increases reflect **clarifications, fixes, regulatory citations, or upstream tracking updates**

See [CHANGELOG.md](./CHANGELOG.md) for detailed release notes.

**Current Release:** v1.0.0 (March 2026) — Aligned with ARF v2.8.0 and CIR 2024/1183

---

## License

This on-ramp pack is provided under the same license as the upstream ARF. See [LICENSE](./LICENSE) for details.

---

## Questions or Feedback?

- **ARF questions:** See the [upstream repository](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework) and its issue tracker
- **Regulatory questions (eIDAS, CIRs):** See [EUR-Lex](https://eur-lex.europa.eu/) or [EDICG](https://digital-strategy.ec.europa.eu/en/policies/european-digital-identity-cooperation-group)
- **On-ramp guidance questions:** File an issue in this repository (cite relevant ARF section and use case)
- **Official EUDI support:** https://commission.europa.eu/about-european-commission/contact_en

---

## Quick Links by Role

| Role | Start Here | Then Read | Regulatory Reference |
|------|------------|-----------|----------------------|
| **Policy / Leadership** | [reading-path-policy-leadership.md](./docs/reading-paths/reading-path-policy-leadership.md) | [arf-explained.md](./docs/arf-explained.md) → [ARF main Ch. 1–3](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | [eIDAS Reg. Art. 5–6](https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18), [CIR 2024/1183 Art. 9–13](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) |
| **Architect** | [reading-path-architect.md](./docs/reading-paths/reading-path-architect.md) | [architecture-layer-map.md](./docs/architecture-layer-map.md) → [ARF main Ch. 2–5](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | ARF Ch. 3 (Roles), Ch. 5 (Protocols), [Technical Specs](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/technical-specifications) |
| **Implementer** | [reading-path-implementer.md](./docs/reading-paths/reading-path-implementer.md) | [conformance-interpretation-companion.md](./docs/conformance-interpretation-companion.md) → [ARF main Ch. 5–6](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md), [OpenID Specs](https://openid.net/) | ARF Annex 2 (HLRs), [Technical Specs](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/technical-specifications), [CIR 2024/1183 Art. 1–8](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) |
| **Security / Assurance** | [reading-path-security-assurance.md](./docs/reading-paths/reading-path-security-assurance.md) | [governance-to-control-mapping.md](./docs/governance-to-control-mapping.md) → [ARF main Ch. 6](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | ARF Ch. 6 (Security), [CIR 2024/1183 Art. 9](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) (Conformance) |

---

**Last Updated:** March 23, 2026  
**ARF Alignment:** v2.8.0 (February 2, 2026)  
**Regulatory Basis:** eIDAS Regulation 2014/910/EU, CIR 2024/1183  
**On-Ramp Version:** 1.0.0
