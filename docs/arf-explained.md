# ARF Explained

This document provides a simplified structural walkthrough of the EU Digital Identity Wallet Architecture and Reference Framework (ARF).

It focuses on:
- **Architectural layers** — How the system is organized
- **Trust boundaries** — Who trusts whom and how
- **Governance structures** — Roles, oversight, certification
- **Interoperability assumptions** — How wallets work across borders and services
- **Key concepts** — Core ideas you'll encounter throughout the ARF

**Important:** This is not normative guidance. Refer to the official [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) for authoritative requirements.

---

## What Is the ARF?

The **Architecture and Reference Framework (ARF)** is the technical specification for how European Digital Identity Wallets must work.

**It defines:**

- What a wallet is and what it does
- Who participates in the ecosystem (wallet providers, issuers, services)
- How wallets issue, store, and share credentials
- How users remain in control of their identity data
- What security and privacy protections are required
- How wallets work across EU member states

**It does NOT:**

- Mandate a specific wallet implementation (app vs. web, native vs. cloud)
- Specify how member states must organize their governance
- Require a single technical standard for everything (multiple alternatives often allowed)
- Prevent innovation; allows room for vendor differentiation

---

## The Big Picture: Wallet Ecosystem

At the highest level, the wallet ecosystem has **four main participants**:

```
┌──────────────────────────────────────────────────────────────┐
│ CREDENTIAL ISSUER                                            │
│ (e.g., government ministry issuing passport data)            │
│ Authenticates the person → Issues credential → Sends to      │
│ wallet                                                       │
└──────────────────────────────────────────────────────────────┘
                              ↑
                              │
                          Issuance
                          (OpenID4VCI)
                              │
         ┌────────────────────┴────────────────────┐
         │                                         │
    ┌────▼──────┐                          ┌──────▼────┐
    │   WALLET  │                          │  SERVICE  │
    │           │                          │ (Relying  │
    │ User keeps│──Presentation Request──→ │  Party)  │
    │credentials│←─Credential Response─────│          │
    │ and proof │  (OpenID4VP)             │ Receives│
    │           │                          │ credential│
    └─────┬─────┘                          └──────────┘
          │
    ┌─────▼──────────────────────────┐
    │ WALLET PROVIDER                 │
    │ (Backend infrastructure)        │
    │ - Enrollment                    │
    │ - Device binding               │
    │ - Backup/recovery             │
    │ - Updates                      │
    └────────────────────────────────┘
```

**Data flows:**

1. **Issuance:** Issuer → Wallet (user receives credential)
2. **Presentation:** Wallet → Service (user shares credential to authenticate or access service)
3. **Support:** Wallet Provider ← → Wallet (backend services)

---

## Key Concepts

### 1. The Wallet

A **wallet** is more than just an app. It has multiple components:

| Component | What It Is | Where It Lives |
|-----------|-----------|---|
| **Wallet Solution** | Complete product (app + backend + support) | Everywhere |
| **Wallet Provider** | Backend infrastructure (servers, APIs) | Company data center |
| **Wallet Instance** | Running instance of the app | User's device |
| **Wallet Unit** | The part that holds credentials and keys | Phone's secure enclave OR cloud |

**Example:** Let's say you download a wallet app:
- The app you download = **Wallet Instance**
- The company's servers managing it = **Wallet Provider**
- The complete offering = **Wallet Solution**
- The secure chip storing your keys = **Wallet Unit**

### 2. Credentials (Attestations)

A **credential** is a digital proof of something about you. Examples:

| Type | What It Proves | Issued By | Example |
|------|---|---|---|
| **PID** | You are a specific person (government ID data) | Government | Name, date of birth, passport number |
| **EAA** | You have a specific attribute or status | Any authorized entity | Driver license, university diploma, employment status |
| **QEAA** | You have a qualified attribute (very high assurance) | Qualified provider | Advanced digital signature certificate |

**Key principle:** You don't share *your data*. You share *proof* of your data. The service gets the proof but doesn't get access to the underlying data unless you explicitly share it.

