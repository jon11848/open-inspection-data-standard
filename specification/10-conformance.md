# 10. Conformance and Exchange Packages

An implementation claims one or more roles:

- **Core Reader:** reads and interprets common entity fields and relationships.
- **Core Writer:** produces schema-valid entities.
- **Package Exporter:** produces a complete manifest and declared entity collections.
- **Package Importer:** imports a package and reports rejected or unsupported content.
- **Round-Trip Preserver:** re-exports unknown extensions, source values, and identifiers without material loss.
- **API Provider:** implements declared API capability subsets.
- **Event Producer or Consumer:** implements declared lifecycle events.
- **Profile Implementer:** meets a named profile's additional requirements.

Schema validity alone does not establish semantic conformance. Implementations MUST also satisfy referential integrity, identifier preservation, declared capability behavior, and profile rules.

A package contains a manifest, entities, relationships, profile declarations, export metadata, and optionally package-relative evidence. The package schema supports a single JSON document for small exchanges; larger implementations may use an equivalent archive layout defined by a later packaging profile.
