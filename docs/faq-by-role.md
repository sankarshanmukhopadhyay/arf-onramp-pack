# Frequently Asked Questions (FAQ) by Role

This document answers common questions organized by role. Find your role below and jump to relevant questions.

---

## 📋 Quick Navigation

- [Policy & Program Leadership](#policy--program-leadership)
- [Architects & System Designers](#architects--system-designers)
- [Developers & Implementers](#developers--implementers)
- [Security & Compliance Teams](#security--compliance-teams)
- [Cross-Cutting Questions](#cross-cutting-questions)

---

## Policy & Program Leadership

### Q1: "What's the difference between the ARF and the EU Digital Identity Regulation?"

**A:** The **Regulation** (2024/910) is law. The **ARF** is technical guidance.

```
Regulation: "Member States SHALL offer digital wallets"  (WHAT to do)
ARF:        "Here's how to build one interoperably"     (HOW to do it)
```

You need both. The Regulation sets the mandate. The ARF describes how to implement it so wallets work across EU.

---

### Q2: "How long will implementation take?"

**A:** Typically 9–18 months from scratch to certified wallet:
- **Months 1–2:** Planning, architecture, design
- **Months 3–6:** Development (backend, app, integration)
- **Months 6–9:** Testing, security review, evidence compilation
- **Months 9–12:** Certification submission and audit
- **Months 12+:** Post-certification operations

**Variables:** Team size, complexity, vendor maturity, certification body speed.

**Recommendation:** Budget 12 months conservatively.

---

### Q3: "Should we build our own wallet or use an existing one?"

**A:** Three options:

| Option | Pros | Cons | Timeline |
|--------|------|------|----------|
| **Build** | Control, customization | High cost, long timeline | 12–18 months |
| **White-label** | Faster, lower cost | Limited customization | 3–6 months |
| **Integrate existing** | Lowest cost | Dependent on partner | 3–4 months |

**Recommendation:** For most member states, white-label or integration faster to certification. Build only if custom requirements essential.

---

### Q4: "How do we measure success?"

**A:** Key metrics:

- **Adoption:** % of target population with wallet
- **Usage:** # transactions per month
- **Interop:** % of cross-border flows working
- **Quality:** Certification approval, defect rates
- **Cost:** Cost per user, cost to certify
- **Satisfaction:** User satisfaction scores, NPS

**Recommendation:** Define target metrics in project charter. Review quarterly.

---

### Q5: "What's the cost of building a wallet?"

**A:** Rough estimates (EU context, varies widely):

| Component | Cost Range |
|-----------|------------|
| Architecture & design | €50–150K |
| Backend development | €200–400K |
| App development (iOS + Android) | €150–300K |
| Testing & QA | €100–200K |
| Security & compliance | €50–100K |
| Certification & audit | €30–50K |
| **Total** | **€580K–1.2M** |

**Variables:** Team location (EU vs. offshore), team size, tech stack, scope (national vs. EU-wide).

**Recommendation:** Get local bids. Consider phased approach (MVP first, extended features later).

---

### Q6: "What are the key member state coordination points?"

**A:** Four critical touchpoints:

1. **Trust Lists** — Who do we trust as issuers?
   - Coordinate with other member states
   - Maintain EU trust list

2. **Supervisory Body** — Who certifies wallets?
   - Designate your SB
   - Share certification criteria
   - Coordinate oversight

3. **Metadata Exchange** — How do services find wallets?
   - Register wallet in ecosystem
   - Share issuer metadata
   - Share RP endpoints

4. **Cross-Border Flows** — Do foreign wallets work in your country?
   - Accept foreign credentials
   - Coordinate on matching rules
   - Test interop flows

**Recommendation:** Join EDICG working groups. Participate in interop testing events.

---

### Q7: "How do we handle incident response?"

**A:** ARF requires incident response (CIR 2025/847):

```
Incident detected
    ↓
Triage (critical? what's affected?)
    ↓
Notify stakeholders (internal, supervisory body, EC)
    ↓
Investigate (what happened? why? how bad?)
    ↓
Remediate (fix the issue, restore service)
    ↓
Report (timeline: 72 hours to Supervisory Body)
    ↓
Learn (post-incident review, prevent recurrence)
```

**Recommendation:** Write incident response plan before going live. Run annual drills.

---

## Architects & System Designers

### Q1: "How do I map my system to ARF?"

**A:** Use the five-layer model from `docs/architecture-layer-map.md`:

```
Your System
    ↓
Layer 1: Governance    (policies, certification, oversight)
Layer 2: Trust         (crypto, identity binding, trust lists)
Layer 3: Infrastructure (wallet components, storage, lifecycle)
Layer 4: Protocol      (OpenID4VCI, OpenID4VP, data flows)
Layer 5: Interop       (standards, formats, cross-border)
    ↓
ARF
```

**Steps:**
1. Draw your system architecture
2. Overlay the five layers
3. Identify which ARF chapters apply to each layer
4. Document in architecture diagram

**Example:** "Backend API lives in Layers 3 & 4. Mobile app in Layers 3 & 4. Key storage in Layer 3."

---

### Q2: "Should device binding be required or optional?"

**A:** ARF 2.6.0+ says: **Recommended, not mandatory**

**Your choice:**

```
Option A: Require device binding (L2+)
  ✅ More secure (credential tied to device)
  ❌ More complex (device key generation, binding verification)
  ❌ More difficult for users (recovery harder)

Option B: Support but don't require
  ✅ Flexible (users can choose)
  ✅ Simpler implementation
  ❌ Slightly less secure if not used

Option C: Don't support
  ✅ Simplest
  ❌ Lower security for L2+
```

**Recommendation:** Support it for L2+. Whether users must enable it is policy choice.

---

### Q3: "How do we handle credential revocation?"

**A:** Two approaches (both supported by ARF):

| Approach | How | Pros | Cons |
|----------|-----|------|------|
| **Revocation endpoint** | Service queries issuer for each cred | Real-time, accurate | Network dependent, slower |
| **Status list** | Issuer publishes list of revoked credentials | Fast, cached | Slightly delayed (list publish lag) |

**Recommendation:** Support both. Use revocation endpoint for time-sensitive (L3). Use status list for high-volume services.

---

### Q4: "How many issuers should we support at launch?"

**A:** Depends on use case:

```
Government wallet:
  Minimum: PID (government ID) → 1 issuer
  Extended: EAA (education, professional) → 3–5 issuers
  Full: All government agencies → 10+ issuers

Private sector:
  Minimum: Single business case credential → 1 issuer
  Extended: Industry partnership → 5+ issuers
  Full: Cross-industry → 10+ issuers
```

**Recommendation:** Start with 1–2 issuers (PID + one EAA). Add more in v2.

---

### Q5: "How do we support multiple credential formats?"

**A:** ARF supports: SD-JWT, CWT, JSON

**Architecture approach:**

```
Credential Store (abstract)
    ├─ JWT Handler (SD-JWT)
    ├─ CBOR Handler (CWT)
    └─ Custom Handler (JSON or proprietary)

When issuing:
    1. Issuer specifies format
    2. Wallet stores in that format
    3. Wallet can re-serialize as needed

When presenting:
    1. Service requests format
    2. Wallet returns in requested format
    3. Service verifies using format-specific rules
```

**Recommendation:** Start with SD-JWT (most common). Add CWT in v2 if needed.

---

### Q6: "How do we design for accessibility?"

**A:** ARF Chapter 8 requires WCAG 2.1 AA:

```
Visual:     High contrast, readable fonts, no color-only UI
Motor:      Keyboard navigation, no complex gestures
Cognitive:  Clear language, simple workflows, good UX
Audio:      Captions for audio content
```

**Implementation:**
- Involve accessibility expert early
- Test with real users (blind, motor disabilities)
- Automated testing (axe, WAVE)
- Keyboard-only testing
- Screen reader testing

**Recommendation:** Budget 10–15% extra for accessibility. It's a conformance requirement, not optional.

---

### Q7: "What's the difference between Wallet Provider and Wallet Instance?"

**A:**

- **Wallet Provider** = Backend services (your servers)
  - API endpoints
  - Credential storage
  - Audit logging
  - Support and operations

- **Wallet Instance** = App on user's phone/browser
  - User interface
  - Local credential storage
  - Key management
  - User authentication

**Example:** "We run the Wallet Provider. Users download our Wallet Instance app."

---

## Developers & Implementers

### Q1: "Where do I start implementing?"

**A:** Follow this order:

```
Phase 1 (Backend):
  1. OpenID4VCI endpoint (issuing credentials)
  2. Credential storage (encrypted database)
  3. Audit logging (immutable logs)
  → Test with curl, Postman

Phase 2 (App):
  1. Credential reception (OpenID4VCI client)
  2. Local storage (Secure Enclave, encrypted DB)
  3. User authentication (biometric, PIN)
  → Test with test issuer

Phase 3 (Integration):
  1. OpenID4VP endpoint (presenting credentials)
  2. Service verification (signature check)
  3. User mapping (credential → user)
  → Test with test service

Phase 4 (Interop):
  1. Test with reference implementation
  2. Test with other wallets
  3. Test with real services
```

---

### Q2: "Which libraries should I use?"

**A:** Recommended by language:

| Language | OpenID4VCI Client | OpenID4VP Verifier | JWT/Signature |
|----------|---|---|---|
| **JavaScript/Node** | oauth4webapi, openid4vc | oauth4webapi | jsonwebtoken, jose |
| **Python** | authlib, pyOpenSSL | pyOpenSSL | PyJWT, cryptography |
| **Go** | oidc.v3, oauth2 | oidc.v3 | golang.org/x/crypto |
| **Java** | spring-security-oauth2, fosite | spring-security-oauth2 | java-jwt, nimbus-jose-jwt |
| **Swift** | AuthenticationServices (iOS) | AuthenticationServices | CryptoKit |
| **Kotlin** | OkHttp, Retrofit | OkHttp | JCA/Bouncy Castle |

**Recommendation:** Check community repos for reference implementations in your language.

---

### Q3: "How do I test my implementation?"

**A:** Layered testing approach:

```
Unit Tests:
  ├─ Credential serialization
  ├─ Signature generation/verification
  ├─ Key operations
  └─ Encryption/decryption

Integration Tests:
  ├─ Full OpenID4VCI flow
  ├─ Full OpenID4VP flow
  ├─ Credential verification
  └─ Database operations

Interop Tests:
  ├─ Reference wallet/issuer/service
  ├─ Third-party implementations
  ├─ Multiple credential formats
  └─ Cross-device flows

Security Tests:
  ├─ Key extraction (should fail)
  ├─ Signature forgery (should fail)
  ├─ Tampered credential (should fail)
  └─ Unauthorized access (should fail)
```

**Recommendation:** >80% unit test coverage. 100% integration test coverage of critical paths.

---

### Q4: "How do I handle errors?"

**A:** Common error scenarios:

| Scenario | ARF Section | How to Handle |
|----------|---|---|
| Invalid issuer | Trust list check | Reject credential, show error |
| Expired credential | Expiration field | Reject gracefully, suggest renewal |
| Revoked credential | Revocation endpoint | Reject, don't share |
| Invalid signature | Signature verification | Reject credential entirely |
| User cancels sharing | User consent | Don't send credential, reset UI |
| Network unavailable | Offline handling | Queue or cache, retry later |
| Service unreachable | Error handling | Display error, suggest retry |

**Recommendation:** Test error paths as thoroughly as success paths.

---

### Q5: "Where do I store sensitive data?"

**A:** By sensitivity level:

| Data | Storage | Why |
|------|---------|-----|
| **Private keys** | Secure Enclave (iOS), TEE (Android), HSM (server) | Never export, never in plaintext |
| **Credentials** | Encrypted local database | Encryption at rest required |
| **User auth tokens** | Memory (temporary) | Never in plaintext storage |
| **Audit logs** | Server-side database | Immutable, access controlled |
| **Metadata** | Local cache or server | Can be public |

**Recommendation:** Follow ARF Chapter 6 security requirements. Never store plaintext keys.

---

### Q6: "How do I implement device binding?"

**A:** Device binding architecture:

```
During credential issuance:
  1. Device generates key pair on Secure Enclave/TEE
  2. Wallet sends device public key to issuer
  3. Issuer embeds public key in credential

During credential presentation:
  1. Service sends presentation request
  2. Wallet creates response (normal)
  3. Wallet signs response with device private key
  4. Wallet sends both (response + device proof)
  5. Service verifies device signature using embedded public key
```

**Code example (pseudocode):**
```python
# Issuance
device_public_key = secure_enclave.generate_keypair()
cred_request.device_key = device_public_key
# Issuer returns credential with device_key embedded

# Presentation
response = create_presentation_response(credential)
device_proof = secure_enclave.sign(response)  # Private key never leaves SE
return { response, device_proof }

# Verification (service side)
issuer_pubkey = get_issuer_key(credential)
device_pubkey = credential.device_key
if verify_signature(response, device_proof, device_pubkey):
    accept credential
else:
    reject credential  # Device proof failed
```

---

### Q7: "How do I handle multiple credentials from different issuers?"

**A:** Credential store design:

```
Credentials
  ├─ PID (Government)
  │  ├─ Issuer: https://government.example/pid
  │  ├─ Key: [signing key]
  │  ├─ Expiration: 2027-03-20
  │  └─ Claims: name, birthdate, etc.
  │
  ├─ University Diploma (University)
  │  ├─ Issuer: https://university.example/diploma
  │  ├─ Key: [signing key]
  │  ├─ Expiration: 2030-01-01
  │  └─ Claims: degree, field, etc.
  │
  └─ [More credentials...]

Per-issuer operations:
  • Different refresh schedules
  • Different revocation checks
  • Different expiration dates
  • Different claim structures
```

**Implementation:**
```python
class Credential:
    issuer: URL
    format: str  # "jwt", "cwt", etc.
    data: bytes  # Signed credential
    metadata: {
        issuer_key: PublicKey,
        expiration: datetime,
        revocation_status: str,
        created_at: datetime
    }

credentials: List[Credential] = []

def add_credential(cred: Credential):
    # Verify issuer in trust list
    # Verify signature
    # Store (encrypted)

def get_for_presentation(service: URL) -> List[Credential]:
    # Filter by service request
    # Check expiration
    # Check revocation
    # Return matching credentials
```

---

## Security & Compliance Teams

### Q1: "How do I design a threat model for a wallet?"

**A:** Follow STRIDE methodology:

```
For each asset/flow, identify threats:

S - Spoofing:  Can attacker impersonate user/issuer/service?
T - Tampering: Can attacker modify credentials/keys/logs?
R - Repudiation: Can user deny actions they took?
I - Info Disclosure: Can attacker read sensitive data?
D - Denial of Service: Can attacker prevent wallet use?
E - Elevation: Can attacker escalate privileges?

Example: Private Key
  S: Attacker generates fake key (mitigate: Secure Enclave)
  T: Attacker modifies key (mitigate: Immutable SE)
  R: N/A (not an actor)
  I: Attacker extracts key (mitigate: No export APIs)
  D: Attacker prevents key use (mitigate: Backup key)
  E: App process escalates to SE (mitigate: Hardware isolation)
```

**Recommendation:** Involve architects. Use threat modeling tools (Microsoft Threat Modeling Tool, ThreatDragon).

---

### Q2: "What security controls are required for each assurance level?"

**A:** From ARF Chapter 6:

| Control | L0 | L1 | L2 | L3 |
|---------|----|----|----|----|
| Private key protection | ✓ | ✓ | ✓ | ✓ |
| User authentication | ✓ | ✓ | ✓✓ | ✓✓ |
| Device binding | - | - | ✓ | ✓ |
| Signature verification | ✓ | ✓ | ✓ | ✓ |
| Audit logging | - | ✓ | ✓ | ✓ |
| Encryption at rest | - | ✓ | ✓ | ✓ |
| Revocation checking | - | ✓ | ✓ | ✓ |

**Key difference:** L2 requires device binding + strong user auth. L3 requires highest crypto standards + continuous monitoring.

---

### Q3: "How do I plan evidence collection?"

**A:** For each control, define:

```
Control: Device binding
  ├─ ARF Ref: Topic 26, Section 4.3.2
  ├─ Requirement: "Wallet SHALL bind credentials to device"
  ├─ Your Implementation: Generate key in Secure Enclave
  ├─ Test Case: "Credential on Device A should fail on Device B"
  ├─ Evidence: 
  │  ├─ Code review (Secure Enclave API usage)
  │  ├─ Test results (binding test passed)
  │  ├─ Architecture doc (device binding flow)
  │  └─ Security review (threat model validated)
  └─ Status: ✅ PASS

Control: Audit logging
  ├─ ARF Ref: Topic 4
  ├─ Requirement: "Wallet Provider SHALL maintain audit logs"
  ├─ Your Implementation: PostgreSQL audit table
  ├─ Test Case: "Issuance creates log entry with timestamp, user, operation"
  ├─ Evidence:
  │  ├─ Log schema (documented)
  │  ├─ Sample logs (real logs from testing)
  │  ├─ Access control (audit team only read)
  │  └─ Retention policy (7 year retention)
  └─ Status: ✅ PASS
```

**Recommendation:** Build traceability matrix as you develop. Don't wait until certification audit.

---

### Q4: "What should I test for security?"

**A:** Security test plan:

| Area | Test Case | Expected Result |
|------|-----------|---|
| **Key Storage** | Try to extract key | FAIL (no export) |
| **Key Storage** | Use key without auth | FAIL (auth required) |
| **Signature** | Verify valid signature | PASS |
| **Signature** | Verify tampered signature | FAIL |
| **Revocation** | Accept non-revoked cred | PASS |
| **Revocation** | Accept revoked cred | FAIL |
| **Encryption** | Decrypt with correct key | PASS |
| **Encryption** | Decrypt with wrong key | FAIL |
| **Audit Logs** | Read as compliance team | PASS |
| **Audit Logs** | Read as non-admin user | FAIL |
| **Incident Response** | Notify within 72 hours | PASS |

---

### Q5: "How do I assess privacy risks?"

**A:** Privacy Impact Assessment (PIA):

```
Data Collection:
  ✓ What data is collected?
  ✓ Why is it needed?
  ✓ Is it minimal (privacy by design)?

Data Processing:
  ✓ Who has access?
  ✓ How long is it retained?
  ✓ Is it encrypted?
  ✓ Are there access logs?

Data Sharing:
  ✓ Is data shared with third parties?
  ✓ Is consent obtained?
  ✓ Can users revoke consent?
  ✓ Are there data processing agreements?

User Rights:
  ✓ Can users access their data?
  ✓ Can users delete their data?
  ✓ Can users export their data?
  ✓ Is there a right to be forgotten?
```

**ARF Requirements:** Data minimization, purpose limitation, user consent, retention limits.

---

### Q6: "How do I prepare for a security audit?"

**A:** Audit preparation checklist:

- [ ] All code reviewed (no obvious vulns)
- [ ] All tests passing (>80% coverage)
- [ ] All dependencies up to date
- [ ] Security scan clean (no critical vulnerabilities)
- [ ] Threat model complete
- [ ] Incident response tested (annual drill)
- [ ] Audit logs configured and tested
- [ ] Access controls working
- [ ] Backup/recovery tested
- [ ] Documentation complete and clear

**Recommendation:** Plan 4 weeks before audit for preparation.

---

## Cross-Cutting Questions

### Q1: "Where do I find the authoritative ARF?"

**A:** Official sources:

- **ARF Main Document:** https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md
- **Annexes (High-Level Requirements):** https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/annexes
- **Discussion Topics:** https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/discussion-topics
- **Technical Specifications:** https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/technical-specifications

**Authoritative = The upstream documents, not this on-ramp.**

---

### Q2: "What's the difference between 'SHALL' and 'SHOULD'?"

**A:** RFC 8174 definitions (used throughout ARF):

- **SHALL / MUST** = Mandatory. You must implement.
- **SHOULD / RECOMMEND** = Strongly advised. Document if you don't.
- **MAY / OPTIONAL** = Truly optional. Your choice.

**Example:**
```
"Wallet SHALL verify issuer signature"  → MUST implement
"Wallet SHOULD support device binding"  → Either do it OR document why not
"Wallet MAY support biometric auth"     → Your choice
```

---

### Q3: "How do I stay synchronized with upstream ARF changes?"

**A:** Use `docs/upstream-alignment-guide.md`:

```
Monthly:
  • Check [GitHub releases](https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/releases)

Quarterly (Feb, May, Aug, Nov):
  • Run quarterly sync checklist
  • Assess impact of changes
  • Plan updates if needed
  • Update your documentation

When ARF major version changes:
  • Major effort (maybe 4–8 weeks)
  • Use change impact assessment template
  • Update traceability matrix
  • Re-test affected components
```

---

### Q4: "What's the conformance profile and why do I need one?"

**A:** A **Conformance Profile** states:

```
"Our wallet implements:
  - ARF version 2.8.0
  - Assurance level L2
  - Credentials: PID + university diploma
  - Flows: Remote same-device + cross-device
  - Device binding: Recommended (implemented)
  - 45 of 55 HLRs apply
  - 0 HLRs excluded
  - High-level requirements mapping: [traceability matrix]
"
```

**Why:**
- Clarifies scope (you don't implement everything)
- Defines what to test
- Helps auditors understand claims
- Enables certification

**Recommendation:** Write on Day 1. Update as scope changes.

---

### Q5: "Where can I find glossary definitions?"

**A:** Three sources:

1. **ARF Annex 1** (Official) → https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/tree/main/docs/annexes
2. **On-Ramp Quick Reference** (100+ terms) → `docs/quick-reference.md`
3. **This FAQ** (Common terms in context)

**Quick lookups:** Use on-ramp quick reference (often faster).
**Authoritative:** Use ARF Annex 1.

---

### Q6: "What if I find an error in the ARF?"

**A:** Report to upstream:

1. **Open GitHub issue:** https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/issues
2. **Describe the error** (section, what's wrong, suggested fix)
3. **EDICG team** will review and respond

**Do NOT:** Just skip the requirement. ARF is maintained by EU authorities. Report it.

---

### Q7: "Where can I get help?"

**A:** By question type:

| Question | Where to Ask |
|----------|---|
| ARF interpretation | ARF GitHub issues |
| Implementation details | This on-ramp + ARF technical specs |
| Certification process | Your supervisory body |
| Standard specs (OpenID, ISO) | Official specification documents |
| Member state coordination | EDICG meetings |
| Emergency (security incident) | Supervisory body, then EC |

**Recommendation:** Try searching past issues/discussions first. You're likely not the first to ask.

---

## Document Version & Updates

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03 | Initial release |

Last Updated: March 2026  
ARF Alignment: 2.8.0 (2026-02-02)
