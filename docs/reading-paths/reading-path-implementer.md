# Reading Path C: Implementers and Engineering Teams
**Target time:** 60–120 minutes  
**Outcome:** You can translate ARF concepts into concrete integration work: interfaces, error semantics, evidence artifacts, and test assertions.

**Primary ARF references:**  
- [ARF §4 (components, lifecycle, interactions)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#4-eudi-wallet-ecosystem-lifecycle-and-interactions)  
- [ARF §4.3.2 Components of the Wallet Unit](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#432-components-of-the-wallet-unit)  
- [ARF §7 Privacy](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#7-privacy)

---

## 1) Implementer objective (what “done” looks like)
A working implementation is not “messages sent.” It is:
- correct role behavior,
- verifiable outcomes,
- evidence artifacts per flow,
- deterministic pass/fail criteria in tests.

Your north star: **assertion-based conformance**.

---

## 2) Build order (pragmatic sequencing)
1) Wallet Unit core capabilities (keys, store, proof engine, consent)  
2) Presentation flow with a reference RP (end-to-end loop)  
3) Issuance flows (PID first, then attestations)  
4) Revocation/status and lifecycle  
5) Hardening: error handling, recovery, anti-correlation checks  
6) Conformance harness + evidence report generation  

---

## 3) Core flow checklists (with artifacts)
### Flow A: Provisioning
**Implementation tasks**
- Initialize wallet instance state
- Generate keys and enforce usage policies
- Implement wallet integrity/update validation
- Implement wallet lifecycle events and recovery hooks

**Minimum evidence artifacts**
- wallet instance ID (or equivalent handle)
- version and configuration state
- attestation marker(s) where applicable
- event log entries for provisioning completion

**ARF pointer:**  
- [ARF §4 EUDI Wallet ecosystem lifecycle and interactions](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#4-eudi-wallet-ecosystem-lifecycle-and-interactions)

---

### Flow B: PID issuance
**Implementation tasks**
- Receive issuance request/response
- Validate issuer trust chain
- Verify signature
- Store PID credential + metadata
- Handle expiry and status pointer

**Minimum evidence artifacts**
- issuance transaction/correlation ID
- credential ID/hash
- signature verification result
- validity window and status pointer record

---

### Flow C: Attestation issuance
Same pattern as PID issuance, but with multiple issuer types and attribute policies.

---

### Flow D: Presentation to RP
**Implementation tasks**
- Parse and validate RP request
- Display human-readable request to user
- Enforce minimization and consent
- Produce proof and bind to request
- Send response and capture RP verification outcomes (if available)

**Minimum evidence artifacts**
- request + response pair (signed objects)
- nonce/challenge binding proof (where applicable)
- disclosed attributes list (what was actually shared)
- RP verification state (valid/invalid + reason)
- audit log entry with correlation ID

**ARF pointer:**  
- [ARF §7.4.3.5.2 Mitigating Relying Party linkability](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#74352-mitigating-relying-party-linkability)

---

## 4) Evidence-first test harness (avoid fake passes)
### Principles
- Every pass requires at least one cryptographically verifiable artifact.
- Timeouts are not “passes.”
- State transitions must reach terminal states with proof.

### What to ban
- “sleep 10 seconds then pass”
- “HTTP 200 means success”
- “we parsed the payload, therefore interoperable”

---

## 5) Anti-correlation implementation notes (practical)
- Avoid stable wallet identifiers exposed to RPs across contexts.
- Ensure request handling does not echo RP-specific identifiers back in stable form.
- Validate that logs do not become cross-RP correlation databases.
- Build a privacy regression test: repeated presentations to different RPs must not leak a stable correlator.

---

## 6) Release gates (engineering definition of done)
- [ ] All core flows pass with evidence artifacts
- [ ] Negative tests are implemented and meaningful
- [ ] Revocation/status handling exists and is tested
- [ ] Update and recovery flows are tested
- [ ] Privacy regression tests exist (anti-correlation, minimization)
- [ ] Conformance report is reproducible and auditable

---
**End**
