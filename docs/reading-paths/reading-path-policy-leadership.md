# Reading Path: Policy Leadership & Program Management

**For:** Program managers, policy officers, executive sponsors, member state representatives  
**Focus:** Regulatory landscape, governance models, ecosystem coordination, strategic decisions  
**Time:** 30–45 minutes to read; 2–3 hours with ARF deep-dive  
**Outcome:** Understand EUDI mandate, governance structures, certification requirements, and member state responsibilities

---

## Before You Start

**You should know:**
- What the eIDAS Regulation is (or read [EU Digital Identity Regulation](https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18))
- Your role (implementing, overseeing, or policy-making)
- Your geographic scope (one member state, EU-wide, etc.)

**You might skip if:**
- You're purely a technical implementer (see [Implementer path](./reading-path-implementer.md))
- You need immediate protocol details (see [Implementer path](./reading-path-implementer.md))

---

## Key Concepts for Policy Leaders

### 1. The Regulatory Mandate

**What:** EU Digital Identity Regulation 2024/910 requires member states to provide citizens and businesses with digital identity wallets.

**Why:** To enable:
- Universal access to government services online across EU
- Strong authentication without relying on private platforms
- User control over personal data
- Cross-border interoperability

**Your role:** Decide *how* your member state implements this (government-run, private operator, hybrid, etc.)

### 2. The Architecture & Reference Framework (ARF)

**What:** Technical specification describing how wallets must work

**Who created it:** European Digital Identity Cooperation Group (EDICG)

**Your role:** Ensure your wallet implementation conforms to ARF to achieve EU interoperability

### 3. Governance Layers

The EUDI ecosystem has governance at three levels:

| Level | Players | Decisions |
|-------|---------|-----------|
| **EU/Commission** | EC, EDICG | Technical standards, CIRs, toolbox |
| **Member State** | Supervisory Body, wallets, issuers | Certification, oversight, national rules |
| **Wallet Operator** | Wallet Provider, issuers, RPs | Product design, service policies, SLAs |

**Your role (Member State):** Design national governance while conforming to EU standards.

### 4. Certification & Compliance

**What:** Wallets must be certified by Supervisory Bodies to prove ARF conformance (CIR 2024/2981)

**Why:** Ensures interoperability and security across EU

**Your role:** Designate Supervisory Body, set certification timelines, oversee member state wallets

### 5. Ecosystem Coordination

**What:** Different member states' wallets must recognize each other's credentials

**Why:** User in Spain should be able to use Portuguese government ID to authenticate in German bank

**Your role:** Coordinate with other member states, contribute to EU trust lists, participate in EDICG

---

## Recommended Reading Order

### Section 1: Regulatory Landscape (10 min)

**Read:** [ARF Explained](../arf-explained.md) → "What Is the ARF?" section

**Then:** Understand the regulatory mandate from the [EU Digital Identity Regulation](https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18) (or read a summary)

**Key Questions to Answer:**
- [ ] What does the EU regulation require of member states?
- [ ] What is the EDICG and what role does it play?
- [ ] What is the ARF and who maintains it?

---

### Section 2: EUDI Wallet Overview (10 min)

**Read:** [ARF Explained](../arf-explained.md) → "Key Concepts" section

