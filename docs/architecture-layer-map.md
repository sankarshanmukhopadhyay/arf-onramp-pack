> **2026 re-audit note:** Read this document together with `legal-baseline-2026.md`. It remains a companion architectural decomposition and should not be treated as a substitute for the current implementing-act layer or the canonical ARF and STS repositories.

# Architecture Layer Map

This document decomposes the ARF into five logical architectural layers, showing how governance principles flow through to protocol implementation. Use this to understand system structure, identify your implementation scope, and navigate the ARF document.

---

## Layer Overview

```
┌─────────────────────────────────────────────────────────────┐
│ LAYER 1: GOVERNANCE LAYER                                   │
│ (Policies, roles, oversight, certification, regulation)     │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│ LAYER 2: TRUST FRAMEWORK LAYER                              │
│ (Trust boundaries, identity binding, attestation models)    │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│ LAYER 3: WALLET INFRASTRUCTURE LAYER                        │
│ (Wallet components, device binding, storage, lifecycle)     │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│ LAYER 4: PROTOCOL INTERACTION LAYER                         │
│ (OpenID4VCI, OpenID4VP, HAIP, data flows, authentication)   │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│ LAYER 5: INTEROPERABILITY LAYER                             │
│ (Standards, formats, cross-border, ecosystem coordination)  │
└─────────────────────────────────────────────────────────────┘
```

Each layer depends on the layers beneath it. Changes at lower layers propagate upward.

---

## Layer 1: Governance Layer

**Purpose:** Define roles, responsibilities, policy requirements, and oversight mechanisms.

**Scope:** Who does what? How is compliance ensured? What are the rules?

### Components

| Component | Description | ARF Reference |
|-----------|-------------|---|
| **Regulatory Framework** | EU Digital Identity Regulation + CIRs | Reg 2024/910, CIRs 2024/2977–2024/2982 |
| **Roles & Responsibilities** | Wallet Provider, PID Provider, Attestation Provider, RP, Supervisory Bodies | ARF Section 2.2 |
| **Certification Model** | Wallet Solution certification criteria and processes | ARF Chapter 7, CIR 2024/2981 |
| **Conformance Profiles** | Requirement sets for different deployment contexts | ARF Annex 2 (Topics 1–10) |
| **Ecosystem Notification** | Registry of wallets, providers, and trusted entities | ARF Section 4.1, CIR 2024/2980 |
| **Supervisory Oversight** | Compliance monitoring and incident response | ARF Chapter 7 |
| **Interoperability Governance** | Cross-border coordination and compatibility | ARF Section 2.3 |

### Key Decisions at This Layer

- **Who operates the wallet?** (Government, private provider, hybrid)
- **What conformance profile applies?** (L0–L3 assurance level)
- **What governance model?** (Centralized, decentralized, federated)
- **Who certifies compliance?** (Member state, independent body)

### Implementation Responsibility

**Policy owners, program leads, compliance teams** define the governance layer. This layer is *not directly implemented* in code but drives all lower-layer choices.

---

## Layer 2: Trust Framework Layer

**Purpose:** Establish cryptographic and logical trust boundaries between ecosystem participants.

**Scope:** Who trusts whom? How is identity bound to credentials? What attestation models apply?

### Components

| Component | Description | ARF Reference |
|-----------|-------------|---|
| **Issuer Trust** | PID Providers, Attestation Providers, their certification | ARF Section 2.2 |
| **Credential Binding** | Cryptographic link between credential and wallet/holder | ARF Section 4.2.1 |
| **Attestation Models** | PID, EAA, QEAA, custom attestations | ARF Section 4.2 |
| **Key Binding** | Public key infrastructure for wallet signatures | ARF Section 3.4 |
| **Trust Anchors** | Root certificates, trust lists, certificate transparency | ARF Topic 55 (ARF 2.8.0+) |
| **Cross-Border Trust** | Recognition of foreign issuers and credentials | ARF Section 2.3, CIR 2025/846 |
| **Holder Identity** | Binding between physical person and wallet | ARF Section 4.3 |

### Key Decisions at This Layer

- **Who is the authoritative issuer for this credential?**
- **How is the holder bound to the credential?** (Biometric, device, cryptographic key)
- **What credential format?** (SD-JWT, CWT, CBOR, JSON)
- **How do I verify the issuer's signature?** (Certificate chain, trusted list)

### Implementation Responsibility

