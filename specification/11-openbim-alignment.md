# 11. openBIM Alignment

OIDS is compatible with, but not dependent on, openBIM.

- **IFC:** Asset and Location records may reference IFC GlobalIds, model identifiers, entity types, and spatial structure. OIDS does not duplicate the full IFC asset model.
- **BCF:** Findings and Issues may map to BCF topics and viewpoints. OIDS preserves inspection-specific observations, evidence provenance, non-BIM locations, and broader workflow links that may not be represented by a basic BCF topic.
- **IDS:** Inspection Profiles may use IDS concepts or files to express model-based information requirements when the exchange includes IFC. OIDS profiles also support non-BIM requirements.
- **bSDD or other dictionaries:** Vocabulary terms may reference externally governed concept URIs.

An IFC, BCF, or IDS mapping should identify the exact standard version and document any information loss. OIDS identifiers should remain stable even when mapped to model-specific identifiers.
