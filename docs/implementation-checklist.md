# Implementation Checklist & Roadmap

## Purpose

This document provides **executable checklists** for different implementation scenarios. Use these to:
- Plan your project phases
- Track progress
- Ensure no critical items are missed
- Coordinate across teams

---

## Pre-Implementation: Discovery & Planning (Weeks 1–4)

### Project Setup

- [ ] **Define wallet scope**
  - [ ] Assurance level target (L0, L1, L2, L3)
  - [ ] Supported credential types (PID, mDL, custom)
  - [ ] Authentication modes (proximity, remote same-device, remote cross-device)
  - [ ] Device binding requirement (mandatory, recommended, optional)
  - Document in: `WALLET_CONFORMANCE_PROFILE.md`

- [ ] **Designate roles & responsibilities**
  - [ ] Program manager / Product owner
  - [ ] Solution architect
  - [ ] Security architect
  - [ ] Backend lead
  - [ ] Mobile/web lead
  - [ ] QA lead
  - [ ] Compliance/Legal
  - Document in: `TEAM_STRUCTURE.md`

- [ ] **Establish governance model**
  - [ ] Wallet operator (government, private, hybrid)
  - [ ] Certification path (member state, independent)
  - [ ] Incident response procedures
  - [ ] Data handling and privacy policy
  - Document in: `GOVERNANCE_MODEL.md`

### ARF Learning & Planning

- [ ] **All team reads foundational docs**
  - [ ] README.md (10 min)
  - [ ] docs/arf-explained.md (30 min)
  - [ ] docs/quick-reference.md (bookmark for lookup)

- [ ] **Each role reads relevant path**
  - [ ] Policy/Leadership: reading-path-policy-leadership.md
  - [ ] Architects: reading-path-architect.md
  - [ ] Engineers: reading-path-implementer.md
  - [ ] Security: reading-path-security-assurance.md

- [ ] **Architecture team completes design phase**
  - [ ] Map to five ARF layers (using architecture-layer-map.md)
  - [ ] Complete architecture layer design exercises
  - [ ] Document system architecture (diagrams, component descriptions)
  - [ ] Identify integration points
  - Document in: `ARCHITECTURE.md`

- [ ] **Security team completes threat modeling**
  - [ ] Read governance-to-control-mapping.md
  - [ ] Create threat model (STRIDE or attack trees)
  - [ ] Map threats to security controls
  - [ ] Identify residual risks and acceptance
  - [ ] Define security architecture (cryptography, key management, audit)
  - Document in: `THREAT_MODEL.md` and `SECURITY_ARCHITECTURE.md`

- [ ] **Compliance team plans conformance**
  - [ ] Define conformance profile (scope, assurance level, features)
  - [ ] Create traceability matrix template
  - [ ] Plan evidence collection strategy
  - [ ] Identify certification body and timeline
  - Document in: `CONFORMANCE_PROFILE.md` and `EVIDENCE_PLAN.md`

---

## Implementation Phase 1: Infrastructure & Backend (Weeks 5–12)

### Wallet Provider Backend

- [ ] **Setup development environment**
  - [ ] Version control repository (GitHub, GitLab, etc.)
  - [ ] CI/CD pipeline (GitHub Actions, Jenkins, etc.)
  - [ ] Artifact repository (Docker Hub, Artifactory, etc.)
  - [ ] Code quality tools (linting, testing, coverage)

- [ ] **Implement credential storage**
  - [ ] Database schema for credentials
  - [ ] Encryption at rest (AES-256)
  - [ ] Access control (role-based, user-based)
  - [ ] Versioning and lifecycle management
  - [ ] Test: Encrypted storage, decryption on access

- [ ] **Implement OpenID4VCI endpoint**
  - [ ] Authorization server (OAuth2)
  - [ ] Token endpoint
  - [ ] Credential endpoint
  - [ ] Metadata endpoint (.well-known/openid-credential-issuer)
  - [ ] Revocation endpoint (or status list)
  - [ ] Test: Full issuance flow with test client

- [ ] **Implement audit logging**
  - [ ] Structured logging (JSON/CSV)
  - [ ] Immutable audit logs
  - [ ] Access controls (compliance team only)
  - [ ] Retention policy (e.g., 7 years)
  - [ ] Test: Log integrity, access control, retention

- [ ] **Implement key management**
  - [ ] Key generation and storage (HSM or encrypted database)
  - [ ] Key rotation procedures
  - [ ] Key lifecycle management
  - [ ] Compromise response plan
  - [ ] Test: Key rotation, compromise handling