### 3. Trust Boundaries

The ARF defines **who must verify what**:

```
┌─────────────────────┐
│  Credential Issuer  │      Signs credential with
│  (e.g., government) │      their private key
└──────────┬──────────┘
           │
           ↓
    ┌──────────────┐
    │  Credential  │      User stores
    │  (e.g., PID) │      in wallet
    └──────┬───────┘
           │
           ↓
┌─────────────────────────────────┐
│      User's Wallet              │      Verifies issuer
│  (on phone or in cloud)         │      signature before
│                                 │      accepting credential
└──────────────┬──────────────────┘
               │
               ↓
        ┌─────────────┐
        │   Service   │          Uses issuer's
        │(Relying Party)         public key to verify
        │             │          credential signature
        └─────────────┘
```

**The rule:** You only trust credentials from issuers you've added to your trust list.

### 4. User Control

A core ARF principle: **The user controls what gets shared.**

**For proximity (NFC/BLE) authentication:**
- Service scans your phone
- Your wallet displays: "Service X wants your name and birthdate. Allow?"
- You decide: Share / Don't Share
- If you share, wallet proves it's your credential (you prove you're the wallet owner)

**For remote authentication:**
- Service sends credential request to your wallet (via QR code or redirect)
- Your wallet displays the request
- You approve and authenticate yourself (biometric, PIN)
- Wallet sends only what you approved

**The user is always in the loop.**

---

## Structural Overview: The Five Layers

The ARF is organized into five layers. Think of this like a building:

### Layer 1: Governance (The Rules)

*"Who certifies wallets? Who oversees compliance? What's the legal framework?"*

- Regulatory requirements from the EU regulation
- Member state certification and oversight
- Wallet certification criteria
- Ecosystem registry and notifications

**ARF Chapters:** 1, 2 (roles), 7 (oversight)

### Layer 2: Trust Framework (The Keys & Chains)

*"How do I know this credential came from a real issuer? How is a person bound to a credential?"*

- Cryptographic signatures and key management
- Certificate chains and trust lists
- Identity binding (biometric, device, cryptographic)
- Credential formats and structures

**ARF Chapters:** 4.2–4.3, 6 (security)

### Layer 3: Wallet Infrastructure (The Device)

*"How is the wallet structured? Where do keys get stored? How do users unlock the wallet?"*

- Wallet architecture and components
- Secure storage and key derivation
- User authentication and device binding
- Wallet lifecycle (installation through deactivation)

**ARF Chapters:** 3, 4.3, 6

### Layer 4: Protocols (The APIs & Flows)

*"How does the wallet talk to issuers and services? What APIs are used? What data flows happen?"*

- OpenID4VCI (credential issuance protocol)
- OpenID4VP (credential presentation protocol)
- Proximity and remote authentication flows
- Registration and enrollment processes

**ARF Chapters:** 4.1, 5, and [Technical Specifications](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications)

### Layer 5: Interoperability (The Standards)

*"How do wallets from different countries work together? What format are credentials in? What standards must we follow?"*

- Credential format standards (SD-JWT, CWT, JSON)
- Attestation rulebooks (PID, mDL, etc.)
- Cross-border metadata and discovery
- Technical standards (ISO, IETF, OpenID)

**ARF Chapters:** 2.3, 4.1 and [Attestation Rulebooks](https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog)

---

## Key Scenarios: What Actually Happens

### Scenario 1: Getting Your Passport in a Wallet

```
1. You open the wallet app on your phone
2. You select "Add Government Credential"
3. Wallet opens issuer's website (government ministry)
4. You authenticate with username/password
5. Government verifies it's really you
6. Government says: "Sign this attestation (PID)"
   → Wallet generates a keypair on the phone
   → Wallet sends public key to government
7. Government returns signed PID credential
   → Wallet stores on secure part of phone
   → Private key never leaves the phone
8. You now have proof of your identity in the wallet
   → No other entity knows this is in your wallet
```