**Architects, security teams** design the trust model. **Cryptography teams** implement key management and signature verification. **Compliance teams** maintain trust lists.

---

## Layer 3: Wallet Infrastructure Layer

**Purpose:** Specify wallet components, storage, lifecycle, and device integration.

**Scope:** How is the wallet structured? What are the data stores? How is the device protected?

### Components

| Component | Description | ARF Reference |
|-----------|-------------|---|
| **Wallet Solution** | Complete system (provider + instances) | ARF Section 3.1 |
| **Wallet Provider** | Backend infrastructure and support | ARF Section 3.2 |
| **Wallet Instance** | Running instance of wallet app/service | ARF Section 3.3 |
| **Wallet Unit** | Component holding credentials and keys | ARF Section 3.4 |
| **Device Binding** | Cryptographic link to physical device | ARF Section 4.3.2, Topic 26 |
| **User Authentication** | Unlocking wallet, accessing credentials | ARF Section 6.5.3.3, Topic 40 |
| **Credential Storage** | Secure storage of credentials and keys | ARF Section 3.4, 6.3.2 |
| **Key Management** | Key generation, storage, rotation, backup | ARF Section 6.3.2, Topic 29 |
| **Wallet Lifecycle** | Installation, provisioning, revocation, deletion | ARF Section 4.4 |
| **Accessibility** | Design for all users | ARF Chapter 8, Topic 54 |

### Key Decisions at This Layer

- **Native app vs. web wallet?**
- **Where are credentials stored?** (Local, cloud, hybrid)
- **How do I authenticate the user?** (PIN, biometric, device unlock)
- **Is device binding required?** (ARF 2.6.0+: recommended, not mandatory)
- **How do I handle backup/restore?**
- **What's the lifecycle from provisioning to deactivation?**

### Implementation Responsibility

**Backend engineers** build Wallet Provider infrastructure. **Mobile/web developers** implement Wallet Instance. **Security teams** design key storage and authentication. **UX teams** implement accessibility (Chapter 8).

---

## Layer 4: Protocol Interaction Layer

**Purpose:** Define how wallet communicates with issuers, verifiers, and devices.

**Scope:** What are the APIs? How do data flows work? Which protocols are used?

### Components

| Component | Description | ARF Reference |
|-----------|-------------|---|
| **Issuance Flow** | OpenID4VCI (issuer → wallet) | ARF Section 5.1.1, CIR 2024/2982 |
| **Presentation Flow** | OpenID4VP (wallet → verifier) | ARF Section 5.2.1, CIR 2024/2982 |
| **Proximity Protocol** | NFC/BLE (wallet ↔ proximity reader) | ARF Section 5.1.2, HAIP spec |
| **Remote Same-Device** | Web/app redirect flow (RP → wallet) | ARF Section 5.2.2 |
| **Remote Cross-Device** | QR code + polling (RP ↔ wallet) | ARF Section 5.2.3 |
| **Device Registration** | Device → Wallet Provider registration | ARF Section 5.4.1 |
| **RP Registration** | RP → Supervisory Body registration | ARF Section 5.4.2, CIR 2025/848 |
| **Notification Protocol** | Wallet notifications to Supervisory Bodies | ARF Section 4.1, CIR 2024/2980 |

### Key Decisions at This Layer

- **Which issuance flow?** (Pre-authorized, authorization code, pushed credentials)
- **Which presentation flow?** (Proximity, remote, hybrid)
- **How does the user approve sharing?** (On-device UI, device unlock)
- **How are errors handled?** (Retry logic, user messaging)
- **What's the credential refresh strategy?**

### Implementation Responsibility

**Backend engineers** implement API endpoints. **Mobile/web developers** implement client flows. **Integration teams** coordinate between wallet and RP systems.

---

## Layer 5: Interoperability Layer

**Purpose:** Ensure wallets work across borders, with multiple issuers, and multiple RPs.

**Scope:** What standards apply? How do I interoperate with other systems?

### Components

| Component | Description | ARF Reference |
|-----------|-------------|---|
| **Credential Format Standards** | SD-JWT, CWT, CBOR, JSON structures | CIR 2024/2977, Rulebooks |
| **Attestation Rulebooks** | PID, mDL, custom rulebooks | https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog |
| **Interop Profiles** | Subset of ARF for cross-border use | ARF Section 2.3, Annex 4 |
| **Metadata Exchange** | Discovery of issuers, formats, policies | ARF Section 4.1 |
| **Cross-Border Flows** | Multi-country scenarios | ARF Section 2.3, CIR 2025/846 |
| **Technical Specifications** | OpenID, CBOR, cryptography specs | ARF [Technical Specs](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications) |
| **Compatibility Testing** | Conformance suites, test vectors | ARF Section 7.3, CIR 2024/2981 |

