# Governance to Control Mapping

## Purpose

This document maps **ARF governance requirements** (policies, oversight, certification) to **technical and organizational controls** you must implement to satisfy them.

Use this to understand:
- Which controls implement which governance requirements
- What evidence is needed to prove compliance
- How to organize your security program around ARF mandates
- Where governance and engineering responsibilities intersect

---

## Mapping Framework

A **governance requirement** is typically a policy mandate. A **control** is a concrete action, system, or process that implements the mandate.

### Example: Device Binding

**Governance Requirement (ARF Section 4.3.2, Topic 26):**
```
"Wallet SHOULD cryptographically bind credentials to the device"
(ARF 2.6.0+: Device binding is recommended, not mandatory)
```

**Technical Controls:**
```
Control 1: Device Key Derivation
  - Generate unique key pair per device during provisioning
  - Derive from device hardware (TEE, Secure Enclave)
  - Never export private key from device

Control 2: Credential Binding
  - Embed device public key in credential
  - Require device private key signature for presentation
  - Binding stored in credential metadata

Control 3: Presentation Verification
  - Service verifies device public key in credential
  - Service verifies device signature on presentation
  - Reject if device binding missing (if device binding is required for your profile)
```

**Evidence:**
```
- Architecture documentation (device key generation)
- Code review (key storage in secure hardware)
- Test cases (device binding acceptance/rejection)
- Threat model (attack scenarios and mitigations)
```

---

## Governance Domains

ARF governance requirements fall into **four domains**:

### Domain 1: Identity Verification & Issuance

**ARF Sections:** 4.2, 4.4, Topic 7–10

**Core Requirement:** Issuers must verify users' identities before issuing credentials.

**Sample Governance Requirements:**

| Requirement | Technical Control | Evidence |
|---|---|---|
| "Issuer SHALL verify user identity before issuing PID" (Topic 7) | User identification process (docs, biometrics, in-person) | Policy doc, enrollment logs |
| "PID SHALL contain authentic source data" (Topic 8) | Integration with government ID registers | System architecture, data integration tests |
| "Attestation Provider SHALL bind attestation to specific user" (Topic 9) | User database with unique identifiers | Database schema, access logs |
| "Credential lifecycle SHALL be managed" (Topic 10) | Expiration dates, revocation lists, status endpoints | Credential metadata, revocation status service |

### Domain 2: Wallet Security & Key Management

**ARF Sections:** 6.3, 6.5, Topic 26–30

**Core Requirement:** Wallets must protect user keys and credentials cryptographically.

**Sample Governance Requirements:**

| Requirement | Technical Control | Evidence |
|---|---|---|
| "Wallet SHALL protect private keys" (Topic 26) | Secure key storage (Secure Enclave, HSM, encrypted storage) | Arch doc, security review, key protection tests |
| "Wallet SHOULD support device binding" (Topic 26) | Device key derivation + credential binding | Arch doc, binding verification tests |
| "Keys SHALL use approved cryptographic algorithms" (Topic 27) | RS256, ECDSA, SHA-256+ | Cryptographic test vectors, code review |
| "Wallet SHALL handle key rotation" (Topic 28) | Key lifecycle management, versioning | Operational procedure, rotation tests |
| "Wallet SHALL prevent unauthorized key access" (Topic 29) | User authentication (PIN, biometric) before key use | UX tests, threat model, access control tests |

### Domain 3: User Authentication & Consent

**ARF Sections:** 6.5.3.3, Topic 40, Chapter 8

**Core Requirement:** Users must explicitly approve and authenticate credential sharing.

**Sample Governance Requirements:**

| Requirement | Technical Control | Evidence |
|---|---|---|
| "Wallet SHALL display credential request to user" (Topic 40) | UI showing requested claims, issuer, purpose | UI review, screenshots |
| "User SHALL authenticate before sharing" (Topic 40, Section 6.5.3.3) | Biometric, PIN, device unlock | UX tests, authentication logs |
| "Wallet SHALL NOT share without user approval" (Topic 40) | Explicit approval button; no auto-sharing | Code review, user acceptance tests |
| "Wallet SHALL be accessible to all users" (Topic 54, Chapter 8) | WCAG 2.1 AA compliance, keyboard nav, screen reader support | Accessibility audit, test report |

