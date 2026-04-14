# Upstream Alignment Guide

## Purpose


This document helps you track how the upstream ARF evolves and map those changes to your implementation. Use it to:

- Identify what changed between ARF versions
- Understand the impact of changes on your system
- Plan migration or conformance updates
- Keep your on-ramp documentation current
- **Monitor Commission Implementing Regulation (CIR) amendments** that impact ARF compliance

---

## 2026 Synchronization Findings

- The canonical upstream repository is `eudi-doc-architecture-and-reference-framework`.
- Standards and Technical Specifications work is now tracked in the dedicated STS repository: `eudi-doc-standards-and-technical-specifications`.
- This guide still uses CIR 2024/1183 as a major anchor for interpretation, but the upstream ARF README now references a broader implementing-regulation set. Use the upstream repository as the authoritative regulatory index.

## Current ARF Version & Regulatory Status

| Attribute | Value |
|-----------|-------|
| **Latest ARF Release** | 2.8.0 |
| **ARF Release Date** | February 2, 2026 |
| **ARF Link** | [GitHub](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/releases/tag/2.8.0) |
| **Current CIR** | **Commission Implementing Regulation (EU) 2024/1183** |
| **CIR Entry into Force** | October 18, 2024 |
| **CIR Application Date** | October 18, 2025 |
| **CIR EUR-Lex Link** | [CIR 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) |
| **CIR Amendment Search** | [EUR-Lex Query](https://eur-lex.europa.eu/search.html?queryText=2024/1183&type=reg) |

> Note: This table highlights one key CIR used throughout this guide. For current legal completeness, consult the upstream ARF repository, which now enumerates a wider set of implementing regulations.

---

## Commission Implementing Regulation (CIR) 2024/1183 Compliance

### Regulatory Structure

**CIR 2024/1183** establishes:
- **Articles 1–8:** Technical specifications for wallet architecture, protocols, data formats
- **Articles 9–13:** Conformance rules, certification procedures, assurance level definitions
- **Annex I:** Data model and schema definitions
- **Annex II:** Technical interoperability requirements
- **Annex III:** Cryptographic algorithms and security parameters

### Key CIR Articles & Implementation Impact

| CIR Article | Title | Implementation Impact | Related ARF |
|---|---|---|---|
| **Art. 1** | Technical specifications for EU Digital Identity Wallet | Defines protocol binding requirements (OpenID4VCI, OpenID4VP) | [ARF Ch. 5](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) |
| **Art. 2** | Definitions and acronyms | Aligns with ARF Annex 1 (Acronyms & Definitions) | [ARF Annex 1](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/annexes) |
| **Art. 9** | Conformance profiles and assurance levels (AL0–AL3) | Governs certification scope and evidence requirements | [ARF Ch. 6](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md), [CIR Annex II](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) |
| **Art. 10** | Supervisory body designation | Defines member state role in wallet oversight | [ARF Ch. 7](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) |
| **Art. 11** | Certification process | Specifies evidence submission and audit procedures | [governance-to-control-mapping.md](./governance-to-control-mapping.md) |
| **Art. 12** | Cross-border recognition | Enables member state wallet acceptance across EU | [ARF Ch. 4](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) |
| **Art. 13** | Amendment procedure | Allows CIR updates through delegated acts | [EUR-Lex](https://eur-lex.europa.eu/search.html?queryText=2024/1183&type=reg) |

### Monitoring CIR Amendments

**Process:** Check for CIR 2024/1183 amendments quarterly using:

1. **EUR-Lex Amendment Search:**  
   https://eur-lex.europa.eu/search.html?queryText=2024/1183&type=reg
   - Filter by "Act Type" = "Amending or Modified Act"
   - Subscribe to EUR-Lex alerts for 2024/1183

2. **Official Journal (OJ) Monitoring:**  
   https://eur-lex.europa.eu/oj/direct-access.html?locale=en
   - Monitor OJ-L (Legislation) for CIR 2024/1183 amendments
   - Amendments typically published with notice periods (30–90 days)

3. **EDICG Coordination:**  
   [European Digital Identity Cooperation Group](https://digital-strategy.ec.europa.eu/en/policies/european-digital-identity-cooperation-group)
   - Quarterly EDICG meetings often precede CIR amendments
   - Subscribe to EDICG updates

### CIR Amendment Impact Assessment Template

When a CIR 2024/1183 amendment is published:

```markdown
## CIR 2024/1183 Amendment: [Title]
- **Amendment ID:** [e.g., Regulation 2024/XXXX]
- **Publication Date:** [OJ date]
- **Entry Into Force:** [date, typically 20 days after OJ]
- **Implementation Deadline:** [if specified]

### Affected Articles/Annexes
- [List articles changed]

### Impact on ARF Implementation
- Cryptographic algorithms: [Yes/No] → Check ARF Ch. 6, Annex III
- Assurance levels: [Yes/No] → Check ARF Ch. 6, CIR Art. 9
- Protocol specs: [Yes/No] → Check ARF Ch. 5, Technical Specs
- Data model: [Yes/No] → Check ARF Annex 2, CIR Annex I

### Required Implementation Changes
- [ ] Code updates
- [ ] Conformance documentation updates
- [ ] Certification evidence re-collection
- [ ] Compliance deadline tracking

### Evidence Update Checklist
- [ ] Update threat model (if security controls changed)
- [ ] Update cryptographic test vectors (if algorithms changed)
- [ ] Update conformance traceability matrix
- [ ] Re-run security testing (if required)
- [ ] Update audit logs and monitoring (if changed)
```

---

## ARF 2.8.0 (February 2, 2026) — Changes & Impact

### Summary

ARF 2.8.0 reflects feedback from Member States (44 comments, primarily on Annex 2), updates from the Certification workstream, progress on Technical Specifications, and finalization of Discussion Topics (F, P, Q, R, S, AA, T, E). All changes align with [CIR 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) requirements.

### Key Changes

| Change Area | What Changed | CIR Alignment | Impact on Implementation |
|-------------|--------------|---|------------------------|
| **Annex 2 (High-Level Requirements)** | 44 member state comments processed; restructured around discussion topics | [CIR Art. 9](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) | **High** — Review your requirement traceability matrix; update conformance profiles if HLRs changed |
| **Main Document (4 figures updated, 1 new)** | Visual updates to architecture and flow diagrams | [CIR Annex II](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) | **Medium** — Verify your architecture diagrams match; update training materials if needed |
| **Discussion Topic F** | Integrated into main text | [CIR Art. 1–8](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) | Check [ARF Section 4.4.3.1](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) if this affects your implementation scope |
| **Discussion Topic P** | Integrated into Section 4.5 | [CIR Art. 2(7)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) (RP definitions) | **High for Relying Parties** — Review RP registration and interaction patterns |
| **Discussion Topic Q** | Integrated into Topic 54 (now in Annex 2) | [CIR Annex II](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) | **Medium** — May affect accessibility requirements |
| **Discussion Topic R** | Integrated into Sections 2.2, 4.3.2, 6.5.3.3; Topic 40 updated | [CIR Annex III](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) (crypto params) | **High** — Device authentication mechanism changes; WSCA/WSCD vs. keystore distinction clarified |
| **Discussion Topic S** | Integrated into Sections 6.3.2.3, 6.4.2; new Topic 55 (Certificate Transparency) | [CIR Art. 9(2)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) | **High** — New transparency requirements for access certificates |
| **Discussion Topic AA** | Electronic Payments SCA support integrated | [CIR Art. 1](https://eur-lex.europa.eu/eli/reg/2024/1183/oj), [PSD2 Directive](https://eur-lex.europa.eu/eli/dir/2015/2366/oj) Art. 67 | **Medium** — Only if you're implementing payment scenarios |
| **Discussion Topic E** | Pseudonym and user authentication mechanism updates | [CIR Annex I](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) (data model) | **Medium** — Review if pseudonym support is in scope |
| **Discussion Topic T** | Wallet Provider support & maintenance integrated | [CIR Art. 2(1)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) | **Low to Medium** — Operational guidance; may affect SLA definitions |
| **Technical Specifications Progress** | Multiple specs advanced toward final release | [CIR Art. 1–8](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) | **Ongoing** — Check [Technical Specs Roadmap](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications) for dependent work |

### Migration Checklist for 2.8.0

- [ ] Read the [full 2.8.0 release notes](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/releases/tag/2.8.0)
- [ ] Review [CIR 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) Articles 1–13 for unchanged mandates
- [ ] Review Annex 2 changes; update traceability matrix against [CIR Annex II](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [ ] If implementing Relying Parties: review [ARF Section 4.5](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) (Topic P) and [CIR Art. 2(7)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [ ] If implementing WSCA/WSCD: confirm alignment with [ARF Section 4.3.2](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) (Topic R) and [CIR Annex III](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [ ] If using certificates for access control: review new Topic 55 requirements against [CIR Art. 9(2)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [ ] Update conformance test evidence for changed HLRs per [CIR Art. 11](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) (certification process)
- [ ] Update architecture diagrams if they reference updated figures (compare with [CIR Annex II](https://eur-lex.europa.eu/eli/reg/2024/1183/oj))
- [ ] Re-run conformance interpretation against new requirements

---

## Recent Versions & What Changed

### ARF 2.7.3 → 2.8.0 Summary

| Topic | Previous Version | Current Version | CIR Authority | On-Ramp Coverage |
|-------|-----------------|-----------------|---|-----------------|
| Device Authentication | Mandatory device binding | Recommended device binding | [CIR Annex III](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) | [reading-path-security-assurance.md](../reading-paths/reading-path-security-assurance.md) |
| Requirement Structure | Monolithic Annex 2 PDF | CSV + Markdown formats | [CIR Annex II](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) | [conformance-interpretation-companion.md](./conformance-interpretation-companion.md) |
| Accessibility | Distributed guidance | Chapter 8 + Topic 54 | [CIR Art. 9(3)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj), [WCAG 2.1](https://www.w3.org/WAI/WCAG21/quickref/) | [reading-path-architect.md](../reading-paths/reading-path-architect.md) |
| Discussion Topics | Active topics F–T | Integrated into main text | [CIR Art. 1–13](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) | [quick-reference.md](./quick-reference.md) |

---

## Historical ARF Releases

For a complete history, see the [ARF CHANGELOG](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/CHANGELOG.md).

### Key Milestones

| Version | Release Date | Notable Changes |
|---------|--------------|-----------------|
| **2.8.0** | 2026-02-02 | Member state feedback, topic integration, spec progress |
| **2.7.0** | 2025-11-10 | Annex 2 restructure (CSV + Markdown), figures regenerated, Discussion Topics P–T integrated |
| **2.5.0** | 2025-09-12 | PID & mDL rulebooks moved to separate repo; Chapter 8 on Accessibility added |
| **2.4.0** | 2025-07-18 | Discussion Topic U & H integration |
| **2.3.0** | 2025-07-04 | Discussion Topic K (combined presentation), various compliance updates |
| **2.2.0** | 2025-06-20 | Ecosystem enhancements, technical specifications roadmap |

---

## How to Track Changes

### Step 1: Monitor Upstream Releases

**Subscribe to notifications:**
- Watch the [ARF repository](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework) (GitHub watch button)
- Subscribe to [releases only](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/releases)

**Check periodically:**
- ARF Releases: https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/releases
- ARF CHANGELOG: https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/CHANGELOG.md
- Discussion Topics: https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/discussion-topics

### Step 2: Assess Impact on Your Implementation

**For each new ARF release:**

1. **Read the release notes** → Understand what changed
2. **Identify affected areas** → Which sections of ARF does this touch?
3. **Map to your system** → How does this affect your architecture?
4. **Update your traceability** → Revise requirement-to-implementation mappings
5. **Plan conformance updates** → What tests or evidence need revision?

Use the **Change Impact Assessment** template below.

### Step 3: Update Your On-Ramp

When you synchronize with a new ARF version:

- [ ] Update the README "Upstream Synchronization Status" table
- [ ] Document breaking changes in your implementation
- [ ] Update reading paths if new topics are introduced
- [ ] Refresh examples and reference sections
- [ ] Add a release note to your CHANGELOG

---

## Change Impact Assessment Template

Use this template to evaluate the impact of ARF changes on your implementation.

```markdown
## ARF [VERSION] Change Impact Assessment

### Release Overview
- **Version:** [X.Y.Z]
- **Release Date:** [YYYY-MM-DD]
- **Link:** [GitHub release URL]

### Changes Summary
[Brief description of what changed]

### Affected Components
| Component | ARF Section(s) | Current Status | Required Changes | Priority |
|-----------|----------------|---------------|--------------------|----------|
| [Component A] | [Section] | [Current implementation status] | [What needs to change] | [P0/P1/P2] |
| [Component B] | [Section] | [Status] | [Changes needed] | [Priority] |

### Evidence & Traceability Updates
- [ ] Update conformance requirement matrix
- [ ] Update architecture diagrams
- [ ] Update test cases / acceptance criteria
- [ ] Update evidence collection procedures

### Migration Effort
- **Effort Estimate:** [Days/weeks]
- **Blockers:** [Any blockers?]
- **Dependencies:** [On what other changes?]

### Signoff
- **Reviewed By:** [Name/Date]
- **Approved By:** [Name/Date]
```

---

## ARF Structure & Where Things Live

To track changes effectively, know where to look:

### Main Document
**File:** `docs/architecture-and-reference-framework-main.md` (~389 KB)

**Structure:**
- **Chapters 1–3:** Regulatory context, principles, roles
- **Chapter 4:** Wallet architecture and ecosystem
- **Chapter 5:** Data flows (proximity, remote, registration)
- **Chapter 6:** Security, integrity, accessibility
- **Appendices:** Glossary, references

**When this changes:** Usually minor updates; major changes are discussed in advance via Discussion Topics.

### Annexes
**Location:** `docs/annexes/`

**Contents:**
- **Annex 1:** Glossary and definitions
- **Annex 2:** High-Level Requirements (now CSV + Markdown)
- **Annex 3–6:** Technical details, conformance profiles, etc.

**When this changes:** Frequently; Annex 2 updates directly reflect member state feedback and Certification workstream comments.

### Discussion Topics
**Location:** `docs/discussion-topics/`

**Format:** Active consultation documents before integration into main ARF. Topics are organized by letter (A, B, C, … AA, AB, …).

**When to monitor:** New Discussion Topics indicate upcoming ARF changes (6–12 month lead time).

### Technical Specifications Roadmap
**Location:** `docs/technical-specifications/`

**Contents:** Links to OpenID4VCI, OpenID4VP, HAIP, and other protocol-specific specs.

**When this changes:** Specs are continuously refined; check for updates quarterly.

---

## Regulatory Changes (Commission Implementing Regulations)

The ARF is anchored in Commission Implementing Regulations (CIRs). Monitor these for normative changes:

### Recent CIRs (2024–2025)

| CIR | Topic | Link |
|-----|-------|------|
| CIR 2024/2977 | PID and EAA | https://data.europa.eu/eli/reg_impl/2024/2977/oj |
| CIR 2024/2979 | Integrity and core functionalities | https://data.europa.eu/eli/reg_impl/2024/2979/oj |
| CIR 2024/2980 | Ecosystem notifications | https://data.europa.eu/eli/reg_impl/2024/2980/oj |
| CIR 2024/2981 | Certification of Wallet Solutions | https://data.europa.eu/eli/reg_impl/2024/2981/oj |
| CIR 2024/2982 | Protocols and interfaces | https://data.europa.eu/eli/reg_impl/2024/2982/oj |
| CIR 2025/846 | Cross-border identity matching | https://data.europa.eu/eli/reg_impl/2025/846/oj |
| CIR 2025/847 | Security breaches | https://data.europa.eu/eli/reg_impl/2025/847/oj |
| CIR 2025/848 | RP registration | https://data.europa.eu/eli/reg_impl/2025/848/oj |
| CIR 2025/849 | List of certified Wallets | https://data.europa.eu/eli/reg_impl/2025/849/oj |

For a complete list, see the [upstream README](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/README.md).

**To stay current:** Subscribe to [EUR-Lex](https://eur-lex.europa.eu/) updates for new CIRs in the digital identity space.

---

## Staying in Sync: Quarterly Checklist

Every quarter, perform this check to keep your implementation aligned with upstream:

### Q1 / Q2 / Q3 / Q4 Sync Checklist

- [ ] **Check for new ARF releases** → [Releases page](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/releases)
- [ ] **Read CHANGELOG entries** → [CHANGELOG.md](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/CHANGELOG.md)
- [ ] **Review new Discussion Topics** → [Discussion topics folder](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/discussion-topics)
- [ ] **Check Technical Specs progress** → [Tech specs folder](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications)
- [ ] **Monitor new CIRs** → [EUR-Lex](https://eur-lex.europa.eu/)
- [ ] **Update your traceability matrix** → Map changed requirements to your components
- [ ] **Run conformance tests** → Verify no regressions from ARF changes
- [ ] **Update on-ramp documentation** → Reflect changes in reading paths and guides

---

## Common Implementation Scenarios & Change Impact

### Scenario: ARF adds a new optional feature

**Example:** New discussion topic on advanced pseudonym modes.

**Your action:**
1. Determine if the feature is in scope for your wallet
2. If in scope → Add to your conformance profile
3. If out of scope → Document the exclusion in your conformance assertion
4. Add test cases for inclusion/exclusion

### Scenario: ARF changes a security requirement

**Example:** Topic S makes certificate transparency mandatory for access certificates (new Topic 55).

**Your action:**
1. Assess current implementation → Do you use access certificates?
2. If yes → Plan conformance changes
3. Update evidence collection procedures
4. Update security tests
5. Update your threat model

### Scenario: ARF moves a rulebook to a separate repo

**Example:** ARF 2.5.0 moved PID and mDL rulebooks to [eudi-doc-attestation-rulebooks-catalog](https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog/).

**Your action:**
1. Update your documentation links
2. Monitor the new rulebook repo for updates
3. If implementing PID/mDL → Follow the rulebook repo going forward

---

## Resources for Deep-Dives

### Understanding ARF Structure
- **ARF Main Document:** https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md
- **Annexes:** https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/annexes
- **Index:** https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/index.md

### Understanding Regulatory Context
- **EU Digital Identity Regulation:** https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18
- **Commission Implementing Regulations:** Listed in [ARF README](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/README.md)

### Standards & Technical Specs
- **Technical Specifications Roadmap:** https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications
- **OpenID4VCI:** https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html
- **OpenID4VP:** https://openid.net/specs/openid-4-verifiable-presentations-1_0.html

---

## Reporting Issues or Gaps

If you identify:

- **Misalignment between ARF and on-ramp:** File an issue in this repo
- **Ambiguity in ARF:** Contribute to the [upstream repo](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework) via issues or pull requests
- **New discussion topics or specs:** They'll be linked here as they emerge

---

## Next Steps

1. **Bookmark this guide** and revisit quarterly
2. **Follow the ARF repository** to catch new releases
3. **Map the current ARF version to your implementation** using the Change Impact Assessment template
4. **Document your conformance mapping** in your conformance profile
5. **Set reminders** to check for updates every 3 months

---

**Last Updated:** March 2026  
**Current ARF Version:** 2.8.0 (2026-02-02)  
**On-Ramp Sync Status:** Aligned ✅
