# Reading Path: Architect & System Designer

**For:** Enterprise architects, solution architects, technical leads, senior developers  
**Focus:** System architecture, design patterns, reference architecture, design trade-offs, security architecture  
**Time:** 45–60 minutes to read; 3–4 hours with ARF deep-dive and design exercises  
**Outcome:** Understand wallet architecture, design your system, identify integration points, plan security controls

---

## Before You Start

**You should know:**
- System design and architecture principles
- Cryptography basics (signatures, key management, encryption)
- Identity and authentication concepts
- Your wallet type (government, private sector, hybrid)

**You might skip if:**
- You're a developer needing to implement protocols (see [Implementer path](./reading-path-implementer.md))
- You need detailed security threat modeling (see [Security/Assurance path](./reading-path-security-assurance.md))

---

## Key Concepts for Architects

### 1. Layered Architecture

The ARF is organized in five logical layers (see [Architecture Layer Map](../architecture-layer-map.md)):

```
Layer 1: Governance (policies, certification)
Layer 2: Trust (cryptography, identity binding)
Layer 3: Infrastructure (wallet components, storage)
Layer 4: Protocol (OpenID4VCI, OpenID4VP, data flows)
Layer 5: Interop (standards, formats, cross-border)
```

**Your job:** Map these layers to your system architecture.

### 2. Wallet Architecture

A wallet consists of four structural components:

```
Wallet Solution (complete product)
  ├─ Wallet Provider (backend services)
  ├─ Wallet Instance (running app/service on device)
  └─ Wallet Unit (secure storage of keys & credentials)
```

**Your job:** Design how these interact in your system.

### 3. Data Flows

Three main scenarios drive architecture design:

- **Issuance:** Government → Wallet (credential acquisition)
- **Presentation:** Wallet → Service (credential sharing for authentication)
- **Registration:** Device ↔ Provider, Service ↔ Supervisory Body (setup/governance)

**Your job:** Design system behavior for each flow.

### 4. Trust Model

Credentials are signed by issuers. Users validate signatures using public keys from trust lists.

```
Issuer (has private key) → Signs credential → Wallet receives
Wallet (has public key) → Verifies signature → Service validates
```

**Your job:** Design trust anchor management and validation.

### 5. Device Binding (Optional but Recommended)

Wallet can cryptographically bind credentials to the physical device, preventing use on other devices.

```
Device generates key → Credential embeds device public key
→ Device private key required to use credential
→ Different device can't use the credential
```

**Your job:** Decide if device binding is in scope; if so, design integration with secure hardware.

---

## Recommended Reading Order

### Section 1: ARF Architecture Overview (15 min)

**Read:** [ARF Explained](../arf-explained.md) → "Structural Overview: The Five Layers" section

**Then:** [Architecture Layer Map](../architecture-layer-map.md) → Full document

