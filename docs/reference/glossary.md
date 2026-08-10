---
layout: default
title: "Glossary"
parent: "Reference"
grand_parent: "Documentation Home"
nav_order: 1
permalink: /docs/reference/glossary/
authority_level: companion-guidance
last_reviewed: 2026-08-10
upstream_dependencies:
  - arf
  - sts
previous_page:
  title: "Reference"
  url: "/docs/reference/"
---
# Glossary

Plain-language definitions for terms used across this pack. These are **companion definitions for orientation**, not binding definitions. Where a term is formally defined in law or in the ARF (typically ARF Annex 1, "Definitions"), that source controls.

{: .authority }
> If a definition here appears to conflict with Regulation (EU) No 910/2014 (as amended), an adopted implementing regulation, or the upstream ARF/STS text, the authoritative source wins. Open an issue using the misclassification report template.

## Ecosystem and actors

**EUDI Wallet (European Digital Identity Wallet)**
The user-controlled application and credential-storage solution that lets a person hold, present, and manage identity data and attestations under Regulation (EU) No 910/2014 as amended.

**Wallet Provider**
The entity (public body, or private entity mandated/recognized by a Member State) responsible for providing a Wallet Solution to users.

**Wallet Solution / Wallet Unit**
The combination of a Wallet Instance (application) and a Wallet Secure Cryptographic Device (or Application) that together form a certified, deployable wallet.

**PID Provider**
The entity issuing Person Identification Data to a wallet, typically a Member State authority or a body it authorizes.

**Attestation Provider**
An entity issuing an Electronic Attestation of Attributes (see below) to a wallet — may be a QEAA, PUB-EAA, or non-qualified EAA provider depending on status and attribute type.

**Relying Party (RP)**
A natural or legal person that relies on a wallet-presented identity or attestation to provide a service, after registering in accordance with the applicable implementing regulation.

**EDICG (European Digital Identity Cooperation Group)**
The Member-State/Commission cooperation body coordinating ARF development, standards work, and implementation guidance under the Common Union Toolbox.

## Credentials and data

**PID (Person Identification Data)**
The core identity attribute set (e.g., name, date of birth) issued to a wallet and used to identify the wallet user.

**EAA (Electronic Attestation of Attributes)**
An attestation of one or more attributes about a person, other than PID, issued to a wallet.

**QEAA (Qualified Electronic Attestation of Attributes)**
An EAA issued by a qualified trust service provider, carrying the qualified-trust-service legal effects under eIDAS.

**PUB-EAA (Public-Body Electronic Attestation of Attributes)**
An EAA issued by or on behalf of a public sector body responsible for the relevant authentic source, without requiring qualified-trust-service status.

**Attestation Rulebook**
A structured, credential-specific specification (data model, trust model, and issuance/verification rules) for a given attestation type — for example PID or mobile driving licence (mDL) — maintained in the upstream attestation rulebooks catalog.

**mDL (mobile Driving Licence)**
A digital driving-licence credential format commonly implemented via ISO/IEC 18013-5 and referenced as an example attestation rulebook.

## Technical and trust infrastructure

**WSCA (Wallet Secure Cryptographic Application)**
The application-level component managing cryptographic operations and key material for a wallet instance.

**WSCD (Wallet Secure Cryptographic Device)**
The hardware or hardware-backed component providing secure key storage and cryptographic operations for a wallet instance (e.g., a secure element).

**Trust Anchor**
A root of trust (certificate, key, or registry entry) used to validate that a wallet, issuer, or relying party is legitimately part of the ecosystem — includes trust lists and certificate-transparency mechanisms.

**HLR (High-Level Requirement)**
A normative, identifiable requirement statement in ARF Annex 2, referenced by an ID (e.g., `ISSU_33b`) so that implementation and conformance work can trace back to a specific upstream obligation.

**OpenID4VCI / OpenID4VP**
The OpenID for Verifiable Credential Issuance and OpenID for Verifiable Presentations protocol families referenced by ARF/STS as candidate interoperability protocols for credential issuance and presentation flows.

## Assurance and conformance

**LoA (Level of Assurance)**
The eIDAS confidence level (low, substantial, high) associated with an identification means or onboarding procedure; several implementing regulations condition obligations on the LoA achieved.

**Conformity Assessment**
The formal process by which a wallet solution (or a component of it) is evaluated against applicable requirements ahead of certification by a competent body.

**FCAF (Functional Conformance Assessment Framework)**
The shared, reusable test-case framework introduced with ARF v3.0.0 (21 July 2026) for assessing wallet functional-requirement conformance ahead of certification. See the [Conformance Interpretation Companion](../conformance-interpretation-companion/) for this pack's current coverage status — companion interpretation guidance for FCAF is a tracked gap, not yet written.

**Drift (upstream drift)**
A detected change in a monitored upstream source (release, branch, watched path, or legal text) that may require this pack's companion guidance to be reviewed or updated. See [Upstream Monitoring](../upstream-monitoring/).

## Legal instruments referenced in this pack

**Regulation (EU) No 910/2014 (eIDAS)**
The primary EU electronic-identification and trust-services regulation, consolidated after amendment by Regulation (EU) 2024/1183.

**Regulation (EU) 2024/1183**
The amending regulation that established the European Digital Identity Framework and the legal basis for the EUDI Wallet. It is an *amending* regulation, not a Commission Implementing Regulation (CIR) — see the [Quick Reference](../quick-reference/) correction note.

**CIR (Commission Implementing Regulation)**
An implementing act adopted by the European Commission that gives operational effect to obligations set out in the amended Regulation (EU) No 910/2014. This pack tracks the wallet-core CIRs listed in [README.md](../../README.md).

{% include page-nav.html %}