### Key Decisions at This Layer

- **Which attestation rulebooks must I support?** (PID, mDL, others)
- **How do I discover other wallets' metadata?**
- **Can my wallet work with wallets from other countries?**
- **Which standards do I target?** (Baseline, extended, custom)

### Implementation Responsibility

**Integration teams** ensure ecosystem compatibility. **QA teams** run cross-wallet tests. **Standards teams** maintain rulebooks and metadata.

---

## Cross-Layer Relationships

Understanding how layers interact is crucial for avoiding architectural drift:

### Example 1: Device Binding (Governance → Infrastructure)

```
Layer 1 (Governance):    Policy decision: Device binding recommended (ARF 2.6.0+)
                          ↓
Layer 2 (Trust):         Design: Binding certificate with public key
                          ↓
Layer 3 (Infrastructure): Implementation: Key derivation + storage on secure hardware
                          ↓
Layer 4 (Protocol):      Data format: Certificate in OpenID4VP credential
                          ↓
Layer 5 (Interop):       Standard: Certificate format per ISO/IEC 14888
```

### Example 2: Credential Issuance (Trust → Protocol → Interop)

```
Layer 2 (Trust):         Design: PID issued by government, signed with root key
                          ↓
Layer 4 (Protocol):      Flow: OpenID4VCI (authorization code + credential endpoint)
                          ↓
Layer 5 (Interop):       Format: PID Rulebook (SD-JWT format + claim structure)
```

### Example 3: Security Controls (Governance → Infrastructure → Protocol)

```
Layer 1 (Governance):    Requirement: Wallet L2 assurance (CIR 2024/2981)
                          ↓
Layer 3 (Infrastructure): Control: Device binding + biometric auth + encrypted storage
                          ↓
Layer 4 (Protocol):      Evidence: Token request includes device proof
                          ↓
Layer 2 (Trust):         Validation: Issuer verifies device proof signature
```

---

## Using This Map to Navigate the ARF

### If You Need to Understand...

| Question | Relevant Layers | ARF Sections |
|----------|---|---|
| "Who certifies my wallet?" | Layer 1 (Governance) | Chapter 7, CIR 2024/2981 |
| "How do I sign credentials?" | Layer 2 (Trust), Layer 3 (Infrastructure) | Section 3.4, 6.3.2 |
| "What data flows exist?" | Layer 4 (Protocol), Layer 5 (Interop) | Chapter 5 |
| "How do I support PID?" | Layer 2 (Trust), Layer 4 (Protocol), Layer 5 (Interop) | Section 4.2, [PID Rulebook](https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog) |
| "How do I prevent tampering?" | Layer 3 (Infrastructure), Layer 2 (Trust) | Chapter 6, Section 3.4 |
| "How does cross-border work?" | Layer 5 (Interop), Layer 1 (Governance) | Section 2.3, CIR 2025/846 |

### If You're Implementing...

| Component | Start at Layer | Key Sections | Then Read |
|-----------|---|---|---|
| **Wallet Backend** | Layer 3 | ARF Section 3.2 | → Layers 4, 5 for APIs |
| **Credential Storage** | Layer 3 | ARF Section 3.4 | → Layer 2 for format |
| **OpenID4VCI Client** | Layer 4 | ARF Section 5.1.1 | → Layers 2, 5 for credential spec |
| **RP Service** | Layer 4 | ARF Section 5.2 | → Layers 2, 5 for credential verification |
| **Certification Documentation** | Layer 1 | ARF Chapter 7 | → All layers for evidence |

---

## Dependency Chain

Changes at higher layers typically require changes at lower layers:

```
Governance Change (Layer 1)
    ↓
Trust Model Update (Layer 2)
    ↓
Infrastructure Redesign (Layer 3)
    ↓
Protocol Changes (Layer 4)
    ↓
Standard Updates (Layer 5)
```

**Example:** If governance adds a new assurance level (L3.5), you may need:
- New trust boundaries (Layer 2)
- Enhanced key management (Layer 3)
- New protocol extensions (Layer 4)
- Interop profile updates (Layer 5)