- [ ] **Implement ecosystem notifications**
  - [ ] Endpoint for supervisory body notifications
  - [ ] Incident reporting (security, operational)
  - [ ] Status updates (new credentials, revocations)
  - [ ] Test: Notification delivery and format

### Testing & Validation

- [ ] **Unit tests**
  - [ ] Credential serialization/deserialization
  - [ ] Signature generation and verification
  - [ ] Key storage and retrieval
  - [ ] Encryption/decryption
  - [ ] Database operations
  - Target: >80% code coverage

- [ ] **Integration tests**
  - [ ] Full issuance flow (OpenID4VCI)
  - [ ] Credential verification
  - [ ] Revocation flow
  - [ ] Audit logging
  - [ ] Target: All critical paths covered

- [ ] **Security tests**
  - [ ] Key extraction attempts (should fail)
  - [ ] Unauthorized access attempts (should fail)
  - [ ] Tampered credential verification (should fail)
  - [ ] SQL injection attempts (should fail)
  - [ ] Target: All critical security functions tested

---

## Implementation Phase 2: Wallet Instance (Weeks 13–20)

### Mobile/Web Wallet App

- [ ] **Setup mobile/web environment**
  - [ ] Development environment (Xcode, Android Studio, Node.js, etc.)
  - [ ] Test device/browser setup
  - [ ] CI/CD for app builds

- [ ] **Implement credential storage**
  - [ ] Secure local storage (Keychain, Keystore, encrypted LocalStorage)
  - [ ] Database for metadata (expiration, issuer, revocation status)
  - [ ] Encryption at rest
  - [ ] Test: Secure storage, unauthorized access prevention

- [ ] **Implement key management**
  - [ ] Key generation on Secure Enclave (iOS) or TEE (Android)
  - [ ] Key backup/recovery (if applicable)
  - [ ] Key rotation
  - [ ] Test: Keys stored securely, not exported

- [ ] **Implement user authentication**
  - [ ] PIN or pattern authentication
  - [ ] Biometric authentication (fingerprint, face)
  - [ ] Device unlock integration
  - [ ] Authentication bypass prevention
  - [ ] Test: Authentication required before key use

- [ ] **Implement OpenID4VCI client**
  - [ ] Authorization flow (redirect to issuer)
  - [ ] Authorization code handling
  - [ ] Token request and handling
  - [ ] Credential request and reception
  - [ ] Credential validation before storage
  - [ ] Test: Full issuance flow from test issuer

- [ ] **Implement OpenID4VP client**
  - [ ] Presentation request reception (QR code scanning, redirect)
  - [ ] Presentation request parsing
  - [ ] User approval UI
  - [ ] User authentication before sharing
  - [ ] Credential selection (single or multiple)
  - [ ] Selective disclosure (claim selection)
  - [ ] Credential signature (with device key if binding)
  - [ ] Presentation response sending
  - [ ] Test: Full presentation flow end-to-end

- [ ] **Implement credential display**
  - [ ] Credential list view
  - [ ] Credential detail view
  - [ ] Expiration warning
  - [ ] Revocation status display
  - [ ] Credential sharing history (optional)
  - [ ] Test: UI responsiveness, data accuracy

- [ ] **Implement accessibility (WCAG 2.1 AA)**
  - [ ] Color contrast ratios
  - [ ] Font sizes and readability
  - [ ] Keyboard navigation (no mouse-only UI)
  - [ ] Screen reader support (semantic HTML, ARIA labels)
  - [ ] No time-limited interactions
  - [ ] Test: Accessibility audit, automated scanning

### Testing & Validation

- [ ] **Unit tests**
  - [ ] Credential parsing and serialization
  - [ ] Key operations
  - [ ] Authentication logic
  - [ ] OpenID4VCI/VP protocol steps
  - [ ] Target: >80% code coverage

- [ ] **Integration tests**
  - [ ] Full issuance flow (with test issuer)
  - [ ] Full presentation flow (with test service)
  - [ ] Credential display and verification
  - [ ] Multiple credentials (different issuers)
  - [ ] Target: All critical paths covered

- [ ] **User acceptance testing**
  - [ ] New user onboarding flow
  - [ ] Adding credentials
  - [ ] Sharing credentials
  - [ ] Error recovery
  - [ ] Help documentation clarity
  - [ ] Participants: 5–10 non-technical users

- [ ] **Accessibility testing**
  - [ ] Screen reader walkthrough
  - [ ] Keyboard-only navigation
  - [ ] Automated WCAG scanning
  - [ ] High contrast mode
  - [ ] Target: WCAG 2.1 AA compliance

