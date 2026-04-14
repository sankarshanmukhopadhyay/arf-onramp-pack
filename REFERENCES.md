# References

This file is the reference register for the ARF On-Ramp Pack.

## Reference hierarchy

Use references in this order:

1. **Primary law**
2. **Adopted implementing regulations and decisions**
3. **Official European Commission and upstream repository material**
4. **Standards bodies and protocol specifications**
5. **This repository's companion guidance**

## 1. Primary law

### Regulation (EU) No 910/2014
The legal foundation remains Regulation (EU) No 910/2014 on electronic identification and trust services, in its consolidated form as amended by **Regulation (EU) 2024/1183**.

### Regulation (EU) 2024/1183
This is the amending regulation that establishes the European Digital Identity Framework. In this repository it should be cited as **Regulation (EU) 2024/1183**, not as a Commission implementing regulation.

## 2. Wallet-core implementing regulations

These are the principal wallet-core implementing acts currently reflected in the companion pack.

- **CIR (EU) 2024/2977** — PID and electronic attestations of attributes issued to wallets
- **CIR (EU) 2024/2979** — integrity and core functionalities of wallets
- **CIR (EU) 2024/2980** — notifications to the Commission concerning the wallet ecosystem
- **CIR (EU) 2024/2981** — certification of wallet solutions
- **CIR (EU) 2024/2982** — protocols and interfaces to be supported by the framework
- **CIR (EU) 2025/846** — cross-border identity matching
- **CIR (EU) 2025/847** — reactions to security breaches of wallets
- **CIR (EU) 2025/848** — registration of wallet relying parties
- **CIR (EU) 2025/849** — list of certified wallets
- **CIR (EU) 2026/798** — onboarding of users to wallets by electronic identification means

## 3. Official upstream repositories

### ARF repository
Canonical repository:
`https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework`

What it provides:
- ARF main narrative text
- annexes
- release history
- integration of discussion topics
- upstream legal inventory and repository structure

### STS repository
Canonical repository:
`https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications`

What it provides:
- standards and technical specifications tracking
- issue-based gap analysis
- roadmap and public discussion structure
- technical-specification documents outside the main ARF narrative

### Rulebooks catalog repository
Canonical repository:
`https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog`

## 4. Official European Commission pages

- European Digital Identity Wallet information page
- European Digital Identity Cooperation Group page
- Common Union Toolbox background material

Use these pages for official public-program framing, not as substitutes for the legal texts or implementing regulations.

## 5. Related legislation frequently cited in this repository

- **GDPR** — Regulation (EU) 2016/679
- **PSD2** — Directive (EU) 2015/2366 where wallet-based payment scenarios are discussed
- **Data Governance Act** — Regulation (EU) 2022/868

## 6. Standards and protocol references

### OpenID Foundation
- OpenID for Verifiable Credential Issuance (OpenID4VCI)
- OpenID for Verifiable Presentations (OpenID4VP)
- OpenID Connect Core

### IETF / JOSE / COSE
- RFCs and drafts used where ARF or STS references them for credential, token, or cryptographic exchange formats

### ISO / ETSI / W3C
- ISO/IEC 18013-5 where mDL and wallet-adjacent patterns are relevant
- ETSI and EN references where cited by implementing acts or STS work
- WCAG / accessibility references where ARF accessibility obligations are discussed

## Citation discipline for this repository

When updating repository content:

- cite **Regulation (EU) 2024/1183** as an amending regulation
- cite wallet-core implementing regulations individually when the obligation or procedure comes from an implementing act
- cite the **ARF repository** for technical narrative and annex structure
- cite the **STS repository** for technical-specification development and tracking
- avoid collapsing law, implementation guidance, and companion interpretation into a single authority layer

## Repository synchronization note

The reference register above was refreshed as part of the 1.1.0 release preparation and April 2026 semantic re-audit.
