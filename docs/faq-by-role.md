# FAQ by Role

## Shared questions

### Is this repository authoritative?
No. It is a companion implementation and governance pack. Authority remains with the legal texts, the adopted implementing acts, and the current upstream repositories.

### What was the biggest correction in 1.1.0?
The biggest correction was restoring the right authority boundary around **Regulation (EU) 2024/1183** and updating the repository to the current ARF and STS upstream structure.

### Why add automation?
Because upstream drift is a governance problem. If a companion repository cannot detect drift and turn it into tracked remediation work, it will silently degrade.

## Policy / Program Leadership

### What should I care about first?
The authority model, the implementing-act inventory, ownership of synchronization, and the certification/evidence plan.

### What changed materially since older summaries?
The implementing-act surface is fuller, and the April 2026 onboarding regulation adds operational relevance that older companion summaries did not reflect.

## Architects

### Where should I look for technical architecture?
Use the ARF repository for the main narrative and annex structure. Use the STS repository for standards and technical-specification tracking.

### What architectural mistake should we avoid?
Do not assume the ARF alone answers every operational or procedural question once later implementing acts now speak more directly.

## Implementers

### What is the practical starting point?
Use the conformance companion, implementation checklist, and quick reference together. Then map each build decision to the right source layer.

### What should I update immediately in local docs?
Legacy repository links, technical-specification references, and any text that still treats Regulation (EU) 2024/1183 as an implementing act.

## Security / Assurance

### What should we evidence?
Controls, runbooks, tests, source mappings, and drift-response actions.

### What new assurance control exists in this repo?
The upstream synchronization control plane. It produces issues and evidence artifacts when upstream drift is detected.