### Domain 4: Audit, Incident Response & Oversight

**ARF Sections:** Chapter 7, Topic 4–6

**Core Requirement:** Wallet providers must maintain audit trails and incident response procedures.

**Sample Governance Requirements:**

| Requirement | Technical Control | Evidence |
|---|---|---|
| "Wallet Provider SHALL maintain audit logs" (Topic 4) | Logging system capturing all credential issuance/sharing | Log architecture, retention policy, audit logs |
| "Logs SHALL include timestamp, user, action, result" (Topic 5) | Structured logging (JSON/CSV), time synchronization | Log format spec, sample logs |
| "Logs SHALL be protected from tampering" (Topic 5) | Immutable audit logs, central syslog server, write-once storage | Security review, log integrity tests |
| "Wallet Provider SHALL have incident response procedure" (Topic 6) | Documented procedure, CERT contact, escalation paths | Policy doc, incident response plan, training records |
| "Security incidents SHALL be reported to Supervisory Body" (Topic 6) | Notification procedure, SLA (e.g., 72 hours) | Policy doc, incident log showing compliance |

---

## Control Patterns by Governance Domain

### Pattern 1: Cryptographic Controls

**Governance Requirement:** "Private keys must be protected"

**Control Pattern:**
```
┌─ Key Storage Control
│  ├─ Requirement: Keys stored in secure hardware (TEE/Secure Enclave)
│  ├─ Implementation: Platform-specific secure storage APIs
│  ├─ Evidence: Code review, threat model
│  └─ Test: "Key can be used but not extracted"
│
├─ Key Access Control
│  ├─ Requirement: User must authenticate before key use
│  ├─ Implementation: Biometric/PIN required before crypto operation
│  ├─ Evidence: UX review, authentication logs
│  └─ Test: "Key operation fails without authentication"
│
└─ Key Lifecycle Control
   ├─ Requirement: Keys are rotated periodically
   ├─ Implementation: Scheduled key regeneration, version tracking
   ├─ Evidence: Operational procedures, rotation logs
   └─ Test: "Old key signature accepted, older key rejected"
```

### Pattern 2: User Consent Controls

**Governance Requirement:** "Users must approve credential sharing"

**Control Pattern:**
```
┌─ Consent UI Control
│  ├─ Requirement: Display what's being shared before user approval
│  ├─ Implementation: Modal dialog showing claims + issuer + service
│  ├─ Evidence: UX design, screenshots
│  └─ Test: "User can read request before approving"
│
├─ Authentication Control
│  ├─ Requirement: User must authenticate (prove device ownership)
│  ├─ Implementation: Biometric/PIN prompt before credential transfer
│  ├─ Evidence: Authentication flow design, UX tests
│  └─ Test: "Sharing fails if authentication cancelled"
│
└─ Denial Control
   ├─ Requirement: User must be able to deny sharing
   ├─ Implementation: "Deny" / "Cancel" button always available
   ├─ Evidence: UX design, user acceptance tests
   └─ Test: "Clicking Deny prevents credential sharing"
```

### Pattern 3: Audit Controls

**Governance Requirement:** "All credential operations must be logged"

**Control Pattern:**
```
┌─ Event Logging Control
│  ├─ Requirement: Log every credential issuance/presentation
│  ├─ Implementation: Event logging in backend, write to audit database
│  ├─ Evidence: Log architecture, sample logs
│  └─ Test: "Issuance creates log entry with all required fields"
│
├─ Data Integrity Control
│  ├─ Requirement: Logs cannot be modified or deleted
│  ├─ Implementation: Immutable append-only audit logs
│  ├─ Evidence: Database access controls, replication strategy
│  └─ Test: "Attempting to modify log entry fails"
│
├─ Access Control
│  ├─ Requirement: Only audit team can read logs
│  ├─ Implementation: Role-based access to audit database
│  ├─ Evidence: IAM configuration, access logs
│  └─ Test: "Non-audit user cannot read detailed logs"
│
└─ Retention Control
   ├─ Requirement: Logs retained per legal hold (e.g., 7 years)
   ├─ Implementation: Backup strategy, retention policy
   ├─ Evidence: Data retention policy, backup schedule
   └─ Test: "Logs available after 12 months AND after 3 years"
```

