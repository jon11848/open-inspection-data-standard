# 7. Evidence, Actors, and Provenance

## 7.1 Evidence

Version 0.1 uses a reference-first evidence model. Evidence normally supplies a retrievable URI or package-relative path plus media metadata. Small embedded content is permitted but discouraged for large media.

Evidence SHOULD include a cryptographic checksum whenever the referenced content is expected to remain evidentiary, auditable, or portable. Temporary signed URLs SHOULD be paired with a stable identifier, package path, checksum, or archival reference.

Supported evidence types may include photographs, video, thermal imagery, audio, drawings, markups, orthomosaics, 3D models, point clouds, documents, sensor streams, measurements, and test results.

## 7.2 Actors

Actor types include humans, organizations, regulators, software systems, AI systems, and devices. Professional credentials may be represented but are not verified merely by inclusion.

## 7.3 Authorship, review, and certification

Authorship answers who or what created a record. Review answers who evaluated it and with what disposition. Certification or attestation answers whether an authorized actor formally accepted responsibility. These concepts MUST remain distinguishable.

Import history and source-system lineage SHOULD be preserved. Implementations MUST NOT present machine-authored content as human-authored or professionally certified unless the record contains the corresponding review or attestation.
