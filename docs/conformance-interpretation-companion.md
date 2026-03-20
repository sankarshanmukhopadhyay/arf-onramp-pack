# Conformance Interpretation Companion

## Purpose

This document translates ARF normative expectations into implementation-facing interpretation guidance. It helps teams reason about what conformance means operationally and plan evidence collection.

**Important:** This does not modify or override the ARF. Refer to the official [ARF Main Document](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) and [Annex 2 (High-Level Requirements)](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/annexes) for normative details.

---

## Conformance Categories

Requirements in the ARF fall into different categories. Understanding the category helps you plan implementation and evidence.

| Category | Description | Implementation Implication | Example |
|-----------|-------------|------------------------------|---------|
| **Mandatory** | Explicit SHALL / MUST requirements | Engineering requirement; must be implemented; evidence required | "Wallet SHALL verify issuer signature before accepting credential" (Topic 12) |
| **Conditional** | Context-dependent requirements (IF…THEN) | Implement based on your deployment role or feature set | "IF wallet supports proximity authentication, THEN it SHALL use HAIP protocol" |
| **Contextual** | Ecosystem-level obligation (roles, governance) | May require governance coordination; not necessarily testable in isolation | "Member States SHALL designate a Supervisory Body" (not a wallet requirement) |
| **Informative** | Explanatory guidance, principles, best practices | Not directly testable but architecturally relevant; understand intent | "Wallets should design for accessibility" → Topic 54 has testable requirements |
| **Configuration** | Choice points where ARF allows alternatives | Select based on your conformance profile | "Credential format SHALL be SD-JWT OR CWT" → Your wallet chooses one or both |

---

## Interpretation Principles

Use these principles to correctly interpret ARF requirements:

### 1. Separate Protocol Requirements from Governance Constructs

**Protocol Requirement** = Something your code must do
```
"Wallet MUST verify the issuer signature"
  → Code must call cryptographic signature verification
  → Evidence: Test case showing signature verification
```

**Governance Construct** = Something your organization must do
```
"Wallet Provider SHALL maintain incident response procedures"
  → Not code; requires a documented process
  → Evidence: Policy document, incident log, response plan
```

**Why this matters:** You can't test governance by running code. You need different evidence types.

### 2. Identify the Scope Level

Requirements operate at three levels. Know which one you're implementing:

| Level | Scope | Example | Implementation Responsibility |
|-------|-------|---------|---|
| **Wallet-Level** | Single wallet instance | "Wallet SHALL display credential presentation request to user" | Engineering team |
| **Provider-Level** | Wallet Provider backend service | "Wallet Provider SHALL maintain audit logs" | Backend/DevOps team |
| **Ecosystem-Level** | Across multiple wallets, issuers, services | "Supervisory Bodies SHALL maintain certified wallet registry" | Governance team |

**Rule:** Map each requirement to the right level.

### 3. Don't Collapse Advisory into Normative

The ARF uses **"SHALL" / "MUST"** (normative/mandatory) and **"SHOULD" / "MAY"** (advisory).

**Wrong:**
```
ARF says: "Wallet SHOULD support biometric authentication"
Your interpretation: "We'll implement it sometime"
  → Risk: Certification body expects evidence of consideration
```

**Right:**
```
ARF says: "Wallet SHOULD support biometric authentication"
Your interpretation: "We either implement it OR document why we didn't"
  → Evidence: Implementation OR decision record with reasoning
```

### 4. Map Normative Clauses to Testable Behaviors

Not all requirements are directly testable by automated tests. Some require manual verification or documentation review.

| Requirement Type | How to Test | Evidence Type |
|---|---|---|
| **Code behavior** | Automated test, manual test | Test report, code review |
| **Data format** | Schema validation, example verification | Schema, test vectors |
| **Cryptographic operation** | Cryptographic test vectors | Test suite results |
| **Process/procedure** | Audit trail, document review | Policy, logs, records |
| **User-facing behavior** | User acceptance test, manual verification | Test report, screenshots |
| **Architecture property** | Design review, threat model verification | Architecture doc, threat model |

---

## Conformance Assessment Framework

Use this framework to plan and execute conformance assessment.

