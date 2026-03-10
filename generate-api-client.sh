#!/usr/bin/env bash

HOSTNAME=${1:-bodyloop-control-pc}

curl -kO https://${HOSTNAME}/api/v2/openapi.json

# Optionally beautify the JSON file with jq
mv openapi.json openapi_tmp.json && jq . openapi_tmp.json > openapi.json && rm openapi_tmp.json

# Generate the API client code
mkdir -p src/bodyloop_sdk/api

# Normalize OpenAPI for openapi-python-client compatibility
uv run python scripts/prepare_openapi_for_codegen.py --input openapi.json --output openapi.codegen.json

uv run --with openapi-python-client python -m openapi_python_client generate --overwrite --config generate-api-client.yml --path openapi.codegen.json --output-path src/bodyloop_sdk

mv src/bodyloop_sdk/README.md src/bodyloop_sdk/client/

rm src/bodyloop_sdk/.gitignore
rm src/bodyloop_sdk/pyproject.toml
rm -rf src/bodyloop_sdk/client/.ruff_cache/