### Pattern 4: Governance Controls

**Governance Requirement:** "Incident response procedures must be documented and tested"

**Control Pattern:**
```
┌─ Policy Control
│  ├─ Requirement: Write incident response policy
│  ├─ Implementation: Document covering detection → triage → response → notification
│  ├─ Evidence: Policy document (ISO 27035 aligned)
│  └─ Verification: Policy review by security officer
│
├─ Process Control
│  ├─ Requirement: Define incident escalation and notification process
│  ├─ Implementation: Runbook with roles, timelines, notification contacts
│  ├─ Evidence: Incident response runbook, contact list, SLA doc
│  └─ Verification: Process review, documented in ISO 27001 risk treatment plan
│
├─ Training Control
│  ├─ Requirement: Team trained on incident response
│  ├─ Implementation: Annual training, documented attendance
│  ├─ Evidence: Training attendance logs, training materials
│  └─ Verification: Training certificates, quiz scores
│
└─ Exercise Control
   ├─ Requirement: Incident response plan tested annually
   ├─ Implementation: Tabletop exercise simulating a security incident
   ├─ Evidence: Exercise report, observed issues, corrective actions
   └─ Verification: Lessons learned documented, process improved
```

---

## Mapping by Role

Different roles own different controls:

### Security Engineer's Controls

**Responsible for:** Cryptography, key management, threat modeling

| ARF Requirement | Control | Implementation |
|---|---|---|
| "Keys protected" (Topic 26) | Key storage in Secure Enclave | Code: `SecureEnclaveKeyStore.store()` |
| "Algorithms approved" (Topic 27) | RS256 only (no deprecated algorithms) | Code: `cryptography.RSAPublicKey(2048)` |
| "Device binding" (Topic 26) | Device key generation + binding | Code: `DeviceBinding.create_binding()` |
| "Threat model" | Document threat scenarios | Doc: `threat-model-v2.md` |

### Backend Engineer's Controls

**Responsible for:** API endpoints, credential storage, audit logging, lifecycle management

| ARF Requirement | Control | Implementation |
|---|---|---|
| "Credential issuance" (Topic 7) | OpenID4VCI endpoint | Code: `/oauth2/token` endpoint |
| "Audit logging" (Topic 4) | Log all issuance events | Code: `audit_log.log_issuance(event)` |
| "Revocation" (Topic 10) | Revocation endpoint / status list | Code: `/revocation-status` endpoint |
| "Provider procedures" (Topic 6) | Incident response system | Code: Incident tracking, alerting |

### Mobile/Web Engineer's Controls

**Responsible for:** User authentication, consent UI, accessibility

| ARF Requirement | Control | Implementation |
|---|---|---|
| "Display request" (Topic 40) | Credential request UI | UI: `CredentialApprovalModal` component |
| "User authentication" (Topic 40) | Biometric/PIN prompt | Code: Platform biometric API calls |
| "Accessibility" (Topic 54) | WCAG 2.1 AA compliance | CSS: Semantic HTML, ARIA labels, keyboard nav |
| "Deny option" (Topic 40) | Always-available Cancel button | UI: Button at bottom of modal |

### Compliance/Governance Team's Controls

**Responsible for:** Policies, processes, certifications, oversight

| ARF Requirement | Control | Implementation |
|---|---|---|
| "Incident response plan" (Topic 6) | Document procedure | Doc: `incident-response-policy.md` |
| "Training" (Topic 6) | Annual training program | Process: Training schedule, attendance tracking |
| "Certification" (Topic 1) | Conformance profile, evidence package | Doc: Conformance matrix, test reports |
| "Supervisory coordination" (Topic 3) | Member state communication | Process: Quarterly status reports |

---

## Common Governance-to-Control Mappings

### Mapping 1: User Control & Consent

**Governance Driver:** ARF Section 1.1 principle—"Users control their identity"

