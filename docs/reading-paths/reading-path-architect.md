# Reading Path B: Architects and System Designers
**Target time:** 30–60 minutes  
**Outcome:** You can map the ecosystem into components, trust boundaries, interfaces, and flows, and you can explain how privacy/security requirements shape architecture choices.

**Primary ARF references:**  
- [ARF §3 EUDI Wallet ecosystem (roles)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#3-eudi-wallet-ecosystem)  
- [ARF §4 (components, lifecycle, interactions)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#4-eudi-wallet-ecosystem-lifecycle-and-interactions)  
- [ARF §4.3.2 Components of the Wallet Unit](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#432-components-of-the-wallet-unit)  
- [ARF §7 Privacy](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#7-privacy)

---

## 1) Mental model (keep this stable)
EUDI Wallet = **three planes + two trust backbones**

### Operational planes
1) Provisioning plane  
2) Issuance plane  
3) Presentation plane

### Trust backbones
1) Crypto / trust services backbone  
2) Governance / compliance backbone

Architectural success = runtime flows + trust decisions + auditability + privacy protections.

---

## 2) Actors and trust boundaries (architectural core)
### Primary actors
- Wallet Unit (on device)
- PID Provider
- Attestation Provider
- Relying Party
- Wallet Provider (ops/lifecycle)
- Registrars / Access Certificate Authorities
- TSP/QTSP (trust services)

**ARF pointers:**  
- [ARF §3.17 Registrars](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#317-registrars)  
- [ARF §3.18 Access Certificate Authorities](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#318-access-certificate-authorities)

### Trust boundaries you must draw explicitly
- Device boundary (secure element / TEE vs app layer)
- Network boundary (issuer and RP channels)
- Governance boundary (trust anchor discovery and policy)
- Audit boundary (what gets logged, where, with what identifiers)

---

## 3) Wallet Unit decomposition (what needs to exist)
Treat the Wallet Unit as five logical capabilities:
1) Credential store  
2) Key management (hardware-backed where possible)  
3) Proof/presentation engine  
4) Consent/UX  
5) Policy enforcement

**ARF pointers:**  
- [ARF §4.3.2 Components of the Wallet Unit](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#432-components-of-the-wallet-unit)

---

## 4) The three core flows (architecture-grade view)
### Flow 1: Provisioning
**Goal:** Wallet Unit becomes trustworthy to ecosystem participants.

Architecture checkpoints:
- wallet integrity and lifecycle management
- update and revocation pathways
- recovery assumptions and operational controls

**ARF pointer:**  
- [ARF §4 EUDI Wallet ecosystem lifecycle and interactions](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#4-eudi-wallet-ecosystem-lifecycle-and-interactions)

### Flow 2: Issuance
- PID Provider → Wallet Unit
- Attestation Provider → Wallet Unit

Architecture checkpoints:
- issuer authentication and trust chain validation
- status/revocation pointers and resolution model
- secure storage and lifecycle updates

### Flow 3: Presentation
Wallet Unit ↔ Relying Party

Architecture checkpoints:
- request/response binding and replay resistance
- selective disclosure/minimal disclosure
- anti-correlation (no stable identifiers across RPs)
- RP verification and audit logs

**ARF pointer:**  
- [ARF §7.4.3.5.2 Mitigating Relying Party linkability](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#74352-mitigating-relying-party-linkability)

---

## 5) Privacy architecture: where systems typically fail
Common failure modes to design against:
- stable identifiers used across RPs (explicit or accidental)
- RP telemetry embedded in requests that becomes a correlation handle
- wallet behavior patterns that leak linkability
- “consent theater” UX that normalizes oversharing

Controls:
- protocol-level anti-correlation techniques
- minimization by default
- deterministic logging discipline

---

## 6) Security architecture: where systems typically fail
Common failure modes:
- weak key lifecycle (rotation/recovery ambiguous)
- insecure update path
- ops channels become a backdoor
- conformance tests validate message shape, not outcomes

Controls:
- hardware-backed key ops where feasible
- signed updates and verified integrity
- explicit privilege separation inside wallet components
- evidence-first test harness integration

---

## 7) Interoperability, architect edition
Interoperability is:
- consistent roles,
- consistent trust discovery,
- consistent evidence artifacts,
- consistent error semantics.

It is not:
- “we can parse the same JSON”.

---

## 8) Deliverables you should produce
- Context diagram with trust boundaries
- Sequence diagrams for the 3 flows
- Threat model mapped to controls (and residual risk)
- Evidence matrix: flow → pass criteria → artifacts → failure modes
- Conformance profile mapping (if profiles exist)

---
**End**
