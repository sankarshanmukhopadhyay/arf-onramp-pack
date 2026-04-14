# Upstream Monitoring

This document describes the governance synchronization control plane added in release 1.1.0.

## Goal

Turn upstream drift from an ad hoc maintenance problem into a monitored, evidenced, issue-driven workflow.

## Components

### Source manifest
`governance/upstream-sources.yaml`

Defines what is monitored, at what granularity, and with which labels.

### Workflow
`.github/workflows/upstream-sync.yml`

Runs on a schedule and on manual dispatch.

### Detection script
`scripts/check_upstream_sync.py`

Detects drift, writes evidence artifacts, and opens or updates GitHub issues.

### State and evidence
- `state/upstream-state.json`
- `reports/upstream-drift-report.json`

## Detection model

The control plane is designed to detect:

- new releases
- branch SHA changes
- watched-path drift
- link or repository authority changes encoded in the manifest

## Issue model

When drift is detected, the workflow creates or updates a GitHub issue with:

- affected source
- previous known state
- current detected state
- severity classification
- suggested remediation steps

## Maintainer workflow

1. monitor scheduled workflow results
2. inspect the drift issue and generated report
3. update local docs and references if needed
4. update changelog or release notes when appropriate
5. close the issue once synchronization is complete

## Why this matters

Without a control plane, repository alignment depends on memory. With a control plane, the repository gains:

- repeatable detection
- auditable evidence
- explicit remediation tracking

That is a stronger operational posture for a companion pack that sits downstream of multiple moving authority sources.