Conversely, you can rarely change lower layers without affecting higher layers.

---

## Architecture Patterns

### Pattern 1: Multi-Attestation Wallet

A wallet supporting multiple credential types (PID, mDL, custom):

```
Layer 5 (Interop):   Multiple rulebooks (PID, mDL, custom)
    ↓
Layer 4 (Protocol):  Single OpenID4VCI endpoint + multi-format credential response
    ↓
Layer 3 (Infra):     Single credential store; per-format serialization
    ↓
Layer 2 (Trust):     Multiple issuers, different trust anchors
    ↓
Layer 1 (Governance): Conformance profile declares supported types
```

### Pattern 2: Federated Governance

Multiple providers sharing a single wallet offering:

```
Layer 1 (Governance): Federated policy + certification
    ↓
Layer 3 (Infra):     Shared backend; multi-provider coordination
    ↓
Layer 4 (Protocol):  Multi-endpoint issuance / presentation
    ↓
Layer 5 (Interop):   Shared metadata service
```

### Pattern 3: Mobile-First Wallet

Wallet optimized for mobile devices:

```
Layer 3 (Infra):     Mobile app instance + secure enclave for keys
    ↓
Layer 4 (Protocol):  QR code–based flows (proximity for NFC, QR for remote)
    ↓
Layer 5 (Interop):   Mobile-specific credential formats
    ↓
Layer 1 (Governance): Mobile-specific conformance profile
```

---

## Common Architectural Drift Risks

### Risk 1: Governance Requirements Not Enforced by Infrastructure

**Symptom:** Policy requires device binding (Layer 1), but implementation has no device verification (Layer 3).

**Prevention:** Review Layer 1 requirements and trace through to Layer 3 implementation.

### Risk 2: Protocol Doesn't Support Trust Model

**Symptom:** Trust model requires issuer revocation checking (Layer 2), but OpenID4VCI endpoint has no revocation endpoint (Layer 4).

**Prevention:** Validate that Layer 4 protocols support Layer 2 trust model.

### Risk 3: Interop Standards Forgotten in Custom Implementation

**Symptom:** Custom credential format (Layer 5) not compatible with rulebook (Layer 5), breaking cross-wallet interop.

**Prevention:** Validate Layer 5 conformance before finalizing Layer 4 protocol.

---

## Mapping to On-Ramp Documents

| Document | Focuses On Layers |
|----------|---|
| [arf-explained.md](./arf-explained.md) | Overview of all layers |
| [conformance-interpretation-companion.md](./conformance-interpretation-companion.md) | Layers 1 → 4 (how to test each) |
| [governance-to-control-mapping.md](./governance-to-control-mapping.md) | Layers 1 → 3 (governance → controls) |
| [upstream-alignment-guide.md](./upstream-alignment-guide.md) | Changes across all layers |
| [reading-path-architect.md](../reading-paths/reading-path-architect.md) | Layers 2–3 (system design) |
| [reading-path-implementer.md](../reading-paths/reading-path-implementer.md) | Layers 3–5 (code & protocol) |
| [reading-path-security-assurance.md](../reading-paths/reading-path-security-assurance.md) | Layers 1–3 (controls & evidence) |

---

## Tools for Layer Analysis

### Questions to Ask

- **Layer 1:** Which governance requirements drive my implementation?
- **Layer 2:** What trust boundaries and cryptographic bindings do I need?
- **Layer 3:** How do I structure my wallet components?
- **Layer 4:** Which protocols and flows must I support?
- **Layer 5:** Which standards and formats must I conform to?

### Traceability Template

Use this to map requirements through all layers:

```
Requirement:  [ARF reference]
Layer 1 (Gov): [Regulatory requirement]
Layer 2 (Trust): [Trust model implication]
Layer 3 (Infra): [System component needed]
Layer 4 (Protocol): [API/endpoint needed]
Layer 5 (Interop): [Standard/format needed]
Evidence: [Test case / documentation]
```

---

## Next Steps

1. **Review your system architecture** and identify which layers you're implementing
2. **Map your requirements** using the questions above
3. **Use the layer dependencies** to identify potential gaps or conflicts
4. **Trace governance requirements** from Layer 1 all the way to Layer 5 implementation
5. **Document your layer boundaries** in your architecture documentation

---

**Last Updated:** April 14, 2026  
**ARF Alignment:** 2.8.0 (2026-02-02)
