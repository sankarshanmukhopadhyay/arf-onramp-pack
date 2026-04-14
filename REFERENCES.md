# ARF On-Ramp Pack: Comprehensive References & Citations

**Document Status:** Complete reference guide for all citations, regulatory authorities, standards, and external resources referenced throughout the ARF On-Ramp Pack.

**Last Updated:** March 23, 2026  
**ARF Alignment:** v2.8.0 (February 2, 2026)  
**Regulatory Basis:** eIDAS Regulation together with the current implementing regulations referenced by the upstream ARF

---

## Table of Contents

1. [Regulatory Authorities & Legal Framework](#regulatory-authorities--legal-framework)
2. [Official ARF Documentation](#official-arf-documentation)
3. [Technical Standards & Specifications](#technical-standards--specifications)
4. [Governance & Cooperation](#governance--cooperation)
5. [Community & Resources](#community--resources)
6. [Citation Format Guide](#citation-format-guide)

---

## Regulatory Authorities & Legal Framework

### Primary Legislation

#### EU Digital Identity Regulation (eIDAS 2014/910/EU)
- **Official Title:** Regulation (EU) No 2014/910 of the European Parliament and of the Council on electronic identification and trust services for electronic transactions in the internal market
- **Current Version:** As amended by Regulation (EU) 2024/1183
- **EUR-Lex Citation:** https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18
- **Key Articles for Wallets:**
  - **Article 5 & 6:** EU Digital Identity Wallet definition and technical requirements
  - **Article 7:** Supervisory role of Member States
  - **Article 8:** Cross-border recognition
- **Entered into Force:** October 18, 2024
- **Effective Date:** October 18, 2025

#### Implementing Regulations Referenced by the Current Upstream ARF
- **Current upstream position:** The ARF repository now explicitly references a broader set of EUDI Wallet implementing regulations, including measures on PID/EAA, integrity and core functionalities, ecosystem notifications, certification of wallet solutions, protocols and interfaces, cross-border identity matching, security breaches, relying party registration, certified wallet lists, qualified trust service operations, supervisory reporting, and related procedures.
- **Authoritative source:** https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework
- **Practical guidance:** Use the upstream ARF README as the current regulatory index, then follow the linked Data.europa and EUR-Lex records for the exact legal text.
- **Historic note:** Earlier versions of this on-ramp pack centered CIR 2024/1183. That reference remains important historical context, but it is no longer sufficient as a complete description of the current upstream regulatory set.

### Regulatory Update Tracking

- **CIR Amendment Search:** https://eur-lex.europa.eu/search.html?queryText=2024/1183&type=reg
  - Regularly check EUR-Lex for amendments or corrigenda

### Related EU Legislation

- **Regulation (EU) 2016/679 (GDPR):** Data protection requirements
  - https://eur-lex.europa.eu/eli/reg/2016/679/oj
  - Key articles: 32–34 (security), 35 (DPIA), 32–39 (accountability)

- **Directive (EU) 2015/2366 (PSD2):** Payment Services Directive
  - https://eur-lex.europa.eu/eli/dir/2015/2366/oj
  - Relevant for payment-linked wallet scenarios

- **Regulation (EU) 2022/868 (Data Governance Act):** Data-sharing governance context
  - https://eur-lex.europa.eu/eli/reg/2022/868/oj
  - Tangential context only; not a primary wallet implementation authority

---

## Official ARF Documentation

## Synchronization Review Notes

- Repository references have been synchronized to the current upstream ARF repository name: `eudi-doc-architecture-and-reference-framework`.
- Technical specification references have been synchronized to the dedicated STS repository.
- Regulatory references have been reframed so this guide no longer implies that CIR 2024/1183 alone exhausts the current upstream legal and technical basis.

### ARF Main Repository & Releases

- **GitHub Repository:** https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework
  - **License:** CC BY 4.0
  - **Issues & Discussions:** https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/issues
  - **Release Notes:** https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/releases

### ARF Main Document (v2.8.0)

- **Document Title:** Architecture and Reference Framework — Version 2.8.0
- **Publication Date:** February 2, 2026
- **Full GitHub URL:** https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md
- **PDF Download:** Available in GitHub releases
- **Size:** ~389 KB (Markdown format)

#### ARF Chapter Structure

1. **Chapter 1: Introduction & Scope**
   - Purpose and regulatory mandate (eIDAS, CIR 2024/1183)
   - Stakeholder landscape

2. **Chapter 2: Overview & Architecture Principles**
   - Five-layer architecture (governance, trust, infrastructure, protocol, interop)
   - Trust model and assurance levels

3. **Chapter 3: Wallet Roles & Responsibilities**
   - Wallet Provider, Wallet Instance, Wallet Unit, Wallet Solution definitions
   - Role interactions and governance

4. **Chapter 4: Data Flows & Interactions**
   - Proximity flows (NFC, Bluetooth)
   - Remote flows (same-device, cross-device)
   - Registration and management flows

5. **Chapter 5: Technical Protocols & Bindings**
   - OpenID4VCI binding specifications
   - OpenID4VP binding specifications
   - HAIP (HTTP Authentication Interop Protocol) specifications
   - Data serialization (SD-JWT, CWT, JSON)

6. **Chapter 6: Security, Integrity & Accessibility**
   - Cryptographic requirements
   - Authentication and authorization controls
   - Audit and logging
   - Accessibility requirements (WCAG 2.1)
   - Privacy by design (GDPR alignment)

7. **Chapter 7: Governance & Conformance**
   - Wallet certification and assurance levels (AL1–AL4)
   - Member State roles and supervisory responsibility
   - Ecosystem governance models

8. **Chapter 8: Interoperability & Cross-Border**
   - Cross-border authentication flows
   - Trust registry and credential trust chains
   - Revocation and status management

### ARF Annexes

- **Annex 1: Acronyms & Definitions**
  - GitHub URL: https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/annexes
  - Comprehensive glossary (100+ terms)

- **Annex 2: High-Level Requirements (HLRs)**
  - **Total HLRs:** 55 mapped requirements
  - **Categories:** 
    - Identity Verification (HLRs 1–12)
    - Wallet Lifecycle (HLRs 13–22)
    - Credential Issuance (HLRs 23–33)
    - Credential Presentation (HLRs 34–40)
    - Security Controls (HLRs 41–50)
    - Governance & Compliance (HLRs 51–55)
  - **Traceability:** Each HLR mapped to ARF chapter, CIR article, and assurance level
  - **Available Formats:** CSV, Markdown, JSON Schema

- **Annex 3: ARF-to-CIR Mapping**
  - Cross-reference table: ARF sections → CIR 2024/1183 articles
  - Alignment with technical specifications

- **Annex 4: Member State Declarations & Governance**
  - Template for MS governance declarations
  - Assurance level declarations

### ARF Discussion Topics (Open Consultation)

- **GitHub Location:** https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/discussion-topics

#### Active Discussion Topics

| Topic | Subject | Status | URL |
|-------|---------|--------|-----|
| **F** | Trust Registry Query Protocol (TRQP) | Active | [GitHub](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/discussion-topics) |
| **P** | Device Binding & Hardware Security | Active | [GitHub](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/discussion-topics) |
| **Q** | Relying Party Federation Models | Active | [GitHub](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/discussion-topics) |
| **R** | Cross-Border Interoperability Enhancement | Active | [GitHub](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/discussion-topics) |
| **S** | Attestation Rulebook Extensibility | Active | [GitHub](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/discussion-topics) |
| **T, AA, etc.** | Emerging Requirements | In Preparation | [GitHub](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/discussion-topics) |

---

## Technical Standards & Specifications

### OpenID Foundation Standards

#### OpenID for Verifiable Credential Issuance (OpenID4VCI)

- **Specification Title:** OpenID for Verifiable Credential Issuance 1.0
- **Latest Version:** 1.0 (Final)
- **Official URL:** https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html
- **GitHub Repository:** https://github.com/openid/OpenID4VCI
- **Key Sections:**
  - Pre-authorized code flow (credential issuance without credential request)
  - Authorization code flow (credential issuance with user interaction)
  - Batch issuance support
  - JWT/CBOR credential serialization

#### OpenID for Verifiable Presentations (OpenID4VP)

- **Specification Title:** OpenID for Verifiable Presentations using Authorization Request Object 1.0
- **Latest Version:** 1.0 (Final)
- **Official URL:** https://openid.net/specs/openid-4-verifiable-presentations-1_0.html
- **GitHub Repository:** https://github.com/openid/OpenID4VP
- **Key Sections:**
  - Request object format for presentation requests
  - Authorization endpoint integration
  - Verifier-to-wallet protocol flows

#### OpenID Connect Core (OIDC)

- **Specification Title:** OpenID Connect Core 1.0
- **Official URL:** https://openid.net/specs/openid-connect-core-1_0.html
- **Relevant for:** Authentication flows, token handling, claim structure

### EU Digital Identity Wallet Technical Specifications

- **GitHub Location:** https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications
- **Contents:**
  - OpenID4VCI EU Wallet Profile
  - OpenID4VP EU Wallet Profile
  - SD-JWT serialization binding
  - CWT serialization binding
  - HAIP (HTTP Authentication Interop Protocol) specification

### Credential Data Format Standards

#### Selective Disclosure JWT (SD-JWT)

- **Specification Title:** SD-JWT family of specifications
- **Status:** Refer to the OpenID / IETF publication state for the exact current document status
- **Practical note:** Use upstream ARF and STS references to determine which SD-JWT profile is actually in scope for your implementation

#### CBOR Object Signing and Encryption (COSE)

- **Specification Title:** CBOR Object Signing and Encryption (COSE): Structures and Process
- **Status:** RFC 9052 & RFC 9053 (Internet Standards)
- **IETF RFC 9052:** https://datatracker.ietf.org/doc/html/rfc9052
- **IETF RFC 9053:** https://datatracker.ietf.org/doc/html/rfc9053
- **Key Use:** Compact credential serialization, mobile device optimization

#### CBOR (Concise Binary Object Representation)

- **Specification Title:** Concise Binary Object Representation (CBOR)
- **Status:** RFC 7049 (Internet Standard)
- **IETF RFC:** https://datatracker.ietf.org/doc/html/rfc7049
- **Key Use:** Compact binary serialization for wallets, credential encoding

#### JSON Web Token (JWT)

- **Specification Title:** JSON Web Token (JWT)
- **Status:** RFC 7519 (Internet Standard)
- **IETF RFC:** https://datatracker.ietf.org/doc/html/rfc7519
- **Key Use:** Wallet token exchange, credential presentation

### ISO/IEC Standards

#### ISO/IEC 18013-5:2021 (Mobile Driver's License - mDL)

- **Title:** Personal identification — mobile driving licence
- **Standard ID:** ISO/IEC 18013-5:2021
- **Scope:** Secure driving credential on mobile devices
- **Key Reference:** Mobile credential design patterns, device binding model
- **Availability:** ISO official standard (paid), summaries available on standards bodies

#### ISO/IEC 27001:2022 (Information Security Management)

- **Title:** Information security management systems
- **Standard ID:** ISO/IEC 27001:2022
- **Application:** Wallet provider organizational controls, certification scope
- **Related:** ISO/IEC 27002:2022 (implementation guidance)

#### ISO/IEC 27035:2023 (Incident Management)

- **Title:** Information security incident management
- **Standard ID:** ISO/IEC 27035:2023
- **Application:** Wallet security incident response requirements

### Cryptographic Standards

#### FIPS 140-3 (Federal Information Processing Standard)

- **Title:** Security Requirements for Cryptographic Modules
- **Standard ID:** FIPS PUB 140-3
- **Reference:** https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.140-3.pdf
- **Application:** Cryptographic algorithm security levels, hardware security module (HSM) validation

#### NIST SP 800-38D (Galois/Counter Mode - GCM)

- **Title:** Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode (GCM)
- **Standard ID:** NIST Special Publication 800-38D
- **Reference:** https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf
- **Application:** AEAD encryption in wallet protocols

#### RFC 3394 (AES Key Wrap)

- **Title:** Advanced Encryption Standard (AES) Key Wrap Algorithm
- **Status:** RFC 3394 (Informational)
- **IETF RFC:** https://datatracker.ietf.org/doc/html/rfc3394
- **Application:** Key management, secure key exchange

#### RFC 5869 (HKDF - HMAC-based Extract-and-Expand Key Derivation Function)

- **Title:** HMAC-based Extract-and-Expand Key Derivation Function (HKDF)
- **Status:** RFC 5869 (Informational)
- **IETF RFC:** https://datatracker.ietf.org/doc/html/rfc5869
- **Application:** Key derivation in wallet cryptographic operations

#### RFC 8174 (Ambiguity of Uppercase vs. Lowercase)

- **Title:** Ambiguity of Uppercase vs. Lowercase in RFC 2119 Key Words
- **Status:** RFC 8174 (Best Current Practice)
- **IETF RFC:** https://datatracker.ietf.org/doc/html/rfc8174
- **Reference:** Combined with RFC 2119 for normative language interpretation in ARF and specifications

### Accessibility Standards

#### WCAG 2.1 (Web Content Accessibility Guidelines)

- **Official Title:** Web Content Accessibility Guidelines (WCAG) 2.1
- **Latest Version:** 2.1 (W3C Recommendation)
- **Publication Date:** June 5, 2018
- **W3C URL:** https://www.w3.org/WAI/WCAG21/quickref/
- **Key Principles:** Perceivable, Operable, Understandable, Robust (POUR)
- **Levels:** A, AA, AAA (ARF recommends AA minimum)
- **Reference:** ARF Chapter 8 (Accessibility requirements)

#### EN 301 549 V3.2.1 (European Accessibility Standard)

- **Title:** Accessibility requirements for ICT products and services
- **Standard ID:** EN 301 549 V3.2.1
- **ETSI Reference:** https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf
- **Key Scope:** EU digital accessibility requirements (aligned with WCAG 2.1)
- **Mandatory Compliance:** EU public institutions and contractors

#### ISO/IEC 40500:2012 (WCAG 2.0 as ISO Standard)

- **Title:** Information technology — W3C Web Content Accessibility Guidelines (WCAG) 2.0
- **Standard ID:** ISO/IEC 40500:2012
- **Note:** WCAG 2.1 supersedes this (ISO/IEC 40500:2021 in progress)

---

## Governance & Cooperation

### European Digital Identity Cooperation Group (EDICG)

- **Official Name:** European Digital Identity Cooperation Group
- **Established By:** eIDAS Regulation 2014/910/EU, Article 10
- **Official Website:** https://digital-strategy.ec.europa.eu/en/policies/european-digital-identity-cooperation-group
- **Key Functions:**
  - Multi-stakeholder governance
  - Technical working groups
  - Public consultation on discussion topics
  - Interoperability decisions
- **Participation:** Member States, EU institutions, industry, civil society

### EU Digital Identity Policy Hub

- **Official Portal:** https://ec.europa.eu/digital-building-blocks/sites/spaces/EUDIGITALIDENTITYWALLET/
- **Contents:**
  - Implementation guidance
  - Pilot phase results
  - Community resources
  - News and updates

### Digital Europe Programme (DIGITAL)

- **Program Overview:** https://digital-strategy.ec.europa.eu/en/funding/digital-europe-programme
- **Relevant for:** Co-financing EU wallet implementation projects
- **Budget:** €7.6 billion (2021–2027)

---

## Community & Resources

### Official Implementation Resources

#### EU Blockchain Observatory & Forum

- **Website:** https://www.eublockchainforum.eu/
- **Relevance:** Distributed identity, credential exchange models

#### ENISA (European Union Agency for Cybersecurity)

- **Website:** https://www.enisa.europa.eu/
- **Relevant Publications:**
  - Digital Identity Guidelines
  - Threat Landscape & Analysis
  - Mobile Security Recommendations

### Related Standards Bodies

#### W3C (World Wide Web Consortium)

- **Website:** https://www.w3.org/
- **Relevant Working Groups:**
  - **Verifiable Credentials Data Model Working Group:** https://www.w3.org/2017/vc/WG/
  - **Web Authentication Working Group:** https://www.w3.org/Webauthn/

#### IETF (Internet Engineering Task Force)

- **Website:** https://www.ietf.org/
- **Relevant Working Groups:**
  - **OAuth Working Group:** https://datatracker.ietf.org/wg/oauth/about/
  - **JSON Object Signing and Encryption (JOSE):** https://datatracker.ietf.org/wg/jose/about/

#### ETSI (European Telecommunications Standards Institute)

- **Website:** https://www.etsi.org/
- **Relevant Standards:**
  - EN 301 549 (Accessibility)
  - ETSI eIDAS technical standards
  - TS 119 612 (Trust Service Status List — TSL)

#### ISO/IEC

- **Website:** https://www.iso.org/
- **Relevant Technical Committees:**
  - **ISO/IEC JTC 1/SC 27:** Information security, cybersecurity and privacy protection
  - **ISO/IEC JTC 1/SC 37:** Biometrics

### Related Initiatives & Ecosystems

#### DVLA (Digital Verifiable Legal Agreements)

- **Relevance:** Credential issuance patterns, trust frameworks

#### OpenID Foundation

- **Website:** https://openid.net/
- **Key Contributions:**
  - OpenID4VCI (credential issuance protocol)
  - OpenID4VP (credential presentation protocol)
  - OpenID Connect (authentication protocol)

#### Decentralized Identity (DIF) Foundation

- **Website:** https://identity.foundation/
- **Relevant Work Streams:**
  - Verifiable Credentials
  - Identity Hubs
  - Sidetree (DID scalability)

---

## Citation Format Guide

### How to Cite ARF Documents

#### Citing ARF Main Document

```
Architecture and Reference Framework v2.8.0. 
EU Digital Identity Wallet Project. 
February 2, 2026. 
https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md
```

**In-text example:**
"As specified in ARF Chapter 6 (Security, Integrity, and Accessibility), wallets MUST implement..."

#### Citing ARF Annex

```
Architecture and Reference Framework v2.8.0, Annex 2: High-Level Requirements.
EU Digital Identity Wallet Project.
https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/annexes
```

#### Citing CIR 2024/1183

```
Commission Implementing Regulation (EU) 2024/1183 of 10 October 2024 
establishing the technical specifications and procedures for EU digital identity wallets.
Official Journal L, 2024-10-11, volume 436, pages 1–67.
https://eur-lex.europa.eu/eli/reg/2024/1183/oj
```

**In-text example:**
"Under CIR 2024/1183 Article 9, wallet implementations MUST conform to the following security controls..."

#### Citing eIDAS Regulation

```
Regulation (EU) No 2014/910 of the European Parliament and of the Council 
on electronic identification and trust services for electronic transactions in the internal market.
As amended by Regulation (EU) 2024/1183.
https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18
```

#### Citing OpenID Specifications

```
OpenID for Verifiable Credential Issuance 1.0. OpenID Foundation. 2023.
https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html
```

#### Citing ISO/IEC Standards

```
ISO/IEC 18013-5:2021. Personal identification — mobile driving licence. 
International Organization for Standardization. 2021.
```

#### Citing IETF RFC

```
IETF RFC 9052: CBOR Object Signing and Encryption (COSE): Structures and Process.
Internet Engineering Task Force. August 2022.
https://datatracker.ietf.org/doc/html/rfc9052
```

#### Citing W3C Standards

```
Web Content Accessibility Guidelines (WCAG) 2.1. W3C Recommendation. 
June 5, 2018.
https://www.w3.org/WAI/WCAG21/quickref/
```

### URN/DOI Format

Many official documents have persistent identifiers:

- **EUR-Lex URN:** `urn:lex:eu:2024:reg:1183`
- **W3C DOI:** Available in W3C Shepherd for published recommendations

---

## Version History & Updates

| Date | Change | Reference |
|------|--------|-----------|
| 2026-02-02 | ARF v2.8.0 released | GitHub releases |
| 2024-10-18 | CIR 2024/1183 entered into force | EUR-Lex |
| 2024-10-11 | CIR 2024/1183 published in OJ | EUR-Lex |
| 2023-08-08 | CIR 2023/1411 published (pilot phase) | EUR-Lex |
| 2024-10-18 | eIDAS Reg. amended by Regulation 2024/1183 | EUR-Lex |

---

## How to Keep This Reference Current

1. **Monitor EUR-Lex** for amendments to CIR 2024/1183: https://eur-lex.europa.eu/search.html?queryText=2024/1183&type=reg
2. **Check ARF GitHub** for version updates and new discussion topics: https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework
3. **Subscribe to EDICG updates** for governance changes: https://digital-strategy.ec.europa.eu/en/policies/european-digital-identity-cooperation-group
4. **Follow OpenID Foundation** for protocol specification updates: https://openid.net/

---

## Contributing to This Reference

Found a broken link, outdated citation, or missing resource? Please:

1. Open a GitHub issue in this repository with details
2. Include the current date, the broken/incorrect reference, and the correct information
3. We will update within one month and credit your contribution in the CHANGELOG

---

**Compiled:** March 23, 2026  
**Next Review:** June 23, 2026 (quarterly)  
**Maintainer:** ARF On-Ramp Pack Community
