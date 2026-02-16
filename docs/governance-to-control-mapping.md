# Governance-to-Control Mapping Table

## Purpose

This table maps governance expectations within the ARF to operational and technical control surfaces.

---

| Governance Domain | Governance Objective | Control Category | Example Control Implementation | Evidence Artifact |
|------------------|---------------------|-----------------|--------------------------------|-------------------|
| Identity Assurance | Ensure trusted issuance | Issuance Control | Verified onboarding workflow | Issuer audit logs |
| Trust Framework Participation | Maintain ecosystem integrity | Registry Control | Trust list validation logic | Registry sync logs |
| Wallet Security | Protect credential integrity | Cryptographic Control | Key management & secure storage | Key lifecycle records |
| Interoperability | Ensure cross-border usability | Protocol Compliance | Standards-aligned VC exchange | Interop test results |
| Supervision & Audit | Enable oversight | Logging & Reporting | Immutable event logging | Audit trail export |
| Revocation & Status | Maintain credential validity | Status Control | Real-time revocation checks | Revocation registry logs |
| Governance Enforcement | Enforce rule compliance | Policy Enforcement | Access restriction logic | Policy enforcement records |

---

## Control Interpretation Notes

1. Governance constructs must translate into either:
   - Technical controls
   - Operational procedures
   - Supervisory processes

2. Not all governance expectations are directly testable at wallet level.

3. Controls should be categorized as:
   - Preventive
   - Detective
   - Corrective

---

## Usage Guidance

Use this mapping to:
- Identify control gaps
- Align system architecture to governance obligations
- Prepare structured conformance documentation
