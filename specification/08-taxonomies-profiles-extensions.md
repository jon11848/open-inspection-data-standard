# 8. Taxonomies, Profiles, and Extensions

## 8.1 Recommended vocabularies

OIDS intentionally avoids large closed mandatory enumerations. A vocabulary value may contain:

- a permanent `standardId`;
- a machine-oriented `code`;
- a human-readable `label`;
- the original `sourceSystem` and `sourceValue`; and
- an optional vocabulary version.

The permanent identifier identifies the concept. Labels may evolve without changing the identifier.

## 8.2 Profiles

An Inspection Profile defines discipline- or use-case-specific requirements and recommendations while reusing the core model. A profile may identify required fields, recommended fields, permitted relationships, vocabulary registries, validation rules, and example packages.

Profiles MUST NOT silently change the meaning of a core property. A profile-specific concept should use a published vocabulary or namespaced extension.

## 8.3 Extensions

Extensions are permitted to avoid blocking adoption. An implementation claiming round-trip conformance MUST preserve unknown extensions even when it does not interpret them, unless it clearly reports that preservation is unsupported.