```
ARF Statement:
  "Individuals shall have the ability to choose and keep track of their 
   identity, data and certificates which they share with third parties. 
   Anything which is not necessary to share will not be shared."

Translation to Controls:

┌─ Control: Selective Disclosure
│  ├─ Implementation: UI checkbox for each claim (name ✓, birthdate ✗)
│  ├─ Evidence: UX mockup, user acceptance tests
│  ├─ Test: "User can approve name but deny birthdate"
│  └─ Risk: User might not understand claim implications
│
├─ Control: Purpose Transparency
│  ├─ Implementation: Show service identity and why it needs claims
│  ├─ Evidence: UI text review, user study
│  ├─ Test: "User can identify requesting service"
│  └─ Risk: Service might misrepresent itself (spoofing attack)
│
└─ Control: Denial Right
   ├─ Implementation: Always-available Cancel/Deny option
   ├─ Evidence: UX design, code review
   ├─ Test: "Canceling prevents any credential transfer"
   └─ Risk: Accidentally tapping OK instead of Cancel
```

### Mapping 2: Security of Keys

**Governance Driver:** ARF Chapter 6 requirement—"Protect cryptographic keys"

```
ARF Statement:
  "Private keys used for credential signing SHALL be protected from 
   unauthorized access and SHALL NOT be exported from the secure storage."

Translation to Controls:

┌─ Control: Hardware-Backed Key Storage
│  ├─ Implementation: iOS Secure Enclave, Android TEE, or HSM
│  ├─ Evidence: Security architecture doc, key storage specification
│  ├─ Test: "Keys can be used but not extracted"
│  └─ Scope: All user-owned keys (identity, device, presentation proofs)
│
├─ Control: Authentication Before Use
│  ├─ Implementation: Biometric/PIN required before key operation
│  ├─ Evidence: UX design, code review of authentication integration
│  ├─ Test: "Key operation fails without valid authentication"
│  └─ Enforcement: Enforced by OS/hardware, not application
│
├─ Control: Backup/Recovery
│  ├─ Implementation: Cloud backup with user-controlled encryption
│  ├─ Evidence: Backup architecture, encryption key management doc
│  ├─ Test: "Backup encrypts keys; restore decrypts correctly"
│  └─ Risk: User loses backup key → Cannot recover account
│
└─ Control: Key Rotation
   ├─ Implementation: Annual key regeneration, versioning
   ├─ Evidence: Operational procedures, rotation schedule
   ├─ Test: "Old key signature still verified; older key signature rejected"
   └─ Scope: Affects issuer trust lists (new public keys published)
```

### Mapping 3: Audit & Accountability

**Governance Driver:** ARF Chapter 7 requirement—"Maintain oversight"

```
ARF Statement:
  "Wallet Providers SHALL maintain audit logs of all credential issuance 
   and presentation operations for the purpose of compliance verification 
   and incident investigation."

Translation to Controls:

┌─ Control: Comprehensive Logging
│  ├─ Implementation: Log issuance, presentation, revocation, support events
│  ├─ Minimum fields: Timestamp, user_id, operation, issuer/service, result, ip_address
│  ├─ Evidence: Log schema design, sample logs
│  ├─ Test: "Issuance creates correctly-formatted log entry"
│  └─ Challenge: Not logging too much (privacy) vs. too little (auditability)
│
├─ Control: Log Protection
│  ├─ Implementation: Immutable audit logs, centralized syslog, encrypted storage
│  ├─ Evidence: Log infrastructure architecture, encryption key management
│  ├─ Test: "Admin cannot modify existing log entries"
│  └─ Assumption: Assumes centralized logging (infrastructure requirement)
│
├─ Control: Retention Policy
│  ├─ Implementation: Logs retained 7 years (per legal hold)
│  ├─ Evidence: Data retention policy, backup schedule
│  ├─ Test: "Logs from 3 years ago are still accessible"
│  └─ Infrastructure: Requires long-term storage strategy
│
├─ Control: Access Control
│  ├─ Implementation: Only audit team + authorized admins can read logs
│  ├─ Evidence: IAM configuration, privileged access management
│  ├─ Test: "Developer cannot read full audit logs"
│  └─ Trade-off: Developer debugging vs. log confidentiality
│
└─ Control: Incident Reporting
   ├─ Implementation: Process for extracting evidence logs for incidents
   ├─ Evidence: Incident response runbook, reporting template
   ├─ Test: "Incident report includes relevant log entries"
   └─ Supervisory Integration: Reports go to Supervisory Body within 72 hours
```

