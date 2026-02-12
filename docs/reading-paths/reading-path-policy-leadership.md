# Reading Path A: Policy, Leadership, and Program Owners
**Target time:** 15–25 minutes  
**Outcome:** You can explain what the EUDI Wallet ecosystem is, why it exists, what “good” looks like at scale, and what must be true for rollout credibility.

**Primary ARF references:**  
- [ARF §1.1 EUDI Wallet ecosystem](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#11-eudi-wallet-ecosystem)  
- [ARF §1.3 Purpose, scope and audience](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#13-purpose-scope-and-audience)  
- [ARF §3 EUDI Wallet ecosystem (roles)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#3-eudi-wallet-ecosystem)  
- [ARF §7 Privacy](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#7-privacy)

---

## 1) The one-paragraph story you should be able to repeat
The EUDI Wallet ecosystem is a standardized EU-wide way for a person to hold authoritative identity data (PID), receive trusted attestations (attributes/qualifications), and present privacy-preserving proofs to services (Relying Parties). The ARF exists to make this interoperable across borders and vendors, while enforcing security, privacy, and governance requirements that can be certified and supervised.

---

## 2) What problem this solves (in program terms)
### Interoperability at EU scale
Without a shared architecture, each Member State and vendor becomes a silo, and cross-border usage collapses into bespoke integrations.

### Trust you can audit
Relying Parties must be able to accept proofs with confidence, based on verifiable trust anchors and certified implementations.

### Privacy as a scaling prerequisite
If the ecosystem enables tracking or data over-collection, it will fail adoption and legitimacy tests, even if it is technically interoperable.

**ARF pointers:**  
- [ARF §7.4.3.5.2 Mitigating Relying Party linkability](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#74352-mitigating-relying-party-linkability)

---

## 3) Roles: who does what (minimum viable clarity)
- **User** (citizen / resident): controls use of the wallet.
- **Wallet Unit:** user’s wallet instance and proof engine.
- **PID Provider:** authoritative issuer of PID.
- **Attestation Providers:** issuers of attributes and qualifications.
- **Relying Party:** service consuming proofs.
- **Registrars / Access Certificate Authorities:** registration + access certificates for ecosystem participants.

**ARF pointers:**  
- [ARF §3.1 Introduction (roles overview)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#31-introduction)  
- [ARF §3.17 Registrars](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#317-registrars)  
- [ARF §3.18 Access Certificate Authorities](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#318-access-certificate-authorities)

---

## 4) The three journeys (what happens in the real world)
1) **Provision** a Wallet Unit into a trustworthy state  
2) **Issue** PID and attestations into the wallet  
3) **Present** proofs to Relying Parties

**ARF pointers (entry points):**  
- [ARF §4 EUDI Wallet ecosystem lifecycle and interactions](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#4-eudi-wallet-ecosystem-lifecycle-and-interactions)

---

## 5) Non-negotiables (the “board slide”)
### Security-by-design
- Compromise must be survivable (revocation, recovery, rotation).
- Update and lifecycle mechanisms are critical infrastructure.

### Privacy-by-design
- Data minimization is mandatory.
- Anti-correlation is a systemic requirement.

### Conformance
- “Interoperable” means testable outcomes with evidence artifacts.
- Certification must reduce false positives and increase auditability.

---

## 6) What to ask teams (high-leverage governance questions)
### A) Ecosystem trust
- Who are the trust anchors for PID Providers, Attestation Providers, Wallet Providers, and Relying Parties?
- How does an RP discover and validate who is authorized to issue what?

### B) Rollout readiness
- What is the incident response model for compromised issuers/wallets?
- What is the revocation and recovery model at population scale?

### C) Adoption and legitimacy
- How do we prevent the wallet from becoming a tracking layer?
- What’s the consent model and how is it enforced?

### D) Conformance and certification
- What evidence is required to claim a pass for each flow?
- How are “passes without proof” prevented in test harnesses?

---

## 7) Decision checklist (definition of done for governance)
- [ ] Roles and accountability mapped per use case
- [ ] Trust anchor discovery model defined for RPs
- [ ] Privacy and anti-correlation requirements operationalized
- [ ] Conformance criteria defined as evidence-backed assertions
- [ ] Supervision and incident response mechanisms documented

---
**End**