### Step 1: Extract Normative Clauses from ARF

**Source:** [Annex 2 (High-Level Requirements)](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/annexes)

Annex 2 is organized by **Topics** (1–55). Each Topic contains:
- Topic title (e.g., "Wallet Provider Functional Requirements")
- High-Level Requirements (typically 3–10 per topic)
- Associated ARF main document sections

**Example:** Topic 12 (Credential Verification) includes:
```
HLR-012-01: Wallet SHALL verify issuer signature before accepting credential
HLR-012-02: Wallet SHALL check credential expiration
HLR-012-03: Wallet SHALL verify credential not revoked (if applicable)
```

**Tool:** Use the [ARF CSV file](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/hltr/high-level-requirements.csv) for searchable, sortable requirements.

### Step 2: Classify Each Requirement

For each requirement, classify it using the categories above:

```
HLR-012-01: Wallet SHALL verify issuer signature
  ├─ Category: MANDATORY
  ├─ Scope: Wallet-Level
  ├─ Type: Code Behavior
  └─ Test: Automated (signature verification test)
```

### Step 3: Map Requirement to System Component

Identify which part of your system implements this requirement:

```
HLR-012-01: Wallet SHALL verify issuer signature
  └─ Component: CredentialValidator (module in Wallet Instance)
     └─ Method: verify_issuer_signature()
```

### Step 4: Identify Testable Evidence

Plan what evidence you'll collect to prove conformance:

```
HLR-012-01: Wallet SHALL verify issuer signature
  ├─ Test Case: "Valid signature from trusted issuer → Accept credential"
  ├─ Test Case: "Invalid signature from any issuer → Reject credential"
  ├─ Test Case: "Valid signature from untrusted issuer → Reject credential"
  ├─ Evidence Artifact: Unit test results (test-signature-verification.log)
  ├─ Evidence Artifact: Code review (CredentialValidator module approved)
  └─ Evidence Artifact: Integration test results (e2e-credential-acceptance.log)
```

### Step 5: Record Traceability

Maintain a **Traceability Matrix** linking requirements to implementation and evidence:

```
| ARF Ref | HLR ID | Component | Test Case | Status | Evidence |
|---------|--------|-----------|-----------|--------|----------|
| Topic 12 | HLR-012-01 | CredentialValidator | test_valid_signature_trusted_issuer | ✅ PASS | [link] |
| Topic 12 | HLR-012-01 | CredentialValidator | test_invalid_signature_reject | ✅ PASS | [link] |
| Topic 12 | HLR-012-02 | CredentialValidator | test_expiration_check | ✅ PASS | [link] |
```

---

## Traceability Model & Matrix

A **Traceability Matrix** is the foundation of conformance evidence. It links:
- **ARF requirement** (normative statement)
- **Your internal requirement** (how you frame it)
- **System component** (code, config, process)
- **Verification method** (test, review, audit)
- **Evidence artifact** (test report, code, doc)
- **Status** (Pass, Fail, N/A, Not Yet Tested)

### Template

```markdown
| ARF Reference | HLR ID | Your Req ID | Component | Verification Method | Evidence Artifact | Status |
|---|---|---|---|---|---|---|
| Topic XX, Section Y | HLR-XXX-YY | REQ-ABC-123 | ComponentName | Unit test | test-report-v1.2.pdf | ✅ PASS |
| Topic XX, Section Z | HLR-XXX-ZZ | REQ-ABC-124 | ComponentName | Code review | cr-2024-03-15.md | ✅ PASS |
| Topic YY, Section A | HLR-YYY-AA | REQ-DEF-567 | OtherComponent | Audit log review | audit-logs-2024.csv | ⚠️ REVIEW |
```

### Benefits

- **Traceability:** Auditors can see exactly which code/doc proves conformance to each ARF requirement
- **Completeness:** You track whether all requirements are covered
- **Clarity:** No ambiguity about which requirement is satisfied by which evidence
- **Change Management:** When ARF changes, update the matrix to track impact

### Tool Recommendations

**Spreadsheet (Lightweight):**
- Google Sheets or Excel
- Easy to share and version control
- Good for <100 requirements

