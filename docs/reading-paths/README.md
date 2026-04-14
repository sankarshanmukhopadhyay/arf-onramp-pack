# Reading Paths

Welcome! This directory contains **role-oriented entry points** into the ARF—customized guides for different readers.

## How to Use Reading Paths

1. **Find your role** in the list below
2. **Read the recommended path** in order
3. **Jump to specific ARF sections** as needed for deeper dives
4. **Use cross-references** to explore related topics

## Available Reading Paths

### 🏛️ [Policy / Program Leadership](./reading-path-policy-leadership.md)
**For:** Program managers, policy officers, executive sponsors  
**Focus:** Regulatory context, governance models, ecosystem coordination, compliance oversight  
**Time:** 30–45 minutes  
**Includes:** What ARF mandates, compliance requirements, certification process, member state coordination  
**Next Steps:** Brief team on regulatory landscape; define wallet strategy and governance model

---

### 🏗️ [Architect / System Designer](./reading-path-architect.md)
**For:** Enterprise architects, solution architects, technical leads  
**Focus:** System design, architectural patterns, reference architecture, design decisions  
**Time:** 45–60 minutes  
**Includes:** Wallet architecture, data flows, integration patterns, trust model, security architecture  
**Next Steps:** Design your wallet system; define architecture document; plan security controls

---

### 👨‍💻 [Implementer / Engineering Team](./reading-path-implementer.md)
**For:** Developers, backend engineers, mobile/web engineers, DevOps  
**Focus:** Protocols, APIs, data formats, implementation details, testing strategy  
**Time:** 60–90 minutes  
**Includes:** OpenID4VCI/VP flows, credential formats, key management, audit logging, deployment  
**Next Steps:** Plan development sprints; define API contracts; set up test infrastructure

---

### 🔒 [Security / Privacy / Assurance Team](./reading-path-security-assurance.md)
**For:** Security architects, privacy officers, QA engineers, compliance auditors  
**Focus:** Threat models, security controls, privacy requirements, assurance evidence, certification  
**Time:** 60–90 minutes  
**Includes:** Assurance levels, control requirements, threat scenarios, privacy by design, audit trails  
**Next Steps:** Define security architecture; plan threat modeling; design evidence collection; prepare for certification

---

## Quick Navigation by Question

**"I need to understand the regulatory landscape"**  
→ [Policy / Program Leadership](./reading-path-policy-leadership.md)

**"I need to design a wallet system"**  
→ [Architect / System Designer](./reading-path-architect.md)

**"I need to implement credential APIs"**  
→ [Implementer / Engineering Team](./reading-path-implementer.md)

**"I need to ensure security & compliance"**  
→ [Security / Privacy / Assurance Team](./reading-path-security-assurance.md)

**"I'm new to EUDI and don't know where to start"**  
→ Start with [../arf-explained.md](../arf-explained.md), then pick your role above

**"I need to understand all five architectural layers"**  
→ Read [../architecture-layer-map.md](../architecture-layer-map.md)

**"I need to map requirements to controls"**  
→ Read [../governance-to-control-mapping.md](../governance-to-control-mapping.md)

**"I need to track ARF changes and updates"**  
→ Read [../upstream-alignment-guide.md](../upstream-alignment-guide.md)

**"I need glossary, acronyms, and regulatory links"**  
→ Read [../quick-reference.md](../quick-reference.md)

---

## Reading Path Structure

Each reading path includes:

1. **Role Overview** — What this role does and why ARF matters
2. **Key Concepts** — 3–5 core ideas for this role
3. **Recommended Reading Order** — Sections to read in sequence
4. **Deep-Dive Topics** — Optional deeper sections (by interest)
5. **Common Questions** — FAQs for this role
6. **Next Steps** — What to do after reading

---

## Complementary Documents

These cross-cutting guides apply to all roles:

| Document | Purpose |
|----------|---------|
| [ARF Explained](../arf-explained.md) | Simplified walkthrough of ARF structure; start here if new |
| [Architecture Layer Map](../architecture-layer-map.md) | Decomposition into governance, trust, infra, protocol, interop layers |
| [Conformance Interpretation Companion](../conformance-interpretation-companion.md) | How to interpret normative requirements and plan evidence |
| [Governance to Control Mapping](../governance-to-control-mapping.md) | Maps policy requirements to technical controls |
| [Upstream Alignment Guide](../upstream-alignment-guide.md) | Tracks ARF changes and impact on your implementation |
| [Quick Reference](../quick-reference.md) | Glossary, acronyms, regulatory links, resources |

---

## How to Read the ARF Main Document

Each reading path references specific ARF chapters and sections. Here's the upstream ARF structure:

**ARF Main Document:** https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md (~389 KB)

| Chapter | Content | Who Should Read |
|---------|---------|---|
| **1** | Introduction, regulatory context, principles | Everyone (policy leadership especially) |
| **2** | Roles, responsibilities, governance, interoperability | Policy leadership, architects |
| **3** | Wallet architecture and components | Architects, senior developers |
| **4** | Ecosystem, trust model, data flows, lifecycle | All roles |
| **5** | Detailed data flows (issuance, presentation, registration) | Developers, architects |
| **6** | Security, integrity, privacy, accessibility | Security team, architects |
| **7** | Conformance, certification, supervisory oversight | Policy leadership, compliance |
| **Appendices** | Glossary, references, standards | As needed |

---

## Recommended First Steps

### If You Have 15 Minutes
→ Read: [ARF Explained](../arf-explained.md) "Key Concepts" section

### If You Have 30 Minutes
→ Read: [ARF Explained](../arf-explained.md) in full

### If You Have 1 Hour
→ Read: [ARF Explained](../arf-explained.md) + your [reading path](#available-reading-paths)

### If You Have 2 Hours
→ Read: [ARF Explained](../arf-explained.md) + your [reading path](#available-reading-paths) + [Architecture Layer Map](../architecture-layer-map.md)

### If You're Implementing Now
→ Read: Your [reading path](#available-reading-paths) + [Conformance Interpretation Companion](../conformance-interpretation-companion.md) + [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) relevant chapters

---

## Tips for Effective Reading

1. **Skim first** — Get the structure and main points before diving deep
2. **Bookmark the glossary** — [ARF Annex 1](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/annexes) and [Quick Reference](../quick-reference.md) for unfamiliar terms
3. **Use the requirements CSV** — [Annex 2 CSV](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/hltr/high-level-requirements.csv) is searchable and sortable
4. **Draw diagrams** — Especially helpful: wallet architecture, data flows, trust model
5. **Ask questions** — Create GitHub issues if guidance is unclear
6. **Iterate** — Reading paths are not linear; jump around as needed

---

## For Your Team

### Multi-Role Workshop (Half Day)

**Agenda:**

| Time | Activity | Materials |
|------|----------|-----------|
| 0:00–0:15 | Introduction | [ARF Explained](../arf-explained.md) overview |
| 0:15–0:35 | Policy path | [Policy reading path](./reading-path-policy-leadership.md) |
| 0:35–0:55 | Architecture path | [Architecture reading path](./reading-path-architect.md) |
| 0:55–1:15 | Implementation path | [Implementation reading path](./reading-path-implementer.md) |
| 1:15–1:30 | Q&A | [Quick Reference](../quick-reference.md) and [Glossary](../quick-reference.md) |

**Outcome:** Team understands their roles and how to use ARF documentation

---

## Getting Started as a Team

1. **All** → Read [ARF Explained](../arf-explained.md) (30 min)
2. **Each role** → Read your [reading path](#available-reading-paths) (45–60 min)
3. **Architects** → Read [Architecture Layer Map](../architecture-layer-map.md) (30 min)
4. **Security** → Read [Governance to Control Mapping](../governance-to-control-mapping.md) (45 min)
5. **All** → Bookmark [Quick Reference](../quick-reference.md) for ongoing lookup
6. **Program team** → Set up [upstream alignment](../upstream-alignment-guide.md) process (quarterly sync)

---

## Contributing

Found an error in a reading path? Have a suggestion for clarity? File an issue or PR!

---

**Last Updated:** March 2026  
**ARF Alignment:** 2.8.0 (2026-02-02)