---

## Implementation Phase 3: Service Integration (Weeks 21–26)

### Relying Party Service

- [ ] **Setup RP service infrastructure**
  - [ ] Web/mobile service development environment
  - [ ] OAuth2/OIDC library integration
  - [ ] Credential verification library

- [ ] **Implement credential request creation**
  - [ ] OpenID4VP request generation
  - [ ] QR code generation (for cross-device flow)
  - [ ] Request signing (if required)
  - [ ] Test: Request format validation

- [ ] **Implement credential verification**
  - [ ] Signature verification (using issuer public key from trust list)
  - [ ] Expiration checking
  - [ ] Revocation status checking
  - [ ] Device binding verification (if applicable)
  - [ ] Test: Valid and invalid credential handling

- [ ] **Implement user mapping**
  - [ ] Claim extraction from credential
  - [ ] User matching (linking credential to local user)
  - [ ] User creation (if new credential)
  - [ ] User session creation
  - [ ] Test: Credential → user mapping correctness

- [ ] **Implement trust list management**
  - [ ] Fetch issuer metadata
  - [ ] Cache issuer public keys
  - [ ] Update rotation strategy
  - [ ] Fallback if issuer unavailable
  - [ ] Test: Key verification, cache consistency

- [ ] **Implement registration with supervisory body**
  - [ ] Register RP with member state
  - [ ] Provide endpoint metadata
  - [ ] Maintain compliance with CIR 2025/848
  - [ ] Document in: `RP_REGISTRATION.md`

### Testing & Validation

- [ ] **Integration tests**
  - [ ] Full presentation flow with test wallet
  - [ ] Credential verification (valid/invalid)
  - [ ] User creation and session management
  - [ ] Multiple wallets (interoperability)
  - [ ] Target: All critical paths covered

- [ ] **Interoperability testing**
  - [ ] Test with reference wallet implementation
  - [ ] Test with multiple third-party wallets (if available)
  - [ ] Test across different credential formats
  - [ ] Document compatibility matrix
  - [ ] Document in: `INTEROP_TEST_REPORT.md`

---

## Certification & Compliance Phase (Weeks 27–36)

### Evidence Collection & Compilation

- [ ] **Complete traceability matrix**
  - [ ] All ARF requirements mapped (from Annex 2)
  - [ ] Each requirement has component → test → evidence
  - [ ] Status: Pass/Fail/N/A
  - [ ] Evidence artifacts linked
  - [ ] Document in: `TRACEABILITY_MATRIX.xlsx` or database

- [ ] **Compile architecture documentation**
  - [ ] System architecture diagrams
  - [ ] Component descriptions
  - [ ] Data flow diagrams
  - [ ] Trust model documentation
  - [ ] Deployment architecture
  - [ ] Document in: `ARCHITECTURE.md`

- [ ] **Compile security documentation**
  - [ ] Threat model (complete)
  - [ ] Security architecture
  - [ ] Cryptographic design (algorithms, key lengths)
  - [ ] Key management procedures
  - [ ] Access control model
  - [ ] Incident response procedures
  - [ ] Document in: `SECURITY.md` and `INCIDENT_RESPONSE.md`

- [ ] **Compile test reports**
  - [ ] Unit test results (coverage report)
  - [ ] Integration test results
  - [ ] Security test results
  - [ ] Accessibility audit results
  - [ ] Interoperability test results
  - [ ] Document in: `TEST_REPORTS/` directory

- [ ] **Compile operational procedures**
  - [ ] Deployment procedure
  - [ ] Incident response procedure
  - [ ] Key management procedure
  - [ ] Audit log management
  - [ ] Update/patch procedure
  - [ ] Support procedures
  - [ ] Document in: `OPERATIONS.md`

