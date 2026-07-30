#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError, ValidationError
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def schema_registry() -> Registry:
    resources = []
    for path in sorted(SCHEMA_DIR.glob("*.schema.json")):
        schema = load_json(path)
        resources.append((schema["$id"], Resource.from_contents(schema)))
    return Registry().with_resources(resources)


def validate_schema_documents() -> None:
    for path in sorted(SCHEMA_DIR.glob("*.schema.json")):
        schema = load_json(path)
        try:
            Draft202012Validator.check_schema(schema)
        except SchemaError as exc:
            raise RuntimeError(f"Invalid JSON Schema {path.relative_to(ROOT)}: {exc.message}") from exc


def validate_instance(instance_path: Path, schema_path: Path, registry: Registry) -> None:
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema, registry=registry, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(load_json(instance_path)), key=lambda e: list(e.absolute_path))
    if errors:
        details = []
        for error in errors[:30]:
            pointer = "/" + "/".join(str(x) for x in error.absolute_path)
            details.append(f"  {pointer}: {error.message}")
        raise RuntimeError(
            f"Validation failed for {instance_path.relative_to(ROOT)} against {schema_path.name}:\n" + "\n".join(details)
        )


def all_entities(package: dict[str, Any]) -> list[dict[str, Any]]:
    entity_keys = [
        "actors", "assets", "locations", "inspectionPrograms", "inspectionEvents",
        "evidence", "observations", "findings", "issues", "relationships", "profiles"
    ]
    return [entity for key in entity_keys for entity in package.get(key, [])]


def validate_referential_integrity(package_path: Path) -> None:
    package = load_json(package_path)
    entities = all_entities(package)
    ids = [entity["id"] for entity in entities]
    duplicate_ids = sorted({identifier for identifier in ids if ids.count(identifier) > 1})
    if duplicate_ids:
        raise RuntimeError(f"Duplicate entity IDs: {duplicate_ids}")
    known = set(ids)

    required_internal_fields = {
        "assetId", "programId", "inspectionEventId", "parentId", "primaryLocationId",
        "documentId", "evidenceId", "requestedById", "supersedesId", "organizationId", "deviceId"
    }
    required_internal_array_fields = {
        "assetIds", "locationIds", "participantIds", "evidenceIds", "observationIds",
        "findingIds", "assignedToIds", "ownerIds", "verificationFindingIds"
    }
    missing: list[str] = []

    def walk(value: Any, path: str = "") -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                current = f"{path}/{key}"
                if key in required_internal_fields and isinstance(child, str) and child not in known:
                    missing.append(f"{current} -> {child}")
                elif key in required_internal_array_fields and isinstance(child, list):
                    for index, identifier in enumerate(child):
                        if isinstance(identifier, str) and identifier not in known:
                            missing.append(f"{current}/{index} -> {identifier}")
                elif key in {"createdBy", "capturedBy", "actor", "source", "target", "resolvedBy"} and isinstance(child, dict):
                    identifier = child.get("id")
                    if identifier and identifier not in known:
                        missing.append(f"{current}/id -> {identifier}")
                walk(child, current)
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{path}/{index}")

    walk(package)
    missing = [item for item in missing if "profileIds" not in item]
    if missing:
        raise RuntimeError("Unresolved internal references:\n  " + "\n  ".join(missing))


def validate_openapi() -> None:
    path = ROOT / "api" / "openapi.yaml"
    document = yaml.safe_load(path.read_text(encoding="utf-8"))
    version = str(document.get("openapi", ""))
    if not version.startswith("3.1."):
        raise RuntimeError(f"OpenAPI document must use 3.1.x, found {version!r}")
    if not document.get("paths") or not document.get("components"):
        raise RuntimeError("OpenAPI document is missing paths or components")


def main() -> int:
    validate_schema_documents()
    registry = schema_registry()
    validate_instance(ROOT / "examples/facade-inspection/package.json", SCHEMA_DIR / "package.schema.json", registry)
    validate_instance(ROOT / "profiles/facade-envelope/profile.json", SCHEMA_DIR / "profile.schema.json", registry)
    validate_instance(ROOT / "taxonomies/core.json", SCHEMA_DIR / "taxonomy.schema.json", registry)
    validate_instance(ROOT / "taxonomies/facade-envelope.json", SCHEMA_DIR / "taxonomy.schema.json", registry)
    validate_instance(ROOT / "events/examples/issue-status-changed.json", SCHEMA_DIR / "lifecycle-event.schema.json", registry)
    validate_referential_integrity(ROOT / "examples/facade-inspection/package.json")
    validate_openapi()
    print("Validation completed successfully.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValidationError, json.JSONDecodeError, yaml.YAMLError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
