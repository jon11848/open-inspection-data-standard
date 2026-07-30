# 2. Design Principles

1. **Vendor neutrality.** No vendor's internal task, issue, annotation, or project model is presumed to be universal.
2. **Asset centered.** The asset is the enduring subject; projects and inspection events are time-bound contexts.
3. **Minimal mandatory core.** Required structural fields enable identity, authorship, provenance, and basic interpretation. Domain fields are generally recommended or profile-defined.
4. **Loss-aware interchange.** Source identifiers and original source values may be retained alongside standard mappings.
5. **Separate fact, interpretation, and workflow.** Observation, Finding, and Issue are distinct records.
6. **Extensible vocabularies.** Stable standard identifiers coexist with vendor, profile, and jurisdiction extensions.
7. **Evidence integrity.** Evidence is normally referenced rather than embedded and SHOULD include immutable integrity metadata.
8. **BIM compatible, not BIM dependent.** IFC and BCF references are supported when available, but ordinary drawings, images, addresses, and free-text locations remain valid.
9. **AI is a first-class actor.** AI systems may author observations or findings; review and certification are separately represented.
10. **Workflow independence.** APIs and lifecycle events define interoperable behaviors without prescribing a vendor's internal workflow.
