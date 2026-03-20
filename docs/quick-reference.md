# Quick Reference & Glossary

## Essential Abbreviations & Terms

### Regulatory & Governance

| Term | Full Name | Definition |
|------|-----------|-----------|
| **ARF** | Architecture and Reference Framework | The technical blueprint for EU Digital Identity Wallets |
| **CIR** | Commission Implementing Regulation | Detailed implementing rules for the EU Digital Identity Regulation |
| **EDICG** | European Digital Identity Cooperation Group | The EU group coordinating ARF and toolbox development |
| **eIDAS** | Electronic Identification, Authentication and Trust Services Regulation | 2014/910/EU; predecessor framework |
| **EU DI Reg** | European Digital Identity Regulation | 2024/910/EU; extends eIDAS to digital identity wallets |
| **QEAA** | Qualified Electronic Attestation of Attributes | Cryptographically signed attestation of attributes |
| **QC** | Qualified Certificate | Certificate for electronic signatures meeting high assurance standards |
| **QSCD** | Qualified Signature Creation Device | Secure device for creating qualified signatures |
| **SCA** | Strong Customer Authentication | Enhanced authentication for payment/sensitive transactions |

### Wallet Roles & Components

| Term | Definition | ARF Reference |
|------|-----------|---|
| **Attestation Provider** | Entity issuing attestations (e.g., credentials, certificates) | ARF Section 2.2 |
| **PID Provider** | Provider of Person Identification Data (government entity) | ARF Section 2.2 |
| **Relying Party (RP)** | Service that accepts wallet credentials for authentication | ARF Section 2.2, Chapter 4.5 |
| **Supervisory Body** | Government entity overseeing wallet certification & compliance | ARF Chapter 7 |
| **Wallet Provider** | Entity providing wallet infrastructure & services | ARF Section 3.2 |
| **Wallet Instance** | Single running instance of wallet software on a device | ARF Section 3.3 |
| **Wallet Solution** | Complete wallet offering (provider + instances + support) | ARF Section 3.1 |
| **Wallet Unit** | Physical device component holding credentials | ARF Section 3.4 |
| **RP Registrar** | Intermediary managing RP registration with supervisory bodies | ARF Section 4.5 |

### Protocol & Technical Terms

| Term | Definition | Standard |
|------|-----------|----------|
| **HAIP** | HTTP Authentication and Information Protocol | ARF custom protocol for device interaction |
| **mDL** | Mobile Driver License | ISO/IEC 18013-5 mobile credential format |
| **OpenID4VCI** | OpenID for Verifiable Credential Issuance | https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html |
| **OpenID4VP** | OpenID for Verifiable Presentations | https://openid.net/specs/openid-4-verifiable-presentations-1_0.html |
| **OID4VCI** | Abbreviated form of OpenID4VCI | |
| **OID4VP** | Abbreviated form of OpenID4VP | |
| **PID** | Person Identification Data | Government-issued fundamental identity data |
| **RP** | Relying Party | Service accepting wallet credentials |
| **WSCA** | Wallet Secure Crypto Architecture | Wallet's cryptographic subsystem |
| **WSCD** | Wallet Secure Crypto Device | Physical/virtual device component for crypto |
| **Keystore** | Storage for cryptographic keys | Distinguished from WSCA/WSCD in ARF 2.7.0+ |

### Security & Assurance

| Term | Definition | ARF Reference |
|------|-----------|---|
| **Assurance Level** | Graduated confidence in wallet security (L0–L3) | ARF Section 6 |
| **Certificate Transparency** | Public log of issued certificates (Topic 55, ARF 2.8.0) | ARF Topic 55 |
| **Conformance Profile** | Subset of ARF requirements applicable to specific role | ARF Annex 2, Topic 1–55 |
| **Device Binding** | Cryptographic link between wallet and device | ARF 2.6.0+: recommended (was mandatory) |
| **High-Level Requirements (HLRs)** | Top-level requirements in Annex 2 organized by topic | ARF Annex 2 |
| **Trust Boundary** | Security perimeter between system components | ARF Sections 2–5 |
| **Threat Model** | Documented security threats and mitigations | ARF Chapter 6 |

### Data Flow Scenarios

| Flow | Description | ARF Reference |
|------|-------------|---|
| **Proximity Flow** | Short-distance (NFC/BLE) authentication | ARF Section 5.1 |
| **Remote Same-Device Flow** | Web/app authentication on same device | ARF Section 5.2 |
| **Remote Cross-Device Flow** | QR code–based authentication across devices | ARF Section 5.3 |
| **Registration Flow** | Wallet/RP registration with supervisory bodies | ARF Section 5.4 |

---

## Key Regulatory Documents

### Primary Regulations