**Trust check:** Your wallet only accepted the credential because you trust the government website.

### Scenario 2: Using Your Wallet to Log Into a Bank

```
1. You go to bank.example.com
2. Bank shows: "Use European Digital Identity"
3. You click the button
4. One of two things happens:

   OPTION A (Same Device - Web):
   - Bank generates a credential request
   - Redirects to wallet (or wallet app opens)
   - Wallet app shows: "Bank wants: Your name, address"
   - You authenticate to wallet (biometric/PIN)
   - Wallet sends: Your proof of identity
   - Bank verifies the signature
   - Bank grants access

   OPTION B (Cross-Device - Mobile App):
   - Bank shows a QR code
   - You scan with your phone
   - QR contains: Bank's credential request + polling URL
   - Wallet shows: "Bank wants: Your name, address"
   - You authenticate to wallet
   - Wallet sends proof to polling URL
   - Browser on bank website gets response
   - Bank grants access
```

**Key point:** The bank never got your actual identity data. They got a cryptographic proof that YOU verified and authorized.

### Scenario 3: Service Verification

```
Service receives credential from wallet:
  │
  ├─ Step 1: Check signature
  │         (Use government's public key)
  │         → Valid or Invalid?
  │
  ├─ Step 2: Check not revoked
  │         (Check revocation list)
  │         → Revoked or Valid?
  │
  ├─ Step 3: Check expiration
  │         (Is credential still valid?)
  │         → Expired or Valid?
  │
  ├─ Step 4: Verify user ownership
  │         (Did user prove they own this credential?)
  │         → YES or NO?
  │
  └─ Result: Accept credential or reject
```

---

## Trust Boundaries Illustrated

### High-Level Trust Model

```
┌─────────────────────────────────────────────────────────────┐
│                     ISSUER DOMAIN                           │
│         (e.g., Government Ministry)                         │
│                                                             │
│  ┌──────────────────────────────────┐                      │
│  │  Authenticate user              │                      │
│  │  Issue credential               │                      │
│  │  Sign with private key          │                      │
│  └──────────┬───────────────────────┘                      │
└─────────────────────────────────────────────────────────────┘
              │
              │ (Signed credential)
              ↓
┌─────────────────────────────────────────────────────────────┐
│              WALLET DOMAIN (User's Device)                  │
│                                                             │
│  ┌──────────────────────────────────┐                      │
│  │  Store credential securely       │                      │
│  │  Keep user's keys safe          │                      │
│  │  Authenticate user               │                      │
│  │  Prove ownership when sharing    │                      │
│  └──────────────────────────────────┘                      │
└──────────────┬───────────────────────────────────────────────┘
               │
               │ (User authorized proof)
               ↓
┌─────────────────────────────────────────────────────────────┐
│              SERVICE DOMAIN (Relying Party)                 │
│                                                             │
│  ┌──────────────────────────────────┐                      │
│  │  Receive proof                   │                      │
│  │  Verify issuer signature         │                      │
│  │  Verify user ownership           │                      │
│  │  Grant access if valid           │                      │
│  └──────────────────────────────────┘                      │
└─────────────────────────────────────────────────────────────┘
```

Each domain has clear responsibilities. Issuers verify people. Wallets protect keys and enforce user consent. Services verify proofs.

---

## Governance & Oversight

The ARF requires oversight at multiple levels:

### Member State Level
- Designate a **Supervisory Body** to oversee wallets in their country
- Maintain a list of **certified wallets**
- Enforce compliance with the ARF

### Wallet Provider Level
- Submit for certification (CIR 2024/2981)
- Meet security requirements (Chapter 6)
- Maintain a conformance profile
- Report incidents to supervisory body

### Ecosystem Level
- Maintain registry of **certified wallets**
- Maintain registry of **trusted issuers**
- Share metadata across countries
- Coordinate cross-border compliance

---

## Assurance Levels

The ARF defines **four assurance levels** (L0–L3):

