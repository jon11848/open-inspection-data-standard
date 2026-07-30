# Decision 0001: Separate Observation, Finding, and Issue objects

- Status: accepted for Version 0.1 working draft
- Date: 2026-07-30

## Context

Inspection platforms often combine observed evidence, professional interpretation, and corrective workflow into one task or issue. Doing so makes exchange lossy because the underlying observation may remain valid after a finding is revised or an issue is closed.

## Decision

OIDS defines Observation, Finding, and Issue as separate entities connected by explicit relationships. Each entity may also be nested using `parentId`.

## Consequences

Implementations that use one internal task object may export multiple OIDS records. Importers may choose to present those records through a combined interface, but must preserve the distinct identifiers and relationships when claiming round-trip conformance.
