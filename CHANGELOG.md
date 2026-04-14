# Changelog

All notable changes to the ARF On-Ramp Pack are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [1.0.1] - 2026-04-14

### Changed

- Synchronized repository references from the legacy ARF GitHub path to the current canonical upstream repository: `eudi-doc-architecture-and-reference-framework`.
- Repointed technical-specification references to the dedicated STS repository: `eudi-doc-standards-and-technical-specifications`.
- Updated reference framing so the pack no longer presents CIR 2024/1183 as the sole current regulatory basis for the upstream ARF.
- Corrected reference metadata in `REFERENCES.md`, including the upstream license signal and Data Governance Act labeling.

### Documentation

- Added synchronization notes to `README.md`.
- Added 2026 synchronization findings to `docs/upstream-alignment-guide.md`.
- Refreshed upstream URLs across docs and reading paths for consistency and reduced link drift.

---

## [1.0.0] - 2026-03-20

### Added

**Core Documentation:**
- Enhanced README with upstream synchronization status table and landscape context
- New [Upstream Alignment Guide](./docs/upstream-alignment-guide.md) for tracking ARF changes and impact assessment
- Comprehensive [Quick Reference & Glossary](./docs/quick-reference.md) with >100 terms, regulations, and resources
- Expanded [Architecture Layer Map](./docs/architecture-layer-map.md) with detailed decomposition, patterns, and risk analysis
- Greatly expanded [ARF Explained](./docs/arf-explained.md) with scenarios, trust model diagrams, and real-world examples

**Implementation Guidance:**
- Enhanced [Conformance Interpretation Companion](./docs/conformance-interpretation-companion.md) with framework, examples, and evidence types
- New [Governance to Control Mapping](./docs/governance-to-control-mapping.md) linking policy to technical controls

**Reading Paths:**
- Enhanced [Reading Paths Overview](./docs/reading-paths/README.md) with navigation and team workshop agenda
- Comprehensive [Policy Leadership Path](./docs/reading-paths/reading-path-policy-leadership.md) with regulatory context and strategic decisions
- Comprehensive [Architect Path](./docs/reading-paths/reading-path-architect.md) with design exercises and architecture patterns
- Comprehensive [Implementer Path](./docs/reading-paths/reading-path-implementer.md) with protocols, code examples, and implementation patterns
- Comprehensive [Security/Assurance Path](./docs/reading-paths/reading-path-security-assurance.md) with threat modeling and evidence collection

**Project Infrastructure:**
- [CONTRIBUTING.md](./CONTRIBUTING.md) for community contributions
- This [CHANGELOG.md](./CHANGELOG.md) for version tracking
- Project structure aligned with upstream ARF organization

### Features

- **Upstream Synchronization Tracking** — Monitor ARF changes with version tables, migration checklists, and impact assessment
- **Change Impact Assessment Template** — Plan updates when ARF versions change
- **Quarterly Sync Checklist** — Structured process for staying current with upstream
- **Conformance Profile Documentation** — Define implementation scope and track completeness
- **Architecture Layer Navigation** — Map requirements and system components to five logical layers
- **Governance-to-Control Framework** — Connect policy mandates to technical implementations
- **Evidence Collection Guidance** — Plan what proof is needed for certification
- **Role-Based Reading Paths** — Customized guides for policy, architecture, implementation, and security roles

### Improvements

- Clear distinction between on-ramp (companion) and upstream (authoritative) documentation
- Cross-references throughout for navigation
- Concrete examples: ARF 2.8.0 changes, data flow scenarios, control patterns, threat models
- Accessible to non-technical readers (policy) and highly technical readers (developers)
- Actionable next steps in every section
- Alignment table showing which on-ramp documents correspond to ARF chapters

### Documentation