| Level | Use Case | Example | Security Controls |
|-------|----------|---------|---|
| **L0** | Low-assurance, non-sensitive | Anonymous forum login | Basic authentication |
| **L1** | Standard public services | Government info access | Credential verification |
| **L2** | Sensitive services | Bank login, benefit claims | + Device binding, + User auth |
| **L3** | High-value transactions | Land registration, legal docs | + Highest crypto standards |

Your wallet might support multiple assurance levels. Services declare what level they require.

---

## Interoperability: The Cross-Border Problem

**The challenge:** Different countries have different government ID formats, different trust anchors, different rules.

**The ARF solution:**

1. **Define core requirements** that all wallets must meet
2. **Create rulebooks** for common credential types (PID, mDL, driver license)
3. **Establish trust lists** so wallets know which foreign issuers to trust
4. **Use open standards** (OpenID, CBOR) so anyone can implement
5. **Allow flexibility** in non-core areas (wallet UI, storage model)

**Result:** A Finnish wallet can accept an Italian government credential, and an Austrian bank can verify it.

---

## Accessibility: Design for Everyone

ARF Chapter 8 (added in 2.5.0) requires wallets to be accessible:

- **Visual:** Large text, high contrast, no color-only distinction
- **Motor:** Keyboard navigation, no complex gestures required
- **Cognitive:** Simple language, clear interactions
- **Audio:** Captions for any audio content

This isn't optional—it's a conformance requirement (Topic 54).

---

## What the ARF Doesn't Specify

Important: The ARF is intentionally flexible on some topics:

- **UI/UX design** — Wallets can look very different
- **Wallet storage model** — Keys can be on-device, in cloud, or hybrid
- **Wallet distribution** — App store, web, directly from provider
- **Issuer enrollment** — How users get credentials is issuer-specific
- **Certification body** — Member states choose their model

This allows vendors to innovate while maintaining baseline interoperability.

---

## How to Use This Walkthrough

### If You're a Policy Leader
1. Read sections: **Governance & Oversight**, **What Is the ARF**, **Assurance Levels**
2. Focus on regulatory requirements and oversight mechanisms
3. Understand the conformance levels and certification process

### If You're an Architect
1. Read sections: **The Five Layers**, **Trust Boundaries**, **Interoperability**
2. Understand how components relate to each other
3. Use [architecture-layer-map.md](./architecture-layer-map.md) for detailed decomposition

### If You're an Implementer
1. Read sections: **Structural Overview**, **Key Scenarios**, **Trust Boundaries**
2. Understand what each layer must do
3. Study the specific layers relevant to your component (see [reading-path-implementer.md](./reading-paths/reading-path-implementer.md))

### If You're in Security/Assurance
1. Read sections: **Governance & Oversight**, **Assurance Levels**, **Trust Boundaries**
2. Focus on security controls and evidence collection
3. Use [governance-to-control-mapping.md](./governance-to-control-mapping.md) to map policy to technical controls

---

## Next Steps

1. **Read your role-specific reading path** ([reading-paths/README.md](./reading-paths/README.md))
2. **Study the ARF main document** for normative details (https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md)
3. **Review annexes** for high-level requirements (Annex 2) and detailed specs (Annexes 3+)
4. **Check technical specifications** for protocol-level details
5. **Use [upstream-alignment-guide.md](./upstream-alignment-guide.md)** to track ARF changes

---

## Key Takeaways

✅ **The ARF creates a trust ecosystem** where users control their identity  
✅ **It's layered** — Governance, trust, infrastructure, protocols, interop  
✅ **It's intentionally flexible** on implementation details  
✅ **It's cross-border** — Designed for EU-wide interoperability  
✅ **It's secure** — Multiple assurance levels for different use cases  
✅ **It's accessible** — Requires design for all users  

---

**Important:** This is a simplified walkthrough. Refer to the official ARF Main Document for normative, authoritative guidance.

---

**Last Updated:** March 2026  
**ARF Alignment:** 2.8.0 (2026-02-02)
