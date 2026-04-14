# Reading Path: Security, Privacy & Assurance Team

**For:** Security architects, privacy officers, compliance auditors, QA engineers, security testers  
**Focus:** Threat models, security controls, privacy requirements, assurance evidence, certification  
**Time:** 60–90 minutes to read; 4–6 hours with threat modeling and control design  
**Outcome:** Understand security architecture, design threat models, plan evidence collection, prepare for certification

---

## Before You Start

**You should know:**
- Threat modeling (STRIDE, attack trees)
- ISO 27001 / 27002 controls
- Cryptography and why it matters
- Privacy requirements (GDPR, privacy by design)
- Compliance and audit processes

**You might skip if:**
- You're building APIs (see [Implementer path](./reading-path-implementer.md))
- You're not responsible for security/compliance
- Your organization outsources security entirely

---

## Key Concepts for Security & Assurance

### 1. Security Is Layered

ARF requires security at multiple levels:

```
┌─ Layer 1: Cryptographic Security
│  ├─ Private keys protected (Secure Enclave, HSM)
│  ├─ Signatures verified (no tampering)
│  └─ Data encrypted at rest and in transit
│
├─ Layer 2: Access Control
│  ├─ User authentication (biometric, PIN)
│  ├─ Device authentication (device binding)
│  └─ Authorization (which credentials to which services)
│
├─ Layer 3: Audit & Accountability
│  ├─ Audit logs of all operations
│  ├─ Incident detection and response
│  └─ Forensic evidence for investigation
│
└─ Layer 4: Data Protection
   ├─ Data minimization (share only what's needed)
   ├─ Privacy controls (consent, revocation)
   └─ Retention limits (delete when no longer needed)
```

**Your job:** Design and verify each layer.

### 2. Assurance Levels Drive Security Design

ARF defines four assurance levels. Each requires different controls:

| Level | Risk Profile | Use Case | Security Baseline |
|-------|-------|----------|---|
| **L0** | Low | Non-sensitive | Basic authentication |
| **L1** | Medium | Standard services | + Credential verification |
| **L2** | High | Sensitive services | + Device binding, + User authentication |
| **L3** | Very High | High-value transactions | + Highest crypto standards |

**Your job:** Map security requirements to your assurance level.

### 3. Threat Model Is Your Blueprint

Before implementing security, model threats:

```
Asset: User's private key
Threat: Malware on device extracts key
Impact: Attacker can impersonate user
Mitigation: Store key in Secure Enclave (extracted keys fail)
Control: Key storage in Secure Enclave
Test: Attempt key extraction (should fail)
```

**Your job:** Create comprehensive threat model.

### 4. Privacy & Security Are Linked

ARF privacy requirements (Chapter 6.4):
- Data minimization (don't collect what you don't need)
- Consent before sharing (user approves each request)
- Purpose limitation (only use data for stated purpose)
- Retention limits (delete after use)

**Your job:** Bake privacy into every control.

### 5. Evidence Is Everything

Certification requires proof that controls work:

| Control | Evidence Type | Example |
|---------|---|---|
| "Keys protected" | Code review + test | `SecureEnclave.generate()` + test showing extraction fails |
| "Audit logs" | Logs + access controls | 1 MB log file + audit showing only compliance team can read |
| "Incident response" | Process doc + incident logs | Policy doc + 3 example incidents with response times |
| "User authentication" | UX test + biometric test | Screenshots + biometric test results |

**Your job:** Plan evidence collection throughout development.

---

## Recommended Reading Order

### Section 1: ARF Security Overview (15 min)

**Read:** [ARF Explained](../arf-explained.md) → "Assurance Levels" section