| Document | Link | Purpose |
|----------|------|---------|
| **EU Digital Identity Regulation 2024/910** | https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18 | Master legal framework for EUDI wallets |
| **eIDAS Regulation 2014/910** | https://eur-lex.europa.eu/eli/reg/2014/910/2024-01-01 | Original framework (predecessor) |

### Commission Implementing Regulations (Core)

| CIR | Topic | Link | Applicability |
|-----|-------|------|---|
| **CIR 2024/2977** | PID and EAA | https://data.europa.eu/eli/reg_impl/2024/2977/oj | Core: Attestation formats |
| **CIR 2024/2979** | Integrity and core functionalities | https://data.europa.eu/eli/reg_impl/2024/2979/oj | Core: Wallet requirements |
| **CIR 2024/2980** | Ecosystem notifications | https://data.europa.eu/eli/reg_impl/2024/2980/oj | Core: Notification protocols |
| **CIR 2024/2981** | Certification of Wallet Solutions | https://data.europa.eu/eli/reg_impl/2024/2981/oj | Core: Conformance criteria |
| **CIR 2024/2982** | Protocols and interfaces | https://data.europa.eu/eli/reg_impl/2024/2982/oj | Core: Technical standards |

### Commission Implementing Regulations (Extended)

| CIR | Topic | Link | Applicability |
|-----|-------|------|---|
| **CIR 2025/846** | Cross-border identity matching | https://data.europa.eu/eli/reg_impl/2025/846/oj | Identity interop |
| **CIR 2025/847** | Security breaches | https://data.europa.eu/eli/reg_impl/2025/847/oj | Incident response |
| **CIR 2025/848** | RP registration | https://data.europa.eu/eli/reg_impl/2025/848/oj | RP governance |
| **CIR 2025/849** | Certified Wallet list | https://data.europa.eu/eli/reg_impl/2025/849/oj | Wallet certification |
| **CIR 2025/1566** | QC/QEAA identity verification | https://data.europa.eu/eli/reg_impl/2025/1566/oj | Attestation verification |
| **CIR 2025/1567** | Remote QSCD management | https://data.europa.eu/eli/reg_impl/2025/1567/oj | Signature services |
| **CIR 2025/1568** | eID scheme peer reviews | https://data.europa.eu/eli/reg_impl/2025/1568/oj | Assurance |
| **CIR 2025/1569** | QEAA/EAA from public bodies | https://data.europa.eu/eli/reg_impl/2025/1569/oj | Authentic sources |
| **CIR 2025/1570** | QSCD notification | https://data.europa.eu/eli/reg_impl/2025/1570/oj | Signature devices |
| **CIR 2025/1571** | Supervisory body reports | https://data.europa.eu/eli/reg_impl/2025/1571/oj | Governance reporting |
| **CIR 2025/1572** | Qualified trust service notification | https://data.europa.eu/eli/reg_impl/2025/1572/oj | Trust service governance |

For a complete list, see the [ARF README](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/README.md).

---

## Essential Standards & Specifications

### EUDI-Specific Standards

| Standard | Link | Purpose |
|----------|------|---------|
| **OpenID4VCI** | https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html | Credential issuance protocol |
| **OpenID4VP** | https://openid.net/specs/openid-4-verifiable-presentations-1_0.html | Credential presentation protocol |
| **ISO/IEC 18013-5** | Mobile Driver License (mDL) | Cryptographic credential format |

### ISO/IEC Standards (Digital Signatures & Trust)

| Standard | Purpose |
|----------|---------|
| **ISO/IEC 27001** | Information security management |
| **ISO/IEC 27002** | Security controls catalog |
| **ISO/IEC 14888** | Digital signatures |
| **ISO/IEC 9796** | Signature schemes |

### IETF Standards (Cryptography & Protocols)

| Standard | Purpose |
|----------|---------|
| **RFC 3394** | Key wrap algorithm |
| **RFC 3610** | AES-CCM AEAD |
| **RFC 5116** | Cryptographic algorithm interface |
| **RFC 8174** | Keyword usage (SHALL, SHOULD, etc.) |

---

## Official Resources & Community

### European Commission

| Resource | Link | Purpose |
|----------|------|---------|
| **EUDI Wallet Home** | https://ec.europa.eu/digital-building-blocks/sites/spaces/EUDIGITALIDENTITYWALLET/ | Official portal |
| **EDICG Page** | https://digital-strategy.ec.europa.eu/en/policies/european-digital-identity-cooperation-group | Governance body info |
| **Digital Strategy** | https://digital-strategy.ec.europa.eu/ | Broader EU digital initiatives |
| **Commission Contact** | https://commission.europa.eu/about-european-commission/contact_en | Get in touch |

### GitHub Repositories

| Repository | Link | Purpose |
|-----------|------|---------|
| **ARF (Main)** | https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework | The authoritative ARF |
| **Attestation Rulebooks** | https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog | PID, mDL, and custom rulebooks |
| **Implementation Samples** | https://github.com/orgs/eu-digital-identity-wallet/repositories | Sample implementations (if available) |

