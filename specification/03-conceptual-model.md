# 3. Conceptual Model

## 3.1 Principal entities

- **Asset:** a building or other constructed asset, system, space, or component.
- **Inspection Program:** an ongoing inspection regime, contract, maintenance program, or compliance cycle.
- **Inspection Event:** a bounded inspection occurrence or data-collection activity.
- **Observation:** directly observed, measured, captured, detected, or reported information.
- **Finding:** an interpretation, classification, conclusion, or assessment based on one or more observations or other findings.
- **Issue:** an item requiring tracking, assignment, action, monitoring, verification, or disposition.
- **Evidence:** a referenced or packaged media file, document, measurement source, model, or test result.
- **Location:** one or more spatial references, including asset hierarchy, address, geographic geometry, drawing coordinates, image coordinates, BIM identifiers, or point-cloud references.
- **Actor:** a human, organization, regulator, software system, AI system, or device.
- **Relationship:** a directed semantic link between entities.

## 3.2 Relationships

The standard permits many-to-many relationships. Common relationship types include `observed-at`, `supported-by`, `supports`, `derived-from`, `generates`, `addresses`, `duplicates`, `supersedes`, `verified-by`, and `related-to`.

Relationships MAY be represented through explicit `Relationship` records. Frequently used references also appear directly on entity objects for implementation convenience. If both forms are present, they MUST NOT contradict each other.

## 3.3 Nesting

Most entities support `parentId`. Nesting MAY represent a plan stamp containing multiple findings, a checklist group, an inspection zone, a parent issue, a grouped annotation, or an asset hierarchy. A child remains independently identifiable.
