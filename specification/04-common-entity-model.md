# 4. Common Entity Model

Every entity MUST include:

- `id`: globally unique URI-compatible identifier;
- `type`: canonical entity type;
- `schemaVersion`: OIDS version used to serialize the record;
- `title`: concise human-readable label;
- `createdAt`: creation timestamp;
- `createdBy`: actor reference.

Entities SHOULD include `updatedAt` when changed, and SHOULD preserve source-system identifiers through `externalIdentifiers`.

UUID URNs are the recommended default identifier form, for example `urn:uuid:...`. Implementations MAY use another globally unique URI. An importer MUST NOT replace a globally unique source identifier merely because it also creates a local internal ID; it should retain the source ID as the canonical ID or an external identifier.

The `extensions` object permits namespaced properties. Extension keys SHOULD be absolute URIs or reverse-domain names controlled by the defining organization, such as `com.example.inspection.calibrationId`. Extensions MUST NOT redefine the meaning of core properties.
