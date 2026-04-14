# Contributing to the ARF On-Ramp Pack

Thank you for considering contributing to the ARF On-Ramp Pack! This guide explains how to help improve this companion documentation project.

---

## What Is This Project?

The **ARF On-Ramp Pack** is a **companion documentation project**, not the authoritative source. Its goal is to help implementers, architects, policy leaders, and assurance teams navigate the upstream [Architecture and Reference Framework (ARF)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework).

---

## How to Contribute

### 1. Report Issues

Found an error or unclear guidance? **Open a GitHub issue.**

**What to include:**
- Which document has the issue?
- What is incorrect or confusing?
- What would clarify it?
- Your role (policy, architecture, implementation, security)

**Example:**
```
Title: "Architecture Layer Map - Missing Container Layer"
Body: "Section 3.2 mentions Wallet Unit but doesn't explain physical vs. virtual containers"
Suggestion: "Add clarification that Wallet Unit can be on-device (Secure Enclave) or cloud (encrypted HSM)"
```

### 2. Suggest Improvements

Have an idea to make guidance better? **Open a GitHub discussion or issue.**

**What to include:**
- What document or topic needs improvement?
- What's missing?
- Why is this important?
- Which role would benefit?

**Example:**
```
Topic: "Add glossary for ARF terms"
Suggestion: "Many readers don't know what WSCA vs. WSCD means"
Why: "Saves them time looking it up in ARF main document"
Audience: "Everyone, especially implementers"
```

### 3. Contribute Content

Want to expand a guide or add a new one? **Propose a pull request.**

**Process:**
1. Fork the repository
2. Create a branch: `git checkout -b docs/add-xyz-guide`
3. Write or edit in Markdown
4. Follow the style guide below
5. Submit a PR with description

**Types of content we welcome:**
- ✅ New reading paths for additional roles
- ✅ Implementation examples and code snippets
- ✅ Case studies or real-world scenarios
- ✅ Clarifications of confusing topics
- ✅ New diagrams or visualizations
- ✅ Translations (if maintained)
- ❌ Normative ARF content (belongs upstream, not here)

### 4. Keep Upstream Alignment Current

The on-ramp tracks the upstream ARF. When the ARF updates, this project needs updates too.

**How to help:**
1. Watch the [ARF releases](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/releases)
2. When a new version is released, open an issue: "Update for ARF vX.Y.Z"
3. Suggest which guides need updating
4. Or contribute the updates yourself (see "Contribute Content" above)

---

## Style Guide

### Writing Style

- **Audience first.** Adapt language to the role (policy leaders use different terms than developers).
- **Clear and concrete.** Use examples, diagrams, and real scenarios.
- **Avoid jargon.** Define acronyms on first use. Link to [quick-reference.md](./docs/quick-reference.md) for definitions.
- **Actionable.** End sections with "Next Steps" or checklists.
- **Not normative.** This is guidance, not the authoritative ARF. Say "ARF says" or "ARF requires," then explain.

### Structure

Follow this template for new documents:

```markdown
# [Document Title]

## Purpose
[What this document is for]

## Key Concepts
[3–5 core ideas]

## [Section 1]
[Content with examples]

## [Section 2]
[Content with examples]

## Next Steps
[What to do after reading]

---
**Last Updated:** [Month Year]  
**ARF Alignment:** [Version, e.g., 2.8.0 (2026-02-02)]
```

### Markdown Formatting

- **Headers:** Use `#` for H1 (title), `##` for H2 (sections), etc.
- **Lists:** Use `-` for bullets, `1.` for numbered
- **Code blocks:** Use triple backticks with language: ` ```python `
- **Links:** `[Link text](URL)` for external, `[Link text](./relative-path)` for internal
- **Tables:** Use GitHub Markdown table syntax
- **Bold:** `**text**` for emphasis
- **Italics:** `*text*` for secondary emphasis

### File Organization

```
docs/
├── README.md (main overview)
├── arf-explained.md
├── architecture-layer-map.md
├── conformance-interpretation-companion.md
├── governance-to-control-mapping.md
├── upstream-alignment-guide.md
├── quick-reference.md
└── reading-paths/
    ├── README.md
    ├── reading-path-policy-leadership.md
    ├── reading-path-architect.md
    ├── reading-path-implementer.md
    └── reading-path-security-assurance.md