**Then:** [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → **Chapter 3** (Wallet Architecture & Components)

**Key Questions to Answer:**
- [ ] What are the five architecture layers?
- [ ] What is the difference between Wallet Solution, Provider, Instance, and Unit?
- [ ] Which layer does your system sit in?

---

### Section 2: Wallet Interior Architecture (15 min)

**Read:** [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → **Chapter 4, Sections 4.1–4.3** (Ecosystem, Trust, Wallet Lifecycle)

**Then:** Revisit [Architecture Layer Map](../architecture-layer-map.md) → "Architecture Patterns" section

**Key Questions to Answer:**
- [ ] How does a wallet provision itself with credentials?
- [ ] How are private keys stored and protected?
- [ ] What does device binding look like architecturally?
- [ ] How does the wallet lifecycle work (provision → use → revoke → deactivate)?

---

### Section 3: Data Flows & Integration Points (15 min)

**Read:** [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → **Chapter 5** (Data Flows)

**Focus on:**
- Section 5.1: Proximity authentication (NFC) flow
- Section 5.2: Remote authentication (web/app) flows
- Section 5.3: Cross-device authentication (QR code) flow
- Section 5.4: Registration flows

**Key Questions to Answer:**
- [ ] What are the three main data flows?
- [ ] How does the wallet interact with services in each flow?
- [ ] Where are the integration points in your system?

---

### Section 4: Security Architecture (10 min)

**Read:** [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → **Chapter 6** (Security, Integrity, Accessibility)

**Then:** [Governance to Control Mapping](../governance-to-control-mapping.md) → Sections on cryptographic and security controls

**Key Questions to Answer:**
- [ ] What are the assurance levels (L0–L3) and what security controls does each require?
- [ ] What threat model applies to your wallet?
- [ ] What cryptographic algorithms and key lengths are mandated?

---

### Section 5: Accessibility & Design for All (5 min)

**Read:** [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → **Chapter 8** (Accessibility)

**Also:** [Governance to Control Mapping](../governance-to-control-mapping.md) → "User Consent Controls" pattern

**Key Questions to Answer:**
- [ ] What WCAG 2.1 compliance level is required?
- [ ] How does accessibility affect your UI design?

---

## Deep-Dive Topics (Optional)

### If You're Designing Wallet Provider Backend

**Additional Reading:**
1. [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → Chapter 4, Sections 4.1 (Ecosystem), 4.4 (Wallet Lifecycle)
2. [Conformance Interpretation Companion](../conformance-interpretation-companion.md) → "Requirement Categories by Topic" → Governance Topics (1–10)
3. [CIR 2024/2980](https://data.europa.eu/eli/reg_impl/2024/2980/oj) → Ecosystem notifications

**Questions to Explore:**
- How will you register with the member state?
- How will you notify supervisory bodies of events?
- What audit logging must you maintain?
- How will you handle wallet recovery/backup?
- What SLAs will you commit to?

### If You're Designing Mobile/Web Wallet Instance

**Additional Reading:**
1. [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → Chapter 3 (Wallet Architecture), Chapter 5 (Data Flows)
2. [Quick Reference](../quick-reference.md) → OpenID4VCI, OpenID4VP, HAIP protocol links
3. Platform security guides (iOS Secure Enclave, Android TEE, web crypto APIs)

**Questions to Explore:**
- Native app vs. web wallet—what are trade-offs?
- How do you store keys securely (Secure Enclave vs. cloud)?
- How do you implement biometric/PIN authentication?
- How do you handle QR code scanning and device approval UI?

### If You're Designing Issuer Integration

**Additional Reading:**
1. [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → Chapter 4, Section 4.2 (Attestation & Issuance)
2. [Attestation Rulebooks](https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog) → PID rulebook, any other rulebooks you support
3. [OpenID4VCI Spec](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html) (technical, for developers)

**Questions to Explore:**
- How will you federate with multiple issuers?
- How will you validate issuer certificates?
- How will you handle different credential formats (PID, mDL, custom)?
- How will you manage issuer metadata and discovery?

### If You're Designing Service Integration

**Additional Reading:**
1. [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → Chapter 4, Section 4.5 (Relying Parties)
2. [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → Chapter 5, Sections 5.2–5.3 (Remote flows)
3. [OpenID4VP Spec](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) (technical)
4. [CIR 2025/848](https://data.europa.eu/eli/reg_impl/2025/848/oj) → RP registration

**Questions to Explore:**
- How will you integrate with services (web, mobile, kiosk)?
- How will you create credential requests?
- How will you register with supervisory bodies?
- How will you verify received credentials?

---

## Architecture Design Exercises

### Exercise 1: Map Your System to ARF Layers

**Objective:** Identify which ARF layers your architecture touches.

**Steps:**

1. Draw your system architecture diagram
2. Overlay the [five ARF layers](../architecture-layer-map.md)
3. Identify which components map to which layers

**Example:** Government Wallet Provider
```
Government Ministry (Issuer) ← Layer 2 (Trust)
  ↓
Wallet Provider Backend ← Layer 3 (Infrastructure) + Layer 1 (Governance)
  ↓
Wallet App on Phone ← Layer 3 (Infrastructure)
  ↓
OpenID4VP API ← Layer 4 (Protocol)
  ↓
Service Integration ← Layer 5 (Interop)
```

**Output:** Layer mapping document

---

### Exercise 2: Design Data Flow for Each Scenario

**Objective:** Map ARF data flows to your system design.

**Steps:**

1. Pick a data flow scenario (issuance, presentation, registration)
2. Draw sequence diagram for your system
3. Label each component and protocol/API call
4. Identify trust boundaries

**Example:** Credential Presentation Flow

```
User phone (Wallet Instance)
  ↓ User clicks "Use digital ID"
Service website
  ↓ Generates OpenID4VP request
Wallet app
  ↓ Shows approval UI + device unlock
User approves + authenticates
  ↓ Wallet calls device API for signature
Device secure enclave (Wallet Unit)
  ↓ Signs with private key
Wallet app
  ↓ Sends signed response to service
Service backend
  ↓ Verifies signature using issuer public key from trust list
Service backend grants access
```

**Output:** Sequence diagrams for each flow

---

### Exercise 3: Identify Cryptographic Components

**Objective:** Plan cryptographic architecture.

**Checklist:**
- [ ] Where are private keys generated? (Device, cloud, hardware module?)
- [ ] Where are private keys stored? (Secure Enclave, encrypted database, HSM?)
- [ ] Which operations use private keys? (Signing credentials, proving ownership, authentication)
- [ ] How are public keys distributed? (Trust lists, certificates, metadata)
- [ ] What algorithms and key lengths? (RS256, ECDSA, SHA-256)

**Output:** Cryptographic architecture document

---

### Exercise 4: Design Security Controls

**Objective:** Map ARF security requirements to your architecture.

**Steps:**

1. Determine target assurance level (L0–L3)
2. List required security controls for that level (see [Governance to Control Mapping](../governance-to-control-mapping.md))
3. Map each control to your architecture
4. Identify gaps

**Example:** Device Binding Control (L2+)

```
ARF Requirement: "Wallet SHOULD bind credential to device"

Your Architecture:
  ├─ Design: Generate unique key pair on device during provisioning
  ├─ Storage: Store private key in Secure Enclave
  ├─ Usage: Require device private key signature in credential presentation
  ├─ Verification: Service verifies device public key in credential
  └─ Evidence: Architecture doc, security tests, threat model
```

**Output:** Security controls matrix

---

## Common Architectural Questions

### Q1: "Should our wallet be cloud-based or on-device?"

**Trade-offs:**

| Aspect | On-Device | Cloud |
|--------|-----------|-------|
| Security | ✅ Keys never leave device | ⚠️ Keys in cloud; must be encrypted |
| UX | ⚠️ Can be cumbersome | ✅ Seamless across devices |
| Recovery | ⚠️ Hard if device lost | ✅ Easy (recover from backup) |
| Scalability | ✅ Distributed | ✅ Centralized |

**ARF Guidance:** Both are allowed. ARF assumes on-device secure hardware, but cloud with strong encryption is viable.

**Recommendation:** Hybrid is common—on-device for keys + cloud for metadata/backup.

---

### Q2: "Must we implement device binding?"

**A:** ARF 2.6.0+ says: **RECOMMENDED, not mandatory**

**In your profile:** You must declare if you support it or not.

```
Option A: "We require device binding for L2+"
  → More secure but less flexible

Option B: "We support device binding but don't require it"
  → More flexible but less secure

Option C: "We don't support device binding"
  → Simpler but less secure
```

**Recommendation:** At minimum, support it; whether you require it depends on your use cases.

---

### Q3: "How do we handle multiple credentials from different issuers?"

**A:** Design a **credential store** that can handle:
- Different credential formats (SD-JWT, CWT, JSON)
- Different issuers (government, university, employer)
- Different lifecycle (one expires, another is revoked, etc.)

**Architecture Pattern:**

```
Credential Store
  ├─ Metadata
  │  ├─ Issuer public key / cert
  │  ├─ Expiration date
  │  ├─ Revocation status
  │  └─ Supported claims
  │
  ├─ Payload (signed)
  │  ├─ Claims (name, birthdate, etc.)
  │  └─ Binding (device public key, holder proof)
  │
  └─ Storage
     ├─ Encryption (at-rest)
     └─ Access control (user auth required)
```

---

### Q4: "How do we manage issuer keys and trust?"

**A:** Maintain a **trust list** of trusted issuers:

```
Trust List
  ├─ Government PID Issuer
  │  ├─ Public key / certificate
  │  ├─ Revocation endpoint
  │  └─ Metadata endpoint
  │
  ├─ University Diploma Issuer
  │  ├─ Public key / certificate
  │  └─ Metadata endpoint
  │
  └─ [More issuers...]
```

**Sources:**
- Local (hard-coded for trusted issuers)
- Remote (fetch from metadata service)
- EU trust list (shared across member states)

---

### Q5: "What does accessibility really mean for our architecture?"

**A:** Accessibility constraints affect architecture at multiple levels:

```
UI Layer:
  ├─ WCAG 2.1 AA compliance (colors, fonts, contrast)
  ├─ Keyboard navigation (no mouse-only UI)
  ├─ Screen reader support (semantic HTML, ARIA labels)
  └─ Cognitive load (simple, clear language)

Interaction Layer:
  ├─ No complex gestures (swipe, pinch)
  ├─ No time-limited interactions (user has unlimited time to approve)
  └─ Clear error messages

System Layer:
  ├─ Support platform accessibility (iOS VoiceOver, Android TalkBack)
  └─ No reliance on color alone to convey information
```

**Recommendation:** Design accessibility from the start, not as an afterthought.

---

## Architecture Review Checklist

Before moving to implementation, review your architecture:

### Structural Completeness
- [ ] All five ARF layers addressed?
- [ ] Wallet Solution, Provider, Instance, Unit all defined?
- [ ] Integration points between components clear?
- [ ] Trust boundaries identified and documented?

### Data Flow Coverage
- [ ] Issuance flow designed?
- [ ] Presentation flow designed?
- [ ] Registration flow designed?
- [ ] Credential revocation flow designed?

### Cryptographic Architecture
- [ ] Key generation, storage, and rotation planned?
- [ ] Algorithm choices (RS256, ECDSA, etc.) justified?
- [ ] Device binding (if in scope) designed?
- [ ] Trust list management designed?

### Security Architecture
- [ ] Target assurance level identified?
- [ ] Required security controls mapped to architecture?
- [ ] Threat model drafted?
- [ ] Privacy controls (data minimization) designed?

### Accessibility
- [ ] WCAG 2.1 AA target identified?
- [ ] Keyboard navigation planned?
- [ ] Screen reader compatibility planned?
- [ ] Cognitive load assessed?

### Interoperability
- [ ] Standards compliance identified (OpenID4VCI, OpenID4VP)?
- [ ] Credential formats chosen (SD-JWT, CWT)?
- [ ] Rulebooks (PID, etc.) reviewed?
- [ ] Cross-border coordination planned?

### Operations & Governance
- [ ] Audit logging designed?
- [ ] Incident response integrated?
- [ ] Certification requirements mapped?
- [ ] Update/patch strategy defined?

---

## Key Resources

### ARF Documentation
- **ARF Main Document:** https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md (Chapters 3–6)
- **Architecture Layer Map:** [../architecture-layer-map.md](../architecture-layer-map.md)
- **Attestation Rulebooks:** https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog

### Standards & Specifications
- **OpenID4VCI:** https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html
- **OpenID4VP:** https://openid.net/specs/openid-4-verifiable-presentations-1_0.html
- **ISO/IEC 18013-5 (mDL):** Mobile credential standard
- **Cryptography Standards:** FIPS 140-2, ISO/IEC 14888

### On-Ramp Guides
- **Governance to Control Mapping:** [../governance-to-control-mapping.md](../governance-to-control-mapping.md) — Security controls
- **Conformance Interpretation:** [../conformance-interpretation-companion.md](../conformance-interpretation-companion.md) — Requirements

---

## Next Steps

1. **Map your system** to the [five ARF layers](../architecture-layer-map.md)
2. **Design data flows** for each scenario (issuance, presentation, registration)
3. **Identify cryptographic components** (key storage, algorithms, trust)
4. **Define security architecture** based on target assurance level
5. **Plan accessibility** compliance (WCAG 2.1 AA)
6. **Document architecture** with diagrams and specifications
7. **Share with security team** for threat modeling ([Security/Assurance path](./reading-path-security-assurance.md))
8. **Brief development team** on architecture ([Implementer path](./reading-path-implementer.md))

---

**Last Updated:** March 2026  
**ARF Alignment:** 2.8.0 (2026-02-02)
