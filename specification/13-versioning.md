# 13. Versioning and Compatibility

Each serialized entity includes `schemaVersion`. Profiles and taxonomies are independently versioned.

During the Version 0 working-draft period, minor versions may include breaking changes. Published releases must preserve tagged copies of the exact schemas and examples.

A change is breaking when a previously conforming producer or consumer would be unable to exchange semantically equivalent information without modification. Adding optional properties is generally non-breaking; changing identifiers, property meaning, coordinate conventions, required fields, or lifecycle semantics is breaking.

Implementations should advertise supported versions and profiles. Importers should reject unsupported major versions with a structured error rather than silently reinterpret them.