- [ ] **Compile conformance profile**
  - [ ] Scope statement (roles, assurance levels, features)
  - [ ] Requirements list (which HLRs apply)
  - [ ] Exclusions (which don't apply and why)
  - [ ] Evidence summary
  - [ ] Document in: `CONFORMANCE_PROFILE.md`

### Certification Submission

- [ ] **Prepare certification package**
  - [ ] Cover letter (overview and scope)
  - [ ] Conformance profile
  - [ ] Traceability matrix
  - [ ] Architecture documentation
  - [ ] Security documentation
  - [ ] Test reports
  - [ ] Operational procedures
  - [ ] Incident response plan
  - Organize in: `CERTIFICATION_PACKAGE/`

- [ ] **Submit to supervisory body**
  - [ ] Verify all documents complete
  - [ ] Verify no sensitive data in submission
  - [ ] Submit according to member state process
  - [ ] Record submission date and confirmation
  - [ ] Document in: `CERTIFICATION_TIMELINE.md`

- [ ] **Respond to certification review questions**
  - [ ] Address auditor questions
  - [ ] Provide additional evidence if requested
  - [ ] Clarify requirements interpretation
  - [ ] Timeline: Typically 3–6 months

- [ ] **Receive certification**
  - [ ] Certification decision
  - [ ] Certificate document
  - [ ] Addition to certified wallet list
  - [ ] Document in: `CERTIFICATION_RECORD.md`

---

## Post-Certification: Operations & Maintenance

### Quarterly ARF Synchronization

Every quarter (Feb, May, Aug, Nov):

- [ ] **Check for ARF updates**
  - [ ] Visit: https://github.com/eu-digital-identity-wallet/architecture-and-reference-framework/releases
  - [ ] Read CHANGELOG
  - [ ] Check discussion topics
  - [ ] Review technical specifications progress
  - [ ] Document in: `ARF_SYNC_REPORT_[DATE].md`

- [ ] **Assess impact**
  - [ ] Which HLRs changed?
  - [ ] Which of your components are affected?
  - [ ] Is re-testing required?
  - [ ] Is re-certification required?
  - [ ] Document in: `IMPACT_ASSESSMENT_[DATE].md`

- [ ] **Plan updates (if needed)**
  - [ ] Create backlog items
  - [ ] Estimate effort
  - [ ] Schedule for sprint
  - [ ] Communicate to stakeholders

- [ ] **Execute updates (if needed)**
  - [ ] Update code/documentation
  - [ ] Re-run affected tests
  - [ ] Update traceability matrix
  - [ ] Update certification evidence
  - [ ] Notify supervisory body of changes

### Annual Operations Review

Once per year:

- [ ] **Review incidents**
  - [ ] Summary of security incidents
  - [ ] Incidents handled correctly
  - [ ] Lessons learned
  - [ ] Document in: `ANNUAL_INCIDENT_REVIEW.md`

- [ ] **Review audit logs**
  - [ ] Audit log integrity
  - [ ] Data retention compliance
  - [ ] No unauthorized access
  - [ ] Document in: `AUDIT_LOG_REVIEW.md`

- [ ] **Review security controls**
  - [ ] All controls still effective
  - [ ] No vulnerabilities found
  - [ ] Keys rotated on schedule
  - [ ] Document in: `SECURITY_CONTROL_REVIEW.md`

- [ ] **Review compliance**
  - [ ] All requirements still met
  - [ ] No non-conformances
  - [ ] Feedback to supervisory body
  - [ ] Document in: `ANNUAL_COMPLIANCE_REVIEW.md`

---

## Tracking & Metrics

### Project Health Dashboard

Track these metrics throughout implementation:

| Metric | Target | Frequency | Owner |
|--------|--------|-----------|-------|
| Requirements coverage (%) | 100% | Weekly | Compliance |
| Code review backlog | <5 days | Weekly | Tech Lead |
| Test coverage (%) | >80% | Weekly | QA |
| Open security issues | 0 critical | Daily | Security |
| Incident response time | <4 hours | Monthly | Ops |
| Certification readiness | Green | Monthly | Compliance |

### Milestone Dates

| Phase | Target Date | Status |
|-------|-------------|--------|
| Discovery & Planning | Week 4 | [ ] On track |
| Architecture Review | Week 6 | [ ] On track |
| Backend Phase Complete | Week 12 | [ ] On track |
| App Phase Complete | Week 20 | [ ] On track |
| RP Integration Complete | Week 26 | [ ] On track |
| Certification Submission | Week 30 | [ ] On track |
| Certification Approval | Week 40 | [ ] On track |

---

## Risk Register

For each risk, track: Description, Likelihood, Impact, Owner, Mitigation

| Risk | L | I | Owner | Mitigation |
|------|---|---|-------|------------|
| ARF changes during implementation | M | H | PM | Quarterly sync process |
| Key compromise | L | C | Security | HSM, access controls, monitoring |
| Schedule slip | M | M | PM | Weekly status, risk tracking |
| Interop issues | L | M | Integration | Early testing with partners |
| Certification delay | L | H | Compliance | Pre-certification review |

---

## Sign-Off

When each phase completes:

```
Phase: ________________
Completed by: ________________
Date: ________________
Reviewed by: ________________
Approved by: ________________
```

---

**Last Updated:** March 2026  
**ARF Alignment:** 2.8.0 (2026-02-02)
