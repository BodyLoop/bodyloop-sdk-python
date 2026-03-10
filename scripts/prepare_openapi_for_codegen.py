"""Normalize an OpenAPI document for `openapi-python-client` compatibility.

This script applies conservative, reversible transformations to a source
OpenAPI JSON file and writes a normalized JSON file for code generation.

Transformations:
- Ensure each schema in `components.schemas` has a unique `title` equal to
  the schema key. This avoids duplicate model names during generation.
- Remove `propertyNames` constraints, which are currently unsupported by
  `openapi-python-client` in a few union/object shapes.
- Remove non-`null` defaults from `anyOf`/`oneOf` unions that include
  `{"type": "null"}`. This avoids parser failures where only `null`
  defaults are accepted for such unions.
"""

from __future__ import annotations

import argparse
import json
from copy import deepcopy
from pathlib import Path
from typing import Any


def _union_includes_null(union_items: Any) -> bool:
    """Return whether a union (`anyOf`/`oneOf`) includes a `null` type branch."""
    if not isinstance(union_items, list):
        return False
    for item in union_items:
        if isinstance(item, dict) and item.get("type") == "null":
            return True
    return False


def _walk_and_normalize(node: Any, stats: dict[str, int]) -> None:
    """Recursively normalize unsupported or problematic JSON Schema fragments.

    The function mutates `node` in place and accumulates change counters in
    `stats`.
    """
    if isinstance(node, dict):
        if "propertyNames" in node:
            node.pop("propertyNames", None)
            stats["property_names_removed"] += 1

        for keyword in ("anyOf", "oneOf"):
            if _union_includes_null(node.get(keyword)):
                if "default" in node and node["default"] is not None:
                    node.pop("default", None)
                    stats["non_null_union_defaults_removed"] += 1

        for value in node.values():
            _walk_and_normalize(value, stats)
        return

    if isinstance(node, list):
        for item in node:
            _walk_and_normalize(item, stats)


def normalize_openapi_document(document: dict[str, Any]) -> tuple[dict[str, Any], dict[str, int]]:
    """Return a normalized copy of an OpenAPI document and change statistics.

    Args:
        document: Parsed OpenAPI JSON object.

    Returns:
        A tuple `(normalized_document, stats)`.

    Raises:
        TypeError: If `document` is not a JSON object represented as `dict`.
    """
    if not isinstance(document, dict):
        raise TypeError("OpenAPI document must be a JSON object")

    normalized = deepcopy(document)
    stats = {
        "titles_updated": 0,
        "property_names_removed": 0,
        "non_null_union_defaults_removed": 0,
    }

    schemas = (
        normalized.get("components", {}).get("schemas", {})
        if isinstance(normalized.get("components"), dict)
        else {}
    )
    if isinstance(schemas, dict):
        for schema_name, schema_def in schemas.items():
            if isinstance(schema_def, dict) and schema_def.get("title") != schema_name:
                schema_def["title"] = schema_name
                stats["titles_updated"] += 1

            _walk_and_normalize(schema_def, stats)

    return normalized, stats


def _default_output_path(input_path: Path) -> Path:
    return input_path.with_name(f"{input_path.stem}.codegen{input_path.suffix}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("openapi.json"), help="Path to input OpenAPI JSON file")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Path to output normalized OpenAPI JSON file (default: <input>.codegen.json)",
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite the input file instead of writing a separate output file",
    )
    args = parser.parse_args()

    input_path: Path = args.input
    output_path: Path = input_path if args.in_place else (args.output or _default_output_path(input_path))

    with input_path.open("r", encoding="utf-8") as fh:
        source = json.load(fh)

    normalized, stats = normalize_openapi_document(source)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as fh:
        json.dump(normalized, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print(
        "Normalized OpenAPI written to"
        f" {output_path} (titles_updated={stats['titles_updated']},"
        f" property_names_removed={stats['property_names_removed']},"
        f" non_null_union_defaults_removed={stats['non_null_union_defaults_removed']})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())