```

New documents should fit logically into this structure. If creating a new category, discuss in an issue first.

### Links & References

- **Link to upstream ARF:** Use full GitHub URLs: `https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/...`
- **Link internally:** Use relative paths: `../quick-reference.md`
- **Link to regulations:** Use EUR-Lex URLs: `https://eur-lex.europa.eu/...`
- **Link to standards:** Use official URLs (OpenID, NIST, ISO, etc.)

### Examples & Code

Include concrete examples where possible:

✅ **Good:**
```
Example: Device binding in ARF 2.6.0+

In the wallet:
1. Generate unique key pair on device
2. Embed device public key in credential
3. Require device private key signature in presentation

In the service:
1. Receive credential with device public key
2. Request device proof (signature)
3. Accept credential only if device proof validates
```

❌ **Bad:**
```
Device binding makes credentials more secure.
```

### Diagrams

We welcome diagrams! Use ASCII art or link to external sources:

```markdown
Example ASCII diagram:

┌─────────────┐
│   Component │
└──────┬──────┘
       │
       ▼
    Flow...
```

Or link to images:

```markdown
![Diagram description](./path/to/image.png)
```

---

## Review Process

### Pull Request Review

1. **Automated checks:**
   - Markdown linting (if enabled)
   - Link validation (if enabled)
   - Spelling check (optional)

2. **Manual review:**
   - Content accuracy (does it match ARF?)
   - Clarity (is it understandable to the target audience?)
   - Completeness (are examples included?)
   - Consistency (does it follow style guide?)

3. **Approval:**
   - At least one maintainer approves
   - Changes requested are addressed
   - PR is merged

### Typical Review Timeline

- **Simple fixes (typos, links):** 1–2 days
- **New sections:** 3–5 days
- **New documents:** 5–10 days (may require stakeholder review)

---

## Reporting Issues with ARF Itself

If you find an error in the upstream ARF (not this on-ramp), please report it upstream:

**GitHub:** https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/issues

**Process:**
1. Check if issue already exists
2. Describe the issue clearly
3. Reference ARF version (e.g., 2.8.0)
4. Suggest a fix if you have one

The EDICG and EC team will review and respond.

---

## Code of Conduct

