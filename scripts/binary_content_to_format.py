"""Translate the OpenAPI 3.1 spelling of binary fields into the 3.0 one.

The BodyLoop API (FastAPI/Pydantic v2, OpenAPI 3.1) describes a file upload
field as::

    {"type": "string", "contentMediaType": "application/octet-stream"}

which is the correct 3.1 spelling. `openapi-python-client` only recognises the
OpenAPI 3.0 spelling ``{"type": "string", "format": "binary"}`` as a file; it
turns the 3.1 form into a plain `str` field that is sent as a text part, so
file uploads would not carry the file. This script rewrites the former into the
latter in a copy of the specification, which is then used for code generation
only. The original `openapi.json` is left untouched.

Only `contentMediaType: application/octet-stream` on a string schema without a
`format` is translated; any other `contentMediaType` is left as it is.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

BINARY_MEDIA_TYPE = "application/octet-stream"


def translate_binary_content(node: Any) -> int:
    """Rewrite binary string schemas below `node` in place; return how many were changed."""
    changed = 0
    if isinstance(node, dict):
        if (
            node.get("type") == "string"
            and node.get("contentMediaType") == BINARY_MEDIA_TYPE
            and "format" not in node
            and "contentEncoding" not in node
        ):
            del node["contentMediaType"]
            node["format"] = "binary"
            changed += 1
        for value in node.values():
            changed += translate_binary_content(value)
    elif isinstance(node, list):
        for item in node:
            changed += translate_binary_content(item)
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="OpenAPI JSON file as served by the API")
    parser.add_argument("--output", type=Path, required=True, help="Where to write the translated copy")
    args = parser.parse_args()

    document = json.loads(args.input.read_text(encoding="utf-8"))
    changed = translate_binary_content(document)
    args.output.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {args.output}: {changed} binary field(s) translated to format: binary")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
