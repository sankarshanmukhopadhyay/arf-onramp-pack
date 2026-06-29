# FAQ by Role

## Shared questions

### Is this repository authoritative?
No. It is a companion implementation and governance pack. Authority remains with the legal texts, the adopted implementing acts, and the current upstream repositories.

### What was the biggest correction in 1.1.0?
The biggest correction was restoring the right authority boundary around **Regulation (EU) 2024/1183** and updating the repository to the current ARF and STS upstream structure.

### What changed in 1.2.0?
The repository now targets ARF 2.9.0, treats `https://eudi.dev/` as the public documentation portal, monitors the attestation rulebooks catalog, and supports non-GitHub upstream drift checks for EUR-Lex and public web sources.

### Why add automation?
Because upstream drift is a governance problem. If a companion repository cannot detect drift and turn it into tracked remediation work, it will silently degrade.

## Policy / Program Leadership

### What should I care about first?
The authority model, the implementing-act inventory, ownership of synchronization, and the certification/evidence plan.

### What changed materially since older summaries?
The implementing-act surface is fuller, and CIR (EU) 2026/798 adds operational relevance for remote onboarding where assurance level substantial eID means are combined with additional remote procedures to meet assurance level high.

## Architects

### Where should I look for technical architecture?
Use the ARF repository and public EUDI portal for the main narrative and annex structure. Use the STS repository for standards and technical-specification tracking, and the attestation rulebooks catalog for credential-specific rulebooks.

### What architectural mistake should we avoid?
Do not assume the ARF alone answers every operational or procedural question once later implementing acts now speak more directly.

## Implementers

### What is the practical starting point?
Use the conformance companion, implementation checklist, and quick reference together. Then map each build decision to the right source layer.

### What should I update immediately in local docs?
Legacy repository links, technical-specification references, rulebook references, ARF 2.8.0 assumptions, and any text that still treats Regulation (EU) 2024/1183 as an implementing act.

## Security / Assurance

### What should we evidence?
Controls, runbooks, tests, source mappings, and drift-response actions.

### What new assurance control exists in this repo?
The upstream synchronization control plane. It produces issues and evidence artifacts when upstream drift is detected.