This project follows the [EU Code of Conduct](https://ec.europa.eu/info/about-european-commission/contact_en) for the EUDI Wallet project.

**Expected Behavior:**
- Respectful and inclusive communication
- Constructive feedback
- Acknowledgment of different perspectives
- Focus on shared goal (better EUDI implementation)

**Unacceptable Behavior:**
- Harassment or discrimination
- Insulting or derogatory comments
- Trolling or spam
- Intentional derailment

**Reporting:** Contact [EUDI support](https://ec.europa.eu/about-european-commission/contact_en) or file a private issue.

---

## Recognition

Contributors are recognized in:
- GitHub commit history
- [CONTRIBUTORS.md](./CONTRIBUTORS.md) (maintained list, optional)
- Release notes (for major contributions)

---

## Questions?

If you're unsure about something:

1. **Check existing issues** — Your question might already be answered
2. **Review style guide** — Might clarify process
3. **Open a GitHub discussion** — Ask maintainers or community
4. **Contact ARF maintainers** — For clarification on upstream content

---

## Citation & Reference Standards

All contributions must include proper citations to authoritative sources. This builds trust and enables readers to verify claims.

### Mandatory References

When writing guidance, cite:

1. **ARF Main Document** (v2.8.0+)
   - **Format:** "ARF Chapter X, Section Y: [topic]"
   - **Example:** "ARF Chapter 6, Section 6.2: Cryptographic Requirements"
   - **Link:** Include GitHub URL to specific chapter/section

2. **Commission Implementing Regulations**
   - **Current Standard:** CIR 2024/1183 (entered into force Oct 18, 2024)
   - **Format:** "CIR 2024/1183 Article X"
   - **Example:** "CIR 2024/1183 Article 9: Conformance Rules"
   - **Link:** EUR-Lex URL (https://eur-lex.europa.eu/eli/reg/2024/1183/oj)

3. **eIDAS Regulation (2014/910/EU as amended)**
   - **Format:** "eIDAS Regulation Article X" or "eIDAS Article 5–6: Wallet Definition"
   - **Link:** EUR-Lex (https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18)

4. **Technical Specifications**
   - **OpenID4VCI/OpenID4VP:** Include version and link
   - **ISO/IEC Standards:** Include standard ID and date
   - **IETF RFCs:** Include RFC number and link (https://datatracker.ietf.org/)
   - **W3C Standards:** Include recommendation version and W3C URL

### Citation Style Guide

#### Example 1: Citing ARF Requirement
```markdown
According to ARF Chapter 5, Section 5.3 (Protocol Bindings), 
wallet implementations MUST support OpenID4VCI 1.0 and OpenID4VP 1.0 protocols.
**Reference:** [ARF Chapter 5](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md), 
Section 5.3
```

#### Example 2: Citing Regulatory Requirement
```markdown
CIR 2024/1183 Article 9 (Conformance Profiles) mandates that wallet providers 
must declare conformance to Assurance Level (AL) 1–4 based on their security architecture.
**Reference:** [CIR 2024/1183 Article 9](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
```

#### Example 3: Citing Technical Standard
```markdown
All cryptographic operations MUST use NIST-approved algorithms as per FIPS 140-3.
**Reference:** [FIPS PUB 140-3: Security Requirements for Cryptographic Modules](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.140-3.pdf)
```

#### Example 4: Citing Protocol Specification
```markdown
The wallet MUST implement the OpenID4VCI pre-authorized code flow for credential issuance.
**Reference:** [OpenID for Verifiable Credential Issuance 1.0, Section 3.1](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html)
```

### What Requires Citation?

- ✅ **Always cite:** Legal requirements (ARF, CIRs, eIDAS), technical standards, security controls
- ✅ **Always cite:** Numbers, statistics, compliance deadlines
- ✅ **Always cite:** Direct quotes (even paraphrased)
- ⚠️  **Cite when unclear:** Implementation approaches (link to examples or precedents)
- ⚠️  **Cite when debated:** Any topic mentioned in Discussion Topics (link to GitHub discussion)

### What Doesn't Require Citation?

- ❌ **General knowledge:** "The ARF covers wallet security" (but cite specifics like Chapter 6)
- ❌ **Common sense:** "Wallets should be tested before release"
- ❌ **Definitions from glossary:** Use on-ramp's own [quick-reference.md](./docs/quick-reference.md)

### Checking Citations

Before submitting:

1. **Verify all links work** — Test each URL
2. **Confirm version is current** — ARF v2.8.0+, CIR 2024/1183 (not older versions)
3. **Match quote to source** — Re-read the original to ensure accuracy
4. **Use permanent URLs** — GitHub raw or EUR-Lex URNs (avoid shortened links)

### Reference Management

For larger contributions:

- **Use this reference guide:** [REFERENCES.md](./REFERENCES.md) (comprehensive citation guide)
- **EUR-Lex search:** https://eur-lex.europa.eu/ for CIR lookup
- **ARF releases:** https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/releases
- **OpenID specs:** https://openid.net/developers/specs/ for protocol versions

### Handling Outdated References

If you find outdated citations in existing docs:

1. **Create an issue** with the old citation and new correct reference
2. **Include the reason** why it's outdated (ARF version changed, CIR amended, etc.)
3. **Suggest the fix** with current version and link
4. **Reference this guide** in your issue

---

## Versioning & Release Process

The on-ramp follows [Semantic Versioning](https://semver.org/):

- **MAJOR** version bumps align with upstream ARF major versions
- **MINOR** version bumps for expanded guidance, new documents
- **PATCH** version bumps for clarifications, fixes, upstream tracking updates, citation updates

See [CHANGELOG.md](./CHANGELOG.md) for version history.

---

## Maintainer Responsibilities

Maintainers:
- Review and merge PRs
- Maintain alignment with upstream ARF
- Keep dependencies and references current
- Respond to issues within reasonable timeframe
- Update on-ramp when ARF changes significantly

---

## Thank You

Thank you for contributing to make EUDI implementation easier for everyone! 🙏

---

**Last Updated:** March 2026  
**ARF Alignment:** 2.8.0 (2026-02-02)
