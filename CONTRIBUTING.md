# Contributing

Thank you for helping develop a practical, vendor-neutral inspection-data standard.

## Before contributing

Please review:

- [`GOVERNANCE.md`](GOVERNANCE.md)
- [`IP_POLICY.md`](IP_POLICY.md)
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)
- the relevant specification section and schema

Do not submit confidential customer information, regulated personal data, proprietary taxonomies without permission, or content that you do not have the right to license.

## Contribution paths

Use an issue for questions, defects, ambiguities, and small changes. Use an RFC for changes that affect object boundaries, required fields, identifiers, interoperability behavior, conformance, governance, or backward compatibility.

Helpful contribution types include:

- mappings from existing vendor models;
- inspection use cases and sample packages;
- schema and API reviews;
- implementation feedback;
- taxonomy proposals;
- regulator and professional-practice requirements; and
- test fixtures and validation tools.

## Pull requests

1. Keep each pull request focused.
2. Explain the interoperability problem being solved.
3. Update specification prose, schemas, examples, and tests together when applicable.
4. Add an entry under `CHANGELOG.md` for externally visible changes.
5. Run `python scripts/validate.py`.
6. Sign off the commit using the Developer Certificate of Origin:

```bash
git commit -s -m "Describe the change"
```

The sign-off certifies the statement in [`DCO.txt`](DCO.txt).

## Normative language

Use `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` only for testable requirements. Explanatory guidance should use ordinary language.

## Schema conventions

- JSON Schemas use Draft 2020-12.
- New entity types extend the common entity structure.
- Core required fields should remain minimal.
- Recommended vocabulary terms use stable identifiers.
- Vendor- or jurisdiction-specific information belongs in namespaced extensions when no shared concept exists.
- Normalized image and drawing coordinates use decimal values from `0` through `1`.

## Review expectations

A change is evaluated for interoperability value, implementability, backward compatibility, clarity, privacy and security implications, and alignment with existing standards. Commercial popularity alone is not sufficient reason to make a field mandatory.