**Requirements Management Tools (Enterprise):**
- DOORS, Jama, Requisite Pro
- Better for 100+ requirements and large teams
- Integrates with test automation

---

## Conformance Profile

A **Conformance Profile** is a specific subset of ARF requirements that apply to your wallet.

### Why Profiles?

The ARF is comprehensive. Not every requirement applies to every wallet:
- A government wallet might require L3 assurance (highest security)
- A private sector wallet might support L1–L2
- A pilot wallet might implement a subset for MVP

**Conformance Profile = Set of requirements you commit to**

### How to Define Your Profile

**1. Choose Assurance Level (L0–L3)**

```
Decision: "We're implementing L2 assurance wallet"
  → Must implement all L2 requirements
  → May skip higher-level (L3) optional features
  → Must implement all L0–L1 baseline
```

**2. Choose Scope**

```
Decision: "We support PID, European Driver License, and custom university credentials"
  → Must implement PID rulebook requirements
  → Must implement mDL rulebook requirements (for driver license)
  → Custom format must meet generic attestation requirements
```

**3. Choose Authentication Modes**

```
Decision: "We support remote same-device and cross-device flows (not proximity/NFC)"
  → Must implement remote authentication (Section 5.2)
  → May skip proximity authentication (Section 5.1)
  → Must implement user consent & approval
```

**4. Choose Optional Features**

```
Decision: "Device binding is recommended but optional; we'll implement it"
  → Topic 26 requirements apply
  → Add device binding test cases to matrix
```

### Document Your Profile

Create a **Conformance Profile Document**:

```markdown
# Wallet Conformance Profile

## Summary
- **Assurance Level:** L2
- **Release:** v1.0 (ARF 2.8.0)
- **Wallet Type:** Government-issued to citizens
- **Supported Credentials:** PID, EAA (university diploma)

## Scope
- ✅ Remote same-device authentication
- ✅ Remote cross-device authentication (QR code)
- ❌ Proximity authentication (NFC/BLE)
- ✅ Device binding
- ✅ Biometric authentication

## Assurance Level Mapping
| L0 | L1 | L2 | L3 |
|----|----|----|-----|
| ✅ | ✅ | ✅ | ❌ (optional) |

## Requirements Coverage
- Total HLRs in scope: 45
- Implemented: 45 (100%)
- Deferred: 0
- Not applicable: 10

## Certification Target
- CIR 2024/2981 compliance for L2 wallets
- Supervisory Body: [Member State]
- Timeline: Q3 2026
```

---

## Common Interpretation Challenges

### Challenge 1: "SHALL" vs. "SHOULD" vs. "MAY"

**ARF Language Rules (RFC 8174):**
- **SHALL / MUST** = Mandatory; you must implement
- **SHOULD / RECOMMEND** = Strongly advised; implement unless you have a good reason not to
- **MAY / OPTIONAL** = Truly optional; document your choice

**Common Mistake:**
```
ARF: "Wallet Provider SHOULD support wallet recovery"
Team: "We'll skip it; it's just a SHOULD"
Auditor: "Why didn't you implement recovery? Document your decision."
```

**Correct Approach:**
```
ARF: "Wallet Provider SHOULD support wallet recovery"
Decision: "We implement recovery via cloud backup"
Evidence: "Feature specification, test cases, user docs"
OR
Decision: "We don't support recovery; users can re-enroll"
Evidence: "Decision record explaining security/UX tradeoff"
```

### Challenge 2: "If Applicable" Conditions

**ARF often uses conditional language:**
```
"If the wallet supports proximity authentication, it SHALL use HAIP protocol"
```

**Interpretation:**
```
If you DON'T support proximity → Requirement doesn't apply
If you DO support proximity → Requirement MUST be met
→ Document your choice in Conformance Profile
```

### Challenge 3: "Shall Not" (Negative Requirements)

**Example:**
```
"Wallet SHALL NOT share credentials without user consent"
```