**Then:** Review [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → **Chapter 1** (Introduction) and **Chapter 2** (Roles & Governance)

**Key Questions to Answer:**
- [ ] What is a wallet and what does it do?
- [ ] Who are the participants (Wallet Provider, PID Provider, Relying Party, Supervisory Body)?
- [ ] What are the governance responsibilities of each role?

---

### Section 3: Governance Model & Member State Role (10 min)

**Read:** [ARF Explained](../arf-explained.md) → "Governance & Oversight" section

**Then:** [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → **Chapter 7** (Conformance & Certification)

**Also Read:** [Commission Implementing Regulation 2024/2981](https://data.europa.eu/eli/reg_impl/2024/2981/oj) → Certification criteria (executive summary)

**Key Questions to Answer:**
- [ ] What are the member state's responsibilities?
- [ ] What is the role of the Supervisory Body?
- [ ] What does wallet certification entail?
- [ ] What oversight mechanisms exist?

---

### Section 4: Certification & Compliance Process (10 min)

**Read:** [Conformance Interpretation Companion](../conformance-interpretation-companion.md) → "Conformance Certification Process" section

**Then:** [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → **Chapter 7** in detail

**Key Questions to Answer:**
- [ ] What is the certification process?
- [ ] What evidence is needed?
- [ ] What is the member state's role in certification?
- [ ] How long does certification typically take?

---

### Section 5: Interoperability & Ecosystem Coordination (5 min)

**Read:** [ARF Explained](../arf-explained.md) → "Interoperability" section

**Then:** [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → **Chapter 2, Section 2.3** (Cross-border interoperability)

**Key Questions to Answer:**
- [ ] How do member state wallets recognize each other?
- [ ] What is the role of trust lists and metadata?
- [ ] How is cross-border compliance coordinated?

---

## Deep-Dive Topics (Optional)

### If You're Designing Member State Wallet Strategy

**Additional Reading:**
1. [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → Chapter 3 (Wallet Architecture)
2. [Governance to Control Mapping](../governance-to-control-mapping.md) → Understand how governance translates to controls
3. [Upstream Alignment Guide](../upstream-alignment-guide.md) → Understand ARF evolution and plan for updates

**Questions to Explore:**
- What assurance levels will your wallet support (L0–L3)?
- Will your wallet be government-run or outsourced?
- How will you handle multiple issuers (PID, EAA, educational credentials)?
- What is your timeline for certification?

### If You're Setting Up Supervisory Body

**Additional Reading:**
1. [CIR 2024/2981](https://data.europa.eu/eli/reg_impl/2024/2981/oj) → Full certification regulation
2. [CIR 2024/2980](https://data.europa.eu/eli/reg_impl/2024/2980/oj) → Ecosystem notifications
3. [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → Chapter 7 (Supervisory Body Responsibilities)

**Questions to Explore:**
- What is the certification approval timeline?
- What resources are needed for oversight?
- How will you maintain the certified wallet list?
- How will you handle incident reports?

### If You're Coordinating Cross-Border Implementation

**Additional Reading:**
1. [EDICG Page](https://digital-strategy.ec.europa.eu/en/policies/european-digital-identity-cooperation-group) → Governance body info
2. [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) → Chapter 2, Section 2.3 (Interoperability)
3. [CIR 2025/846](https://data.europa.eu/eli/reg_impl/2025/846/oj) → Cross-border identity matching

**Questions to Explore:**
- How are trust lists maintained?
- How are metadata and ecosystem information shared?
- What is the process for member state wallets recognizing each other's credentials?

---

## Common Questions for Policy Leaders

### Q1: "What's the difference between the Regulation and the ARF?"

**A:** The **Regulation** is law—what member states must do. The **ARF** is technical guidance—how to do it.

```
Regulation 2024/910 says: "Member states SHALL offer citizens digital wallets"
  ↓
ARF says: "Here's how to build one that interoperates with others"
```

You need both to implement successfully.

### Q2: "Can we build a wallet that doesn't conform to ARF?"

**A:** Technically yes, but it won't interoperate with other member states. The ARF is the basis for EU interoperability.

**Recommendation:** Conform to ARF to enable citizens to use your wallet across EU.

### Q3: "How long does certification take?"

**A:** 3–6 months typically, depending on wallet maturity and evidence completeness. CIR 2024/2981 specifies the process, but timelines vary by member state.

**Planning:** Budget 6–9 months from "ready to certify" to "certified."

### Q4: "What is an 'assurance level' and why does it matter?"

**A:** Assurance levels (L0–L3) are confidence levels in wallet security:

| Level | Use Case | Example |
|-------|----------|---------|
| L0 | Very low stakes | Blog comment login |
| L1 | Standard services | Gov info access |
| L2 | Sensitive services | Bank login |
| L3 | High-value transactions | Land registry, legal docs |

**Implication:** Your wallet must declare what level it targets. L3 requires more stringent security controls.

### Q5: "What role does the Supervisory Body play?"

**A:** The Supervisory Body (member state designated):
- Certifies wallets
- Maintains certified wallet list
- Oversees compliance
- Handles incident reports

**Your role:** Designate a body (government agency, independent authority, etc.) and give it authority.

### Q6: "Can member states have different rules?"

**A:** Some variation is possible, but must stay within ARF envelope. Example:

```
ARF baseline: Device binding is RECOMMENDED (optional)
Member State A: Requires device binding for L2+ (adds requirement)
Member State B: Allows device binding (follows ARF default)
Both are valid as long as both support ARF minimum
```

**Rule:** You can add requirements above ARF minimum, but not below it.

### Q7: "How do we handle incidents (e.g., security breach)?"

**A:** ARF requires incident reporting to Supervisory Body (CIR 2025/847):
- Wallet Provider discovers breach
- Reports to member state within 72 hours
- Supervisory Body notifies EC
- Public notification if user data compromised

**Your role:** Define incident response procedures for your member state.

---

## Strategic Decision Framework

Use this to guide member state wallet strategy:

### Decision 1: Wallet Operator Model

```
Question: Who operates the wallet?

Option A: Government-run
  ✅ Full control, public trust
  ❌ High cost, slower innovation

Option B: Private provider (certified)
  ✅ Market innovation, private sector efficiency
  ❌ Regulatory oversight needed

Option C: Hybrid (government + private alternatives)
  ✅ Choice for citizens, market incentive
  ❌ Complex coordination

ARF Requirement: CIR 2024/2981 applies to all
```

### Decision 2: Assurance Level Target

```
Question: Which assurance levels will your wallet support?

L0–L1: Faster to market, broader use cases
L2: Standard for most government services, good security
L3: High-value transactions, most stringent controls

ARF Requirement: Must support at least some level
Recommendation: Start with L1–L2; L3 optional for later
```

### Decision 3: Credential Scope

```
Question: What credentials will your wallet support at launch?

Baseline: PID (Person ID, government-issued)
Extended: EAAs (educational, professional credentials)
Custom: Industry-specific or domain-specific

ARF Requirement: PID is mandated; others are optional
Recommendation: Define roadmap (what's in v1, v2, v3)
```

### Decision 4: Cross-Border Strategy

```
Question: How will you handle EU interoperability?

Option A: Full interoperability (recognize all EU credentials)
  ✅ Best for citizens, most interoperable
  ❌ Requires coordination and updates

Option B: Gradual (start with trusted partners)
  ✅ Manageable rollout
  ❌ Fragmented user experience initially

ARF Requirement: Member states SHALL coordinate
Recommendation: Join EDICG, participate in trust list maintenance
```

---

## Organizational Checklist

### Before You Start Implementation

- [ ] Understand EU Digital Identity Regulation 2024/910
- [ ] Review ARF main document (especially Chapters 2 & 7)
- [ ] Identify your member state's governance body
- [ ] Designate or establish Supervisory Body
- [ ] Define wallet strategy (operator model, assurance levels, scope)
- [ ] Estimate timeline and budget
- [ ] Plan for EDICG participation

### As You Implement

- [ ] Establish certification criteria for wallet providers
- [ ] Set up compliance monitoring process
- [ ] Maintain certified wallet list
- [ ] Coordinate with other member states (trust lists, metadata)
- [ ] Plan for updates when ARF changes

### Before Certification

- [ ] Ensure wallet provider has conformance evidence
- [ ] Verify traceability matrix completeness
- [ ] Conduct certification review
- [ ] Prepare incident response procedures
- [ ] Train Supervisory Body on oversight duties

---

## Key Resources

### Regulatory Documents
- **EU Digital Identity Regulation 2024/910:** https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18
- **CIR 2024/2981 (Certification):** https://data.europa.eu/eli/reg_impl/2024/2981/oj
- **Other CIRs:** See [Quick Reference](../quick-reference.md)

### ARF Documentation
- **ARF Main Document:** https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md
- **ARF Annexes (high-level requirements):** https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/annexes
- **ARF Repository:** https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework

### Community & Governance
- **EDICG (European Digital Identity Cooperation Group):** https://digital-strategy.ec.europa.eu/en/policies/european-digital-identity-cooperation-group
- **EUDI Wallet Home:** https://ec.europa.eu/digital-building-blocks/sites/spaces/EUDIGITALIDENTITYWALLET/

### On-Ramp Guides (Complementary)
- **Quick Reference:** [../quick-reference.md](../quick-reference.md) — Glossary, regulatory links, resources
- **Upstream Alignment Guide:** [../upstream-alignment-guide.md](../upstream-alignment-guide.md) — Track ARF changes
- **Conformance Interpretation:** [../conformance-interpretation-companion.md](../conformance-interpretation-companion.md) — How to assess conformance

---

## Next Steps

1. **Brief your leadership** on EUDI mandate and ARF landscape
2. **Define your member state strategy** (operator model, timeline, assurance levels)
3. **Establish governance structure** (designate Supervisory Body, set oversight procedures)
4. **Engage with EDICG** for cross-border coordination
5. **Share ARF with implementers** (give them [Implementer path](./reading-path-implementer.md))
6. **Set up compliance monitoring** using [Conformance Interpretation Companion](../conformance-interpretation-companion.md)
7. **Plan for updates** using [Upstream Alignment Guide](../upstream-alignment-guide.md)

---

**Last Updated:** March 2026  
**ARF Alignment:** 2.8.0 (2026-02-02)
