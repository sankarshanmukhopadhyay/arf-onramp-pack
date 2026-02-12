# ARF Explained (Plain-English On‑Ramp)
**Repository:** eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework  
**Source of truth:** ARF main document (https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md)  

> **What this is:** a “front door” to the Architecture and Reference Framework (ARF).  
> **What this is not:** a replacement for the ARF, the Regulation, or implementing/delegated acts.

---

## 0. Executive summary (read this first)

The **EUDI Wallet ecosystem** is a standardized way for a person (or business) to:
1) **get verified identity data** (PID) from an authoritative source,  
2) **receive attestations** (attributes, qualifications, permissions), and  
3) **present proofs** to a service provider (Relying Party) securely and with strong privacy controls.

**ARF pointers:**  
- [ARF §1.1 EUDI Wallet ecosystem](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#11-eudi-wallet-ecosystem)  
- [ARF §1.3 Purpose, scope and audience](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#13-purpose-scope-and-audience)

---

## 1. Reading paths (choose your adventure)

- **Policy / leadership:** [`docs/reading-paths/reading-path-policy-leadership.md`](reading-paths/reading-path-policy-leadership.md)  
- **Architect / system designer:** [`docs/reading-paths/reading-path-architect.md`](reading-paths/reading-path-architect.md)  
- **Implementer / engineering:** [`docs/reading-paths/reading-path-implementer.md`](reading-paths/reading-path-implementer.md)  
- **Security / privacy / assurance:** [`docs/reading-paths/reading-path-security-assurance.md`](reading-paths/reading-path-security-assurance.md)

---

## 2. The mental model (relatable, stable, and true)

Think of EUDI Wallet as **three operational planes + two trust backbones**:

### Operational planes (what happens at runtime)
1) **Provisioning plane:** getting a wallet instance into a trustworthy state  
2) **Issuance plane:** receiving PID and attestations into the wallet  
3) **Presentation plane:** proving something to a Relying Party

### Trust backbones (why others believe what’s presented)
1) **Crypto / trust services backbone:** signatures, keys, timestamps, certificates, etc.  
2) **Governance / compliance backbone:** registration, certification, conformance, supervision

**ARF pointers:**  
- [ARF §3 EUDI Wallet ecosystem (roles)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#3-eudi-wallet-ecosystem)  
- [ARF §3.17 Registrars](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#317-registrars)  
- [ARF §3.18 Access Certificate Authorities](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#318-access-certificate-authorities)

If you remember only one thing:  
**Runtime flows are easy. Trust at scale is hard. The ARF is about making trust at scale operational.**

---

## 3. The cast of characters (with real-world analogies)

### User
The human (or business representative) using the wallet.

### Wallet Unit (the “wallet instance”)
The actual wallet instance used by the user on a device (think: “your banking profile + secure credential holder + proof engine”).

### Wallet Provider
The organization providing the wallet solution (distribution, lifecycle, updates, operational support).  
**Analogy:** like a mobile banking app provider—except the wallet must be interoperable across borders and contexts.

### PID Provider (Person Identification Data Provider)
The authoritative entity that issues the **PID**.  
**Analogy:** passport office / population registry issuing “who you are” data.

### Attestation Provider (incl. (Q)EAA providers)
Entities issuing **attestations** (attributes, qualifications, permissions).  
**Analogy:** university issuing a degree credential; professional body issuing a license; employer issuing employment status.

### Relying Party (RP)
A service (public or private) requesting proof to deliver a service.  
**Analogy:** bank, telco, government portal, rental service, airline, employer portal.

### Trust Service Provider (TSP) / Qualified TSP (QTSP)
Entities providing trust services that underpin legally meaningful signatures/seals and related trust mechanisms.  
**Analogy:** the “legal-grade crypto infrastructure” layer.

**ARF pointers:**  
- [ARF §3.1 Introduction (roles overview)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#31-introduction)

---

## 4. What’s “inside” a Wallet Unit (conceptual decomposition)

You can treat the Wallet Unit as five logical capabilities:

1) **Credential store**
- Holds PID and attestations (and associated metadata).
- Supports lifecycle events (issue, update, revoke/expire, delete).

2) **Crypto & key management**
- Key generation, storage, usage policies.
- Secure execution path (ideally hardware-backed where available).

3) **Presentation / proof engine**
- Produces proofs (selective disclosure, minimal disclosure, anti-tracking properties).
- Handles supported presentation formats and protocols.

4) **User consent & interaction**
- The user should understand “what am I sharing, with whom, and why.”
- Consent must be meaningful, not ceremonial.

5) **Policy enforcement**
- Applies ecosystem rules (what is allowed, what requires step-up, what is blocked).