### Consultation & Discussion

| Channel | Purpose |
|---------|---------|
| **GitHub Issues (ARF)** | Report bugs, suggest improvements |
| **GitHub Discussions (ARF)** | Ask questions, discuss topics |
| **EDICG Meetings** | Official policy discussions (quarterly) |

---

## Common Regulatory Concepts

### Conformance Levels

The ARF defines assurance levels for different deployment scenarios:

| Level | Confidence | Use Case |
|-------|-----------|----------|
| **L0** | Low | Non-critical services; basic authentication |
| **L1** | Medium | Standard public services |
| **L2** | High | Sensitive public/private services |
| **L3** | Very High | Regulatory/legal services; high-value transactions |

See ARF Chapter 6 for detailed security requirements per level.

### Topics in Annex 2

ARF Annex 2 organizes high-level requirements by topic (1–55). Key topics include:

| Topics | Area |
|--------|------|
| **1–5** | Governance & roles |
| **6–20** | Wallet architecture & data flows |
| **21–35** | Protocols & interoperability |
| **36–45** | Security & privacy |
| **46–50** | Attestation formats |
| **51–55** | Assurance & certification |

See [conformance-interpretation-companion.md](./conformance-interpretation-companion.md) for how to map these to implementation.

### Certification Pathways

ARF supports certification at multiple levels:

- **Wallet Solution Certification** — Full wallet product certification (CIR 2024/2981)
- **Component Certification** — Individual component (WSCA, attestation format) certification
- **Member State Notification** — National wallet scheme notification

See ARF Chapter 7 for governance details.

---

## Implementation Quick Links

### By Role

| Role | Key Resources |
|------|---|
| **Policy / Program Lead** | [EU DI Regulation](https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18), [EDICG Page](https://digital-strategy.ec.europa.eu/en/policies/european-digital-identity-cooperation-group), [ARF Overview](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/index.md) |
| **Architect** | [ARF Main Document](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md), [Annexes](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/annexes), [Technical Specs](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/technical-specifications) |
| **Implementer** | [OpenID4VCI](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html), [OpenID4VP](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html), [Technical Specs](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/technical-specifications) |
| **Security / Assurance** | [ARF Chapter 6](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md), [CIR 2024/2981](https://data.europa.eu/eli/reg_impl/2024/2981/oj), [Threat Models](./governance-to-control-mapping.md) |

### By Scenario

| Scenario | Recommended Reading |
|----------|---|
| **Implementing a Wallet Provider** | ARF Ch. 3, 6 + [reading-path-architect.md](./reading-paths/reading-path-architect.md) |
| **Implementing a Relying Party** | ARF Ch. 4.5, 5 + CIR 2025/848 |
| **Issuing Attestations** | ARF Ch. 4.2, Annex 3 + [Rulebooks](https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog) |
| **Certification / Audit** | ARF Ch. 7 + CIR 2024/2981 + [reading-path-security-assurance.md](./reading-paths/reading-path-security-assurance.md) |

---

## Frequently Used Links

Keep these bookmarked:

### Upstream ARF
- **Repository:** https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework
- **Main Document:** https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md
- **Releases:** https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/releases
- **CHANGELOG:** https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/CHANGELOG.md

### Regulations
- **EU Digital Identity Regulation:** https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18
- **CIR List:** https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/README.md

### Standards
- **OpenID4VCI:** https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html
- **OpenID4VP:** https://openid.net/specs/openid-4-verifiable-presentations-1_0.html

### Community
- **EDICG:** https://digital-strategy.ec.europa.eu/en/policies/european-digital-identity-cooperation-group
- **EUDI Home:** https://ec.europa.eu/digital-building-blocks/sites/spaces/EUDIGITALIDENTITYWALLET/

---

## When You Don't Know Something

**If you need to find...**

| What | Where |
|------|-------|
| A regulatory requirement | [EU Digital Identity Regulation](https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18) + relevant CIR |
| Architecture guidance | [ARF Main Document](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) |
| A protocol standard | [Technical Specs](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/technical-specifications) |
| An acronym or term | [ARF Annex 1 (Glossary)](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/annexes) or this document |
| Implementation examples | [Rulebooks](https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog) |
| Who does what | [ARF Section 2 (Roles & Responsibilities)](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) |
| Conformance criteria | [ARF Annex 2 (High-Level Requirements)](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/annexes) |
| Data flows | [ARF Chapter 5](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) |
| Security controls | [ARF Chapter 6](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) |

---

## Version History of This Document

| Version | Date | Changes |
|---------|------|---------|
| **1.0** | 2026-03 | Initial release; aligned with ARF 2.8.0 |

---

**Last Updated:** March 2026  
**ARF Alignment:** 2.8.0 (2026-02-02)