---

## Mapping Template

Use this template to map governance requirements to controls for your wallet:

```markdown
## Governance Domain: [Domain Name]

### Requirement: [ARF Section/Topic]
"[ARF normative statement]"

### Controls (Your Implementation)

**Control 1: [Control Name]**
- **What it does:** [Functional description]
- **How it's implemented:** [Technical detail]
- **Who's responsible:** [Team/role]
- **Evidence artifact:** [Test report, code review, doc, etc.]
- **Test case:** [How you verify it works]
- **Risk/assumption:** [What could go wrong]

**Control 2: [Next control]**
- [Same structure]

### Mapping to Architecture Layers
- **Governance Layer:** [What policy drives this?]
- **Trust Layer:** [How does trust model support this?]
- **Infrastructure Layer:** [What system component?]
- **Protocol Layer:** [What API/protocol?]
- **Interop Layer:** [What standards?]

### Audit Evidence Summary
| Evidence Type | Status | Location |
|---|---|---|
| Code review | ✅ Complete | [PR #123] |
| Test report | ✅ Complete | [test-report-2024.pdf] |
| Architecture doc | ✅ Complete | [confluence link] |
| Threat model | ⚠️ In Progress | [jira ticket] |
```

---

## Governance-to-Control Gap Analysis

After mapping, identify gaps:

### Gap Type 1: Governance Without Control

```
ARF Requirement: "Wallet Provider SHALL maintain incident response procedures"
Your Current State: Policy written but not tested

Gap: Requirement is documented but not verified to work

Fix: 
  1. Conduct tabletop incident response exercise
  2. Document results and lessons learned
  3. Update procedure based on findings
```

### Gap Type 2: Control Without Governance

```
ARF Requirement: (none; just good security practice)
Your Current State: You implement hardware key protection but don't document it

Gap: Control exists but governance team doesn't know about it

Fix:
  1. Document security architecture
  2. Create test plan verifying key protection
  3. Add to conformance matrix
```

### Gap Type 3: Control But No Adequate Evidence

```
ARF Requirement: "Keys SHALL use approved algorithms" (Topic 27)
Your Current State: You use RS256 in code, but no test proves it

Gap: Control exists and is correct, but auditor can't verify

Fix:
  1. Create cryptographic test vector from NIST
  2. Run test and capture results
  3. Add test report to evidence package
```

---

## Conformance Governance Controls

Beyond wallet functionality, ARF requires governance controls for certification:

| Control | Purpose | Implementation |
|---|---|---|
| **Conformance Profile** | Document what you're claiming to conform to | Document: List topics, assurance level, features |
| **Traceability Matrix** | Link requirements to evidence | Spreadsheet: Req → Component → Test → Status |
| **Test Plan** | Define how you'll verify each requirement | Document: Test cases, scenarios, acceptance criteria |
| **Security Review** | Annual security assessment | Report: Threat model, control validation |
| **Incident Log** | Track security incidents and responses | Logs: Incidents, response times, corrective actions |
| **Change Management** | Control changes to certified wallet | Process: Change request, impact analysis, approval |
| **Staff Training** | Team trained on ARF and security procedures | Records: Training attendance, annual refresher |

---

## Tools for Governance-Control Mapping

### Lightweight (Spreadsheet)
- Google Sheets with tabs: Requirements → Controls → Evidence → Status
- Share with team, version control in Git
- Good for <100 requirements

### Mid-Range (Wiki/Docs)
- Confluence pages linked to requirements
- Markdown documents tracked in Git
- Searchable and linked cross-references

### Enterprise (Requirements Tools)
- DOORS, Jama, Requisite Pro
- Automated traceability reports
- Integration with testing tools

---

## Next Steps

1. **Review ARF governance requirements** ([ARF Chapters 1–3, 7](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md))
2. **Identify applicable governance domains** for your wallet
3. **Map each requirement to one or more controls**
4. **Assign responsibility** to teams (security, engineering, governance)
5. **Collect evidence** for each control
6. **Gap analysis** — What's missing?
7. **Remediate gaps** — Implement missing controls or document why not applicable
8. **Build conformance package** for certification

---

**Last Updated:** March 2026  
**ARF Alignment:** 2.8.0 (2026-02-02)