**Then:** [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → **Chapter 6** (Security, Integrity, Accessibility)

**Key Questions to Answer:**
- [ ] What are the assurance levels (L0–L3)?
- [ ] What security controls does each level require?
- [ ] What is the threat model?
- [ ] What cryptographic algorithms are mandated?

---

### Section 2: Security Controls by Domain (15 min)

**Read:** [Governance to Control Mapping](../governance-to-control-mapping.md) → Full document

**Focus on:**
- Cryptographic controls
- Key management controls
- User authentication controls
- Audit and incident response controls

**Key Questions to Answer:**
- [ ] What does "private key protection" actually mean?
- [ ] How do device binding controls work?
- [ ] What audit logging is required?
- [ ] What incident response procedures are needed?

---

### Section 3: Privacy Requirements (10 min)

**Read:** [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → **Chapter 6, Section 6.4** (Privacy)

**Also:** [Governance to Control Mapping](../governance-to-control-mapping.md) → "User Consent Controls" pattern

**Key Questions to Answer:**
- [ ] What is data minimization and how is it enforced?
- [ ] How is user consent obtained and recorded?
- [ ] What data retention limits apply?
- [ ] How do users revoke consent?

---

### Section 4: Conformance & Certification (15 min)

**Read:** [Conformance Interpretation Companion](../conformance-interpretation-companion.md) → Full document

**Focus on:**
- Conformance categories
- Conformance profiles
- Traceability matrix
- Certification process

**Also:** [CIR 2024/2981](https://data.europa.eu/eli/reg_impl/2024/2981/oj) → Certification requirements (executive summary)

**Key Questions to Answer:**
- [ ] What is a conformance profile?
- [ ] What goes in a traceability matrix?
- [ ] What evidence is needed for certification?
- [ ] What is the certification process timeline?

---

### Section 5: Threat Modeling & Risk Assessment (15 min)

**Read:** [Governance to Control Mapping](../governance-to-control-mapping.md) → "Cryptographic Controls" and "Audit Controls" patterns

**Then:** Download [STRIDE cheat sheet](https://owasp.org/www-community/attacks/STRIDE_Classification) for threat modeling reference

**Key Questions to Answer:**
- [ ] What are the main threat scenarios?
- [ ] How does your architecture mitigate each threat?
- [ ] What residual risks exist?
- [ ] How are risks accepted or mitigated?

---

## Deep-Dive Topics (Optional)

### If You're Designing Wallet Security Architecture

**Additional Reading:**
1. [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → Chapter 6 in detail
2. [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) → Risk management
3. [ISO 27005](https://www.iso.org/standard/80585.html) → Risk assessment (if accessible)
4. [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Model_Info_and_Common_Approaches) → Practical approach

**Topics to Cover:**
- Threat modeling methodology (STRIDE, attack trees)
- Risk quantification (likelihood × impact)
- Control selection and prioritization
- Risk acceptance criteria
- Residual risk documentation

---

### If You're Building Security Test Suite

**Additional Reading:**
1. [Conformance Interpretation Companion](../conformance-interpretation-companion.md) → "Evidence Types & Collection" section
2. [NIST Cryptographic Test Vectors](https://csrc.nist.gov/projects/cryptographic-algorithm-validation-program/) → Test cases
3. [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) → Security testing methodology

**Topics to Cover:**
- Cryptographic test vectors
- Key extraction tests
- Authentication bypass tests
- Audit log integrity tests
- Incident response drills

---

### If You're Preparing for Certification Audit

**Additional Reading:**
1. [CIR 2024/2981](https://data.europa.eu/eli/reg_impl/2024/2981/oj) → Full certification regulation
2. [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → Chapter 7 (Conformance & Certification)
3. ISO 27001 audit checklists (sample format)

**Topics to Cover:**
- Evidence collection and organization
- Traceability matrix completion
- Audit interview preparation
- Non-conformance remediation
- Continuous compliance monitoring

---

### If You're Designing Privacy Controls

**Additional Reading:**
1. [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → Chapter 6, Section 6.4 (Privacy)
2. [GDPR Regulation](https://eur-lex.europa.eu/eli/reg/2016/679/oj) → Chapters 3–4 (User Rights & Consent)
3. [Privacy by Design Framework](https://www.ipc.on.ca/wp-content/uploads/Resources/7foundationalprinciples.pdf) → Design principles

**Topics to Cover:**
- Data minimization design
- Privacy impact assessment
- Consent mechanisms
- Data subject rights (access, deletion, portability)
- Breach notification procedures

---

## Security Architecture Design

### Exercise 1: Threat Model Development

**Objective:** Identify threats and design mitigations.

**Steps:**

1. **Identify assets** (what you're protecting)
   - Private keys
   - User credentials
   - Audit logs
   - User personal data

2. **Identify threats** (how could they be compromised?)
   ```
   Asset: Private Key
   Threats:
     - Malware on device steals key
     - Attacker with physical access extracts key
     - Cloud backup stolen or hacked
     - Developer accidentally logs key
   ```

3. **Design mitigations** (controls to prevent threat)
   ```
   Threat: Malware steals key
   Mitigations:
     - Store key in Secure Enclave (hardware isolation)
     - Require user authentication before key use (biometric/PIN)
     - No key export APIs available
     - Audit logs of all key operations
   ```

4. **Evaluate mitigations**
   ```
   Likelihood (before): High (malware prevalent)
   Likelihood (after): Low (Secure Enclave very hard to compromise)
   Impact: Critical (key compromise = user impersonation)
   Risk Level: Medium (Low likelihood × Critical impact)
   ```

5. **Document** in threat model

**Output:** Threat model document (STRIDE table or attack tree)

---

### Exercise 2: Control Selection & Mapping

**Objective:** Map ARF requirements to specific controls.

**Template:**

```
ARF Requirement: "Wallet SHALL protect private keys from unauthorized access"
Assurance Level: L2 (for this analysis)

Control 1: Hardware Key Storage
  ├─ Description: Keys stored in Secure Enclave (iOS) or TEE (Android)
  ├─ Implementation: Use platform key generation APIs
  ├─ Test: Attempt key extraction (should fail)
  ├─ Evidence: Code review + security test report
  └─ Status: Implemented ✅

Control 2: User Authentication Before Key Use
  ├─ Description: Biometric or PIN required before signing
  ├─ Implementation: Biometric API + device unlock integration
  ├─ Test: Key operation fails without authentication
  ├─ Evidence: UX test screenshots + code review
  └─ Status: Planned 📋

Control 3: Audit Logging
  ├─ Description: All key operations logged with timestamp, user, operation
  ├─ Implementation: Event logging in backend + audit database
  ├─ Test: Verify log entry created for each operation
  ├─ Evidence: Log format spec + sample logs
  └─ Status: Implemented ✅

Control 4: Key Rotation
  ├─ Description: Annual key regeneration
  ├─ Implementation: Scheduled job, version tracking
  ├─ Test: Old key still works, older key rejected
  ├─ Evidence: Operational procedure + rotation logs
  └─ Status: Planned 📋
```

**Output:** Controls matrix

---

### Exercise 3: Privacy Impact Assessment

**Objective:** Identify privacy risks and design privacy controls.

**Steps:**

1. **Map data flows**
   ```
   User data: Name, birthdate, address
   Collection: Government issues PID credential
   Processing: Wallet stores and presents
   Sharing: User shares with services
   Retention: Depends on service
   ```

2. **Identify privacy risks**
   ```
   Risk 1: Service gets more data than needed
   Risk 2: User doesn't know what data was shared
   Risk 3: Service keeps data longer than needed
   Risk 4: Issuer tracks user credentials
   ```

3. **Design privacy controls**
   ```
   Risk: Service gets more data than needed
   Control: Selective disclosure (user chooses which claims to share)
   Implementation: Checkbox UI per claim
   Test: User can approve name but deny birthdate
   
   Risk: User doesn't know what was shared
   Control: Share receipt (record of shared data)
   Implementation: Log in wallet showing timestamp, service, claims shared
   Test: User can access history of shares
   
   Risk: Service keeps data too long
   Control: Retention limits (contract with service)
   Implementation: Data deletion after service period
   Test: Data deleted on schedule
   
   Risk: Issuer tracks users
   Control: Unlinkable credentials (issuer can't correlate uses)
   Implementation: Different signature per use (requires architecture change)
   Test: Two credentials from same issuer have different signatures
   ```

4. **Document** in privacy impact assessment

**Output:** Privacy Impact Assessment (PIA) document

---

## Security & Privacy Controls Checklist

### Cryptographic Controls
- [ ] Private keys generated in secure hardware (Secure Enclave, TEE, HSM)
- [ ] Private keys never exported or accessible to application code
- [ ] Public keys distributed via trust lists or certificates
- [ ] Algorithms: RS256 or ECDSA (no deprecated algorithms)
- [ ] Key lengths: 2048-bit RSA or 256-bit ECDSA (or stronger)
- [ ] Symmetric encryption: AES-256 for data at rest
- [ ] Hash function: SHA-256 or stronger

### Key Management Controls
- [ ] Key generation documented and tested
- [ ] Key backup encrypted and stored separately
- [ ] Key rotation process defined and scheduled
- [ ] Compromise response plan exists
- [ ] Key lifecycle (creation, use, retirement) tracked

### Authentication & Access Controls
- [ ] User authentication required before credential sharing (biometric, PIN, pattern)
- [ ] Device authentication (device binding) recommended for L2+
- [ ] Multi-factor authentication for high-risk operations
- [ ] Account lockout after failed authentication attempts
- [ ] Session management (timeout, revocation on logout)

### Audit & Monitoring Controls
- [ ] All credential operations logged (issuance, presentation, revocation)
- [ ] Log entries include: timestamp, user ID, operation, service, result, IP address
- [ ] Logs protected from tampering (immutable, access-controlled)
- [ ] Logs retained per legal hold (e.g., 7 years)
- [ ] Real-time alerting for suspicious activities
- [ ] Regular audit log reviews (monthly/quarterly)

### Incident Response Controls
- [ ] Incident response policy documented
- [ ] Incident types defined (data breach, service outage, key compromise)
- [ ] Escalation procedures clear (who to notify, when, how)
- [ ] Notification timeline: 72 hours to Supervisory Body
- [ ] Incident log maintained (date, type, severity, response, outcome)
- [ ] Annual incident response drill/exercise

### Data Protection Controls
- [ ] Data minimization: Only collect necessary data
- [ ] Consent management: Explicit approval before sharing
- [ ] Purpose limitation: Only use data for stated purpose
- [ ] Retention limits: Delete data after service period
- [ ] User rights: Access, deletion, portability on request
- [ ] Privacy by design: Privacy considered in all design decisions

### Accessibility Controls
- [ ] WCAG 2.1 AA compliance
- [ ] Keyboard navigation support (no mouse-only UI)
- [ ] Screen reader compatibility (semantic HTML, ARIA labels)
- [ ] Color contrast ratios meet standards
- [ ] No complex gestures required
- [ ] Sufficient time for interactions (no time-based auto-actions)

---

## Certification Evidence Collection

### For Each Control, Collect:

| Evidence Type | Example | Collection Method |
|---|---|---|
| **Architecture Doc** | "Keys stored in Secure Enclave per iOS specification" | Design review meeting |
| **Code Review** | Approved PR showing `SecKeyCreateRandomKey()` | Peer code review |
| **Test Report** | "Key extraction test: FAIL (as expected)" | Automated security test |
| **Threat Model** | Risk assessment with mitigations | Threat modeling session |
| **Policy Doc** | "Incident Response Policy v1.2" | Policy authoring |
| **Procedure Doc** | "Key Rotation Procedure" with steps | Operational documentation |
| **Training Records** | "Team trained on security on 2024-03-15" | Training attendance log |
| **Incident Logs** | "Incident 2024-001: Malware detection and response" | Real incident or drill |

---

## Certification Readiness Checklist

Before submitting for certification:

### Documentation Complete
- [ ] Conformance profile documented (scope, assurance level)
- [ ] Traceability matrix 100% complete (all HLRs covered)
- [ ] Architecture document with diagrams
- [ ] Threat model with mitigations and residual risks
- [ ] Security test plan and results
- [ ] Privacy impact assessment
- [ ] Incident response procedures
- [ ] Staff training records

### Testing Complete
- [ ] Unit tests all critical security functions
- [ ] Integration tests for data flows
- [ ] Security tests (key extraction, auth bypass, etc.)
- [ ] Interoperability tests with reference implementation
- [ ] Accessibility tests (WCAG 2.1 AA)
- [ ] Performance tests (load, latency)

### Controls Verified
- [ ] Security review by independent auditor (recommended)
- [ ] Penetration test of critical components (recommended)
- [ ] Incident response drill executed
- [ ] Audit logs tested and validated

### No Major Gaps
- [ ] No unimplemented required features
- [ ] No unresolved security findings
- [ ] No unmitigated risks above accepted threshold
- [ ] All evidence artifacts present and linked in traceability matrix

---

## Common Security Challenges

### Challenge 1: "Device Binding is Complex"

**ARF Status:** Recommended (not mandatory) in 2.6.0+

**Your Decision:**
```
Option A: Implement device binding
  ✅ Enhanced security
  ❌ More complex implementation, testing, and user support

Option B: Don't implement, document why
  ✅ Simpler, faster to market
  ❌ Security slightly lower
  
Document your choice in conformance profile
```

---

### Challenge 2: "Balancing Usability with Security"

**Common Conflicts:**
```
Security: Require biometric + PIN + 2FA before sharing
Usability: Takes 30 seconds, user clicks "deny"

Security: Store all credential sharing history
Usability: Overwhelming for users, privacy concern

Security: Frequent key rotation (monthly)
Usability: Causes trust issues, crashes
```

**Solution:** Risk-based trade-offs per assurance level
```
L0: Minimal security, high usability
L1: Standard security, good usability
L2: Strong security, acceptable usability trade-off
L3: Highest security, usability secondary
```

---

### Challenge 3: "Privacy & Security Conflict"

**Example:**
```
Privacy: Minimize data collection
Security: Log all operations for audit

Solution: Log operations but delete personal data after audit period
  - Log timestamp, user ID, service, operation
  - Don't log actual shared claims
  - Delete logs after retention period
```

---

## Key Resources

### Security Standards
- **ISO 27001/27002:** Information security management
- **NIST Cybersecurity Framework:** Risk-based approach
- **OWASP:** Security best practices
- **FIPS 140-2:** Cryptographic module validation

### Privacy Standards
- **GDPR (Regulation 2016/679):** EU data protection
- **Privacy by Design Principles:** Privacy impact assessment
- **ISO 27701:** Privacy management

### ARF Documentation
- **ARF Chapter 6:** https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md (Security & Privacy)
- **CIR 2024/2981:** https://data.europa.eu/eli/reg_impl/2024/2981/oj (Certification)
- **Governance to Control Mapping:** [../governance-to-control-mapping.md](../governance-to-control-mapping.md)

### Tools & Frameworks
- **STRIDE Threat Modeling:** OWASP methodology
- **Attack Trees:** Attack tree modeling tool
- **Risk Assessment Tools:** ISO 27005 templates
- **Security Test Frameworks:** OWASP, NIST test vectors

---

## Next Steps

1. **Review ARF security requirements** (Chapter 6)
2. **Determine your assurance level** (L0–L3)
3. **Create threat model** for your wallet
4. **Design security controls** to mitigate threats
5. **Plan evidence collection** (tests, logs, reviews)
6. **Implement security tests** in CI/CD
7. **Conduct security review** (internal or external)
8. **Document conformance** using traceability matrix
9. **Prepare for certification audit**

---

**Last Updated:** March 2026  
**ARF Alignment:** 2.8.0 (2026-02-02)