**How to Test:**
- ✅ Test that credentials are never shared without user action
- ✅ Test that user action (approval) is required before sharing
- ✅ Test that cancellation prevents sharing
- ❌ (Can't test "never happens" directly—test the positive case instead)

### Challenge 4: Governance vs. Engineering Requirements

**Governance Requirement:**
```
"Wallet Provider SHALL maintain incident response procedures"
```

**Evidence:**
- Documented incident response policy ✅
- Incident log showing responses ✅
- Training records for team ✅
- Not a code test ❌

**Engineering Requirement:**
```
"Wallet SHALL encrypt credentials at rest"
```

**Evidence:**
- Code review showing encryption ✅
- Security test showing encrypted storage ✅
- Decryption only on user unlock ✅
- Unit test of encryption/decryption ✅

---

## Requirement Categories by Topic

The ARF Annex 2 groups requirements by topic. Here's what each topic group requires:

### Governance Topics (1–10)
**Focus:** Roles, responsibilities, ecosystem governance

| Topic | Title | Implementation Responsibility |
|-------|-------|---|
| 1–3 | Wallet/Provider/Ecosystem governance | Program office, not engineering |
| 4–5 | Certification & conformance | Program office, compliance team |
| 6–10 | Supervisory oversight, incident response | Program office, DevOps, security |

### Architecture & Wallet Topics (11–25)
**Focus:** System structure, data flows, credential handling

| Topic | Title | Implementation Responsibility |
|-------|-------|---|
| 11–15 | Wallet architecture, credential verification | Architects, backend engineers |
| 16–20 | Data flows, authentication scenarios | Backend, mobile/web engineers |
| 21–25 | Interoperability, ecosystem coordination | Integration engineers |

### Security & Privacy Topics (26–40)
**Focus:** Cryptography, key management, user authentication, privacy

| Topic | Title | Implementation Responsibility |
|-------|-------|---|
| 26–30 | Device binding, key management, cryptography | Security engineers, backend engineers |
| 31–35 | Privacy, data minimization, audit logging | Privacy officers, backend engineers |
| 36–40 | User authentication, access controls | Mobile/web engineers, security engineers |

### Attestation & Assurance Topics (41–55)
**Focus:** Credential formats, quality assurance, certification evidence

| Topic | Title | Implementation Responsibility |
|-------|-------|---|
| 41–45 | Attestation formats, PID/EAA specifications | Integration engineers, rulebook experts |
| 46–50 | Quality assurance, testing | QA engineers, integration engineers |
| 51–55 | Accessibility, assurance evidence, certification | Accessibility specialists, compliance team |

---

## Evidence Types & Collection

Different requirement types need different evidence:

### Requirement Type: Code Behavior

**Example:** "Wallet SHALL verify issuer signature"

**Evidence Type:** Test report
```
Test Case: Signature Verification
  ├─ Valid signature, trusted issuer → Accept ✅
  ├─ Invalid signature, any issuer → Reject ✅
  ├─ Valid signature, untrusted issuer → Reject ✅
  └─ Results: 3/3 pass (100%)
```

**Collection:** Automated unit tests + integration tests

---

### Requirement Type: Data Format

**Example:** "PID credential SHALL conform to PID rulebook schema"

**Evidence Type:** Schema validation report
```
Validation:
  ├─ Credential JSON validates against PID schema ✅
  ├─ All mandatory claims present ✅
  ├─ No unknown claims ✅
  └─ Date formats per ISO 8601 ✅
```

**Collection:** Schema validation tools + test vectors

---

### Requirement Type: Cryptographic Operation

**Example:** "Credential signature SHALL use RS256 algorithm"

**Evidence Type:** Cryptographic test vectors
```
Test Vector:
  ├─ Message: [test payload]
  ├─ Expected Signature: [NIST test vector]
  ├─ Actual Signature: [your code output]
  └─ Match: ✅ YES
```

**Collection:** NIST test vectors, cryptographic test suites

---

### Requirement Type: Architecture Property

**Example:** "Device binding SHALL cryptographically link wallet to device"

**Evidence Type:** Architecture documentation + threat model
```
Architecture:
  ├─ Device generates key pair on secure hardware ✅
  ├─ Private key never leaves device ✅
  ├─ Public key bound to credential ✅
  └─ Credential + signature proves device ownership ✅

Threat Model:
  ├─ Attacker can't use credential on different device (because device proof required) ✅
```

**Collection:** Architecture review, threat modeling session, code review

---

### Requirement Type: Process/Procedure

**Example:** "Wallet Provider SHALL maintain incident response procedures"

**Evidence Type:** Policy document + incident logs
```
Policy:
  ├─ Document: "Incident Response Policy v1.2" ✅
  ├─ Roles defined (incident commander, communicator, etc.) ✅
  ├─ Response timeline (detect → report → remediate) ✅
  └─ Annual training required ✅

Logs:
  ├─ Incident 2024-01 (security vulnerability) 
     - Detected: [date/time]
     - Reported to CERT: [date/time]
     - Fixed: [date/time]
     ✅ Policy followed
```

**Collection:** Policy review, incident log audit

---

### Requirement Type: User-Facing Behavior

**Example:** "Wallet SHALL display credential request and obtain user approval before sharing"

**Evidence Type:** User acceptance test + screenshots
```
Test Scenario: User approves credential sharing

Steps:
  1. Service requests credential via QR code
  2. Wallet app displays request showing:
     - Service name ✅
     - Requested claims (name, birthdate) ✅
     - "Approve" and "Deny" buttons ✅
  3. User taps "Approve"
  4. Wallet prompts for authentication (biometric/PIN) ✅
  5. User completes authentication
  6. Wallet sends credential ✅

Result: ✅ PASS
```

**Collection:** Manual testing, UX reviews, screenshots

---

## Mapping ARF Topics to Your Architecture Layers

Use the [architecture-layer-map.md](./architecture-layer-map.md) to organize requirements by layer:

| ARF Topic | Governance Layer | Trust Layer | Infrastructure Layer | Protocol Layer | Interop Layer |
|-----------|---|---|---|---|---|
| **1–5** | ✅ | | | | |
| **6–10** | ✅ | | | | |
| **11–15** | | ✅ | ✅ | | |
| **16–20** | | | ✅ | ✅ | |
| **21–25** | | | | | ✅ |
| **26–30** | | ✅ | ✅ | | |
| **31–40** | ✅ | ✅ | ✅ | ✅ | |
| **41–50** | | ✅ | | ✅ | ✅ |
| **51–55** | ✅ | | ✅ | | |

Use this to understand which team owns which requirements.

---

## Conformance Certification Process

Once you have a traceability matrix and evidence, how do you get certified?

**Process (CIR 2024/2981):**

1. **Self-Assessment** — Compile evidence and complete conformance matrix
2. **Supervisory Body Submission** — Submit evidence package to member state
3. **Conformity Assessment** — Independent body reviews evidence
4. **Certification Decision** — Approved or rejected
5. **Publication** — Certified wallet added to public list (CIR 2025/849)
6. **Annual Review** — Maintain conformance and respond to audits

**What They Look For:**

- ✅ Complete traceability matrix (every HLR covered)
- ✅ Evidence types appropriate to requirement type
- ✅ No conflicting evidence (if test says X, code agrees)
- ✅ Clear scope/profile (no ambiguity about what you claim)
- ✅ Security controls effective (threat model validated)
- ✅ Governance procedures documented (policies, incidents, reviews)

---

## Next Steps

1. **Review your requirements** using [Annex 2 CSV](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/hltr/high-level-requirements.csv)
2. **Create a Conformance Profile** documenting your scope
3. **Build a Traceability Matrix** linking ARF HLRs to your components
4. **Plan evidence collection** using the types above
5. **Identify gaps** — Which HLRs lack evidence?
6. **Execute testing** — Run test cases and collect evidence
7. **Prepare certification package** — Compile for supervisory body

---

## Key Takeaways

✅ **Separate normative (SHALL) from advisory (SHOULD)** — Both matter, but evidence types differ  
✅ **Know your scope level** — Wallet, provider, or ecosystem  
✅ **Build a traceability matrix** — Links requirements to evidence  
✅ **Collect evidence that matches requirement type** — Code tests, architecture reviews, policy docs  
✅ **Document your conformance profile** — Be clear about what you're claiming  
✅ **Manage change** — When ARF updates, update your matrix and evidence  

---

**Last Updated:** March 2026  
**ARF Alignment:** 2.8.0 (2026-02-02)