**ARF pointers:**  
- [ARF §4.3.2 Components of the Wallet Unit](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#432-components-of-the-wallet-unit)

---

## 5. The three core journeys (end-to-end, in plain language)

### Journey 1: Provision a wallet (make it trustworthy)
**Goal:** A relying party can have confidence that this wallet instance is genuine, up to date, and operating as expected.

**ARF pointers (starting points):**  
- [ARF §4 (Lifecycle/state models)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#4-eudi-wallet-ecosystem-lifecycle-and-interactions)

**Evidence artifacts you want in tests:**
- wallet instance identifier(s) (where applicable)
- attestation or compliance marker (where applicable)
- version + configuration state snapshot
- logs/events showing successful provisioning state

---

### Journey 2: Receive PID and attestations (fill the wallet)
**Goal:** The wallet becomes useful by carrying authoritative data.

Two subflows:
- **PID issuance:** PID Provider → Wallet Unit  
- **Attestation issuance:** Attestation Provider → Wallet Unit

**ARF pointers:**  
- [ARF §3 (Issuer roles and trust)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#3-eudi-wallet-ecosystem)

**Evidence artifacts you want in tests:**
- issuance transaction id / correlation id
- credential object hash / identifier
- issuer signature verification result
- status metadata (validity, expiry, revocation pointer if applicable)

---

### Journey 3: Present proof to a Relying Party (use the wallet)
**Goal:** The RP gets just enough proof to deliver the service—without creating surveillance side-effects.

**ARF pointers:**  
- [ARF §7.4.3.5.2 Mitigating Relying Party linkability](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#74352-mitigating-relying-party-linkability)

**Evidence artifacts you want in tests:**
- presentation request + response pair (signed/verified)
- RP verification flags (cryptographic + policy)
- proof minimization check (“only disclosed what was requested”)
- anti-linkability checks (where applicable)
- audit log entries with correlation ids

---

## 6. Trust, governance, and why “interoperable” is not a slogan

At small scale, you can trust a wallet because you know the vendor.
At EU scale, you need **institutional trust**:
- Who is allowed to issue what?
- How does an RP decide what issuers to accept?
- How are compromised issuers handled?
- How do we stop “fake wallets” and “credential farms”?

So the ecosystem depends on:
- **Trust anchors** (for issuers, wallets, relying parties)
- **Registration / metadata** (so participants can discover trust information)
- **Conformance & certification** (so implementations are testable and auditable)
- **Supervision & incident response** (so reality is handled, not ignored)

**ARF pointers:**  
- [ARF §3.17 Registrars](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#317-registrars)  
- [ARF §3.18 Access Certificate Authorities](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#318-access-certificate-authorities)

---

## 7. Security & privacy: the non-negotiables (translated)

### Security-by-design (what it means operationally)
- Minimize attack surface (reduce exposed interfaces and privilege).
- Bind proofs to the right keys / device / wallet instance.
- Make compromise survivable (revocation, rotation, recovery).
- Treat update mechanisms as critical infrastructure.

### Privacy-by-design (what it means operationally)
- Data minimization: share only what’s required.
- Prevent correlation: avoid creating stable identifiers across relying parties.
- User agency: consent is explicit and understandable.
- RP accountability: verification must not turn into silent tracking.

**ARF pointers:**  
- [ARF §7 Privacy (chapter start)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#7-privacy)  
- [ARF §7.4.3.5.2 Mitigating Relying Party linkability](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#74352-mitigating-relying-party-linkability)

---

## 8. Implementation checklist (a pragmatic “definition of done”)

### A) Role clarity
- [ ] We can name which entity plays PID Provider, Attestation Provider, Wallet Provider, RP, and (Q)TSP in each use case.
- [ ] We can describe the trust relationship between each pair (who trusts whom and why).

### B) Interface readiness
- [ ] Wallet ↔ Issuer issuance path implemented and tested
- [ ] Wallet ↔ Relying Party presentation path implemented and tested
- [ ] Error handling is explicit (timeouts, retries, refusal, invalid proofs)

### C) Evidence-first conformance
- [ ] Every “pass” result has a concrete artifact (IDs, signed messages, verification state, logs)
- [ ] Every failure has a machine-readable reason (problem report / error code) and a test assertion

### D) Security posture
- [ ] Keys protected and lifecycle-managed (rotation, revocation, recovery)
- [ ] Update mechanism integrity verified
- [ ] Threat model exists with control mapping and residual risk notes

### E) Privacy posture
- [ ] Selective/minimal disclosure works as designed
- [ ] Correlation risks assessed (stable identifiers, RP telemetry, wallet behavior patterns)
- [ ] User consent UX prevents “dark pattern consent”

---
**End of document**
