# Quick Reference & Glossary

**Purpose:** Searchable reference for 100+ ARF terms, abbreviations, regulatory documents, standards, and external resources. All entries cite their authoritative source.

**How to Use:** Use Ctrl+F (Cmd+F) to search for terms. Each entry includes definition, ARF/regulatory reference, and external links where applicable.

---

## Essential Abbreviations & Terms

### Regulatory & Governance

| Term | Full Name | Definition | Source |
|------|-----------|-----------|--------|
| **ARF** | Architecture and Reference Framework | The technical blueprint for EU Digital Identity Wallets (v2.8.0 current) | [ARF GitHub](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) |
| **CIR** | Commission Implementing Regulation | Detailed implementing rules for the EU Digital Identity Regulation; current: 2024/1183 (Oct 18, 2024) | [CIR 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) |
| **EDICG** | European Digital Identity Cooperation Group | Multi-stakeholder EU governance body coordinating ARF and implementation | [EDICG Official](https://digital-strategy.ec.europa.eu/en/policies/european-digital-identity-cooperation-group) |
| **eIDAS** | Electronic Identification, Authentication and Trust Services Regulation | Base regulation 2014/910/EU (amended by Regulation 2024/1183); foundation for digital identity | [EUR-Lex eIDAS](https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18) |
| **EU DI Reg** | European Digital Identity Regulation | Regulation 2024/910/EU extending eIDAS scope to digital identity wallets (entering force Oct 18, 2025) | [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) |
| **DICG** | Digital Identity Cooperation Group | Alternative name for EDICG (same governance body) | [EDICG](https://digital-strategy.ec.europa.eu/en/policies/european-digital-identity-cooperation-group) |
| **QEAA** | Qualified Electronic Attestation of Attributes | Cryptographically signed attestation meeting high assurance (eIDAS definition, ARF 2.4.1) | ARF Ch. 1, eIDAS Art. 6 |
| **QC** | Qualified Certificate | Certificate for electronic signatures meeting eIDAS Annex I–II standards | eIDAS Regulation, Annex I–II |
| **QSCD** | Qualified Signature Creation Device | Secure device for qualified signature creation per eIDAS requirements | eIDAS Regulation, Art. 3(13) |
| **SCA** | Strong Customer Authentication | Multi-factor authentication for payment/sensitive transactions (PSD2 context) | [PSD2 Directive](https://eur-lex.europa.eu/eli/dir/2015/2366/oj), Art. 4(30) |

### Wallet Roles & Components

| Term | Definition | ARF Reference | External Reference |
|------|-----------|---|---|
| **Attestation Provider** | Entity issuing attestations (credentials, certificates); non-government entity (e.g., university, employer) | [ARF Ch. 3, Sec. 3.1](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | CIR 2024/1183 Art. 2(3) |
| **PID Provider** | Provider of Person Identification Data; government entity issuing foundational identity data | [ARF Ch. 3, Sec. 3.1](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | [CIR 2024/1183 Art. 2(5)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) |
| **Relying Party (RP)** | Service/website accepting wallet credentials for authentication or transaction | [ARF Ch. 3, Sec. 3.1](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | [CIR 2024/1183 Art. 2(7)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) |
| **Supervisory Body** | Government entity overseeing wallet certification, assurance levels, and compliance | [ARF Ch. 7](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | [CIR 2024/1183 Art. 9–13](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) |
| **Wallet Provider** | Commercial or public entity providing wallet software/infrastructure and support services | [ARF Ch. 3, Sec. 3.2](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | [CIR 2024/1183 Art. 2(1)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) |
| **Wallet Instance** | Single running instance of wallet software on a user's device (mobile, desktop, web) | [ARF Ch. 3, Sec. 3.3](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | [CIR 2024/1183 Art. 2(2)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) |
| **Wallet Solution** | Complete wallet offering bundling provider software, instances, support, governance, and lifecycle | [ARF Ch. 3, Sec. 3.1](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | [CIR 2024/1183 Recital 5](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) |
| **Wallet Unit** | Physical or virtual device component holding cryptographic keys and credentials (Secure Enclave, HSM, cloud vault) | [ARF Ch. 3, Sec. 3.4](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | ARF Topic P (Device Binding) |
| **RP Registrar** | Intermediary entity managing Relying Party registration with supervisory bodies for wallet acceptance | [ARF Ch. 4, Sec. 4.5](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | [CIR 2024/1183 Art. 2(9)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) |

### Protocol & Technical Terms

| Term | Definition | Standard/Reference | Link |
|------|-----------|---|---|
| **HAIP** | HTTP Authentication and Information Protocol | Custom ARF protocol for device-to-wallet interaction over HTTP/HTTPS | [ARF Tech Specs](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/technical-specifications) |
| **mDL** | Mobile Driver License | ISO/IEC 18013-5:2021 mobile credential format; model for wallet design | [ISO/IEC 18013-5:2021](https://www.iso.org/standard/69084.html) |
| **OpenID4VCI** | OpenID for Verifiable Credential Issuance | Protocol for issuing verifiable credentials; v1.0 final (2023) | [OpenID4VCI 1.0](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html) |
| **OpenID4VP** | OpenID for Verifiable Presentations | Protocol for presenting verifiable credentials; v1.0 final (2023) | [OpenID4VP 1.0](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) |
| **OID4VCI** | Abbreviated form of OpenID4VCI | Used interchangeably in technical specs and documentation | [OpenID4VCI](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html) |
| **OID4VP** | Abbreviated form of OpenID4VP | Used interchangeably in technical specs and documentation | [OpenID4VP](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) |
| **PID** | Person Identification Data | Government-issued foundational identity data (name, birth date, nationality, etc.) | [ARF Ch. 2](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md), [CIR 2024/1183 Annex I](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) |
| **RP** | Relying Party | Service accepting wallet credentials (web service, mobile app, etc.) | [ARF Ch. 3](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) |
| **SD-JWT** | Selective Disclosure JWT | JWT format enabling credential holders to selectively disclose claims | [RFC 9052](https://datatracker.ietf.org/doc/html/rfc9052) |
| **CWT** | CBOR Web Token | Compact binary token format (CBOR-based alternative to JWT) | [RFC 9052](https://datatracker.ietf.org/doc/html/rfc9052) |
| **CBOR** | Concise Binary Object Representation | Compact binary serialization format for tokens and data | [RFC 7049](https://datatracker.ietf.org/doc/html/rfc7049) |
| **WSCA** | Wallet Secure Crypto Architecture | Wallet's cryptographic subsystem design (vs. hardware WSCD) | [ARF Ch. 3, Sec. 3.4](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) |
| **WSCD** | Wallet Secure Crypto Device | Physical or virtual device component for cryptographic operations (Secure Enclave, HSM) | [ARF Ch. 3, Sec. 3.4](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) |
| **Keystore** | Storage for cryptographic keys | Distinguished from WSCA (architecture) and WSCD (device) in ARF v2.7.0+ | [ARF Ch. 3, Sec. 3.4](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) |

### Security & Assurance

| Term | Definition | ARF Reference | Regulatory Reference |
|------|-----------|---|---|
| **Assurance Level (AL)** | Graduated confidence in wallet security: L0 (baseline) → L3 (highest); formerly labeled AL1–AL4 | [ARF Ch. 6, Sec. 6.1](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | [CIR 2024/1183 Art. 9](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) |
| **Certificate Transparency** | Public, verifiable log of issued certificates for accountability and revocation tracking | [ARF Topic 55](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/discussion-topics) | RFC 6962 (CT for TLS), ARF Ch. 6 |
| **Conformance Profile** | Subset of ARF requirements applicable to specific role or use case (e.g., "RP conformance profile") | [ARF Annex 2](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/annexes) | [CIR 2024/1183 Art. 9](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) |
| **Device Binding** | Cryptographic link between wallet and physical device; recommended (not mandatory) as of ARF v2.6.0 | [ARF Topic P](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/discussion-topics), [ARF Ch. 3, Sec. 3.4](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | [ISO/IEC 18013-5:2021](https://www.iso.org/standard/69084.html) |
| **High-Level Requirements (HLRs)** | 55 top-level requirements in ARF Annex 2 organized by topic (identity, lifecycle, security, governance) | [ARF Annex 2](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/annexes) | [CIR 2024/1183 Annex II](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) |
| **Trust Boundary** | Security perimeter separating trusted wallet components from untrusted external systems | [ARF Ch. 2–5](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | ARF Ch. 6 (Security model) |
| **Threat Model** | Documented security threats, vulnerabilities, and mitigations applicable to wallet architecture | [ARF Ch. 6, Sec. 6.2](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | ISO/IEC 27005 (Risk management) |
| **Privacy by Design** | Integrating privacy requirements into all architectural and control layers from inception | [ARF Ch. 6, Sec. 6.4](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | [GDPR Art. 25](https://eur-lex.europa.eu/eli/reg/2016/679/oj) |
| **Accessibility** | Design ensuring wallet usability for all users including those with disabilities (WCAG 2.1 AA minimum) | [ARF Ch. 8](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | [WCAG 2.1](https://www.w3.org/WAI/WCAG21/quickref/), [EN 301 549](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf) |

### Data Flow Scenarios

| Flow | Description | ARF Reference | Use Case |
|------|-------------|---|---|
| **Proximity Flow** | Short-distance (NFC/Bluetooth) authentication between wallet device and RP | [ARF Ch. 4, Sec. 4.2](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | In-person transactions, physical access |
| **Remote Same-Device Flow** | Web/app authentication on same device (mobile or desktop) | [ARF Ch. 4, Sec. 4.3](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | Online services on phone; password manager pattern |
| **Remote Cross-Device Flow** | QR code–based authentication across devices (wallet on phone, RP on desktop/web) | [ARF Ch. 4, Sec. 4.4](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | Web authentication via mobile wallet |
| **Registration Flow** | Wallet and/or RP registration with supervisory bodies for conformance and operational recognition | [ARF Ch. 4, Sec. 4.5](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) | Onboarding, ecosystem participation |

---

## Key Regulatory Documents

### Primary Regulations

| Document | Link | Purpose | Key Articles |
|----------|------|---------|---|
| **eIDAS Regulation 2014/910/EU** (Current) | [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18) | Base legal framework for electronic identification and trust services; amended by Regulation 2024/1183 | Art. 1–8 (scope, definitions), Art. 5–6 (wallet), Art. 9–11 (trust services) |
| **Regulation (EU) 2024/1183** (Current CIR) | [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) | **Final** technical specifications and conformance rules for EU Digital Identity Wallets (effective Oct 18, 2025) | Art. 1–8 (technical specs), Art. 9–13 (conformance & certification), Annex I–III (data models, crypto, security) |
| **Regulation (EU) 2023/1411** (Pilot Phase) | [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2023/1411/oj) | Pilot phase specifications (superseded by CIR 2024/1183; kept for reference) | Art. 1–5 (pilot technical specs) |

### Supporting EU Legislation

| Document | Link | Relevance to Wallet |
|----------|------|---|
| **GDPR — Regulation (EU) 2016/679** | [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Data protection requirements; Art. 25 (privacy by design), Art. 32–34 (security obligations) |
| **Digital Services Act — Regulation (EU) 2022/868** | [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2022/868/oj) | Wallet Provider may fall under DSA scope as digital service provider; platform governance, liability |
| **PSD2 — Directive (EU) 2015/2366** | [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2015/2366/oj) | Strong Customer Authentication (SCA) standards; applicable if wallet integrates payment credentials |

---

## Technical & Standards References

### OpenID Foundation Protocols

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