- [README](./README.md) — Project overview, usage guide, resource links
- [ARF Explained](./docs/arf-explained.md) — Simplified structural walkthrough
- [Architecture Layer Map](./docs/architecture-layer-map.md) — Five-layer decomposition with patterns
- [Conformance Interpretation Companion](./docs/conformance-interpretation-companion.md) — Requirement interpretation and evidence planning
- [Governance to Control Mapping](./docs/governance-to-control-mapping.md) — Policy-to-technical mappings
- [Upstream Alignment Guide](./docs/upstream-alignment-guide.md) — ARF change tracking
- [Quick Reference & Glossary](./docs/quick-reference.md) — Terms, regulations, links
- [Reading Paths](./docs/reading-paths/) — Role-specific guides (4 paths)

### Known Limitations

- This is a companion documentation project; it does not replace the authoritative [ARF Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md)
- On-ramp updates lag ARF updates by design (we synthesize, not mirror)
- Community is early-stage; response times may vary

---

## Version History Summary

| Version | Release Date | ARF Alignment | Status |
|---------|--------------|---|---|
| **1.0.0** | 2026-03-20 | 2.8.0 | ✅ Current |

---

## Planned for Future Releases

### Version 1.1.0 (Planned)
- [ ] Implementation case studies (government wallet, private sector wallet, RP integration)
- [ ] Expanded code examples (more languages, more protocols)
- [ ] Interoperability testing guide
- [ ] FAQ by role and common questions
- [ ] Glossary translations (if language demand exists)

### Version 2.0.0 (Planned, ARF Major Version Alignment)
- [ ] Align with ARF 2.9.0 or ARF 3.0.0 (when released)
- [ ] Updates to all reading paths
- [ ] Migration guide from 1.0 to 2.0

---

## Maintenance & Support

**Current Maintainers:**
- Project: [ARF On-Ramp Pack](https://github.com/sankarshanmukhopadhyay/arf-onramp-pack)
- Upstream: [EU Digital Identity Wallet - Architecture and Reference Framework](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework)

**Support Channels:**
- **Issues & Discussions:** GitHub (this repository)
- **Upstream ARF Questions:** GitHub ([ARF repository](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework))
- **EUDI Coordination:** [EDICG](https://digital-strategy.ec.europa.eu/en/policies/european-digital-identity-cooperation-group)

**Maintenance Schedule:**
- **Quarterly Sync:** Check for ARF updates (Feb, May, Aug, Nov)
- **Major ARF Versions:** Full alignment push within 1–2 months
- **Community Issues:** Reviewed weekly, responded to within 5 business days
- **Security Issues:** Escalated immediately (if any found)

---

## How to Report Issues

### Bug Reports
If you find an error in the on-ramp documentation:
1. **Check existing issues** — Your issue might already be reported
2. **Open a new issue** with:
   - Document name and section
   - What's incorrect or unclear
   - Suggested fix
   - Your role (helps context)

### Upstream ARF Issues
If you find an error in the upstream ARF itself:
1. Report to [ARF repository](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/issues)
2. Notify on-ramp maintainers if it affects our guidance

### Feature Requests
Want a new guide or section?
1. **Open a GitHub discussion** or issue
2. Describe what's needed
3. Which role would benefit
4. Why it's important

---

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on:
- Reporting issues
- Suggesting improvements
- Contributing content
- Style guide
- Review process

Thank you for helping improve EUDI implementation guidance! 🙏

---

## Acknowledgments

This on-ramp pack was created to help implementers, architects, policy leaders, and assurance teams navigate the upstream [Architecture and Reference Framework](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework), which is maintained by the European Digital Identity Cooperation Group (EDICG) under the European Commission.

**Credits:**
- Original project structure inspired by EUDI ecosystem needs
- ARF content copyright © European Commission
- On-ramp enhancements © [Author/Organization]

---

## License

This on-ramp pack is provided under the same license as the upstream ARF. See [LICENSE](./LICENSE) for details.

---

**Last Updated:** March 2026  
**Current ARF Alignment:** 2.8.0 (2026-02-02)  
**Next Sync:** June 2026
