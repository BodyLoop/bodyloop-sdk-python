# GitHub Copilot Instructions

## Project Overview

`bodyloop-sdk-*` is the pattern for the repositories of the SDKs 
for the BodyLoop API for certain languages.

This repository, `bodyloop-sdk-python` implements the one for Python.

## Spec-Driven Development Workflow

REVIEW: Defect, major: Does not apply SDD in a correct way. Does not describe the workflow we intend. 

1. **Spec** – Write a detailed docstring describing the function/class contract
   (inputs, outputs, raised exceptions, edge cases) before any implementation.
2. **Implement** – Ask Copilot to generate the implementation that satisfies the spec.
3. **Test** – Ask Copilot to generate `pytest` tests covering the spec.
4. **Review** – Verify Copilot output matches the spec; adjust as needed.

## Code Style

- Python ≥ 3.11; use type hints on all public APIs.
- Keep the `src/bodyloop_sdk/` layout; add new modules inside that package.
- Use `snake_case` for functions/variables, `PascalCase` for classes.
- Keep public APIs small and composable; prefer pure functions.

## Testing

- All tests live in `tests/`; mirror the source module structure.
- Every public function must have at least one happy-path test and one
  error/edge-case test.
- Run tests with: `uv run pytest`

## Dependency Management

- Manage dependencies with `uv`; edit `pyproject.toml` directly.
- Add runtime deps: `uv add <package>`
- Add dev deps: `uv add --dev <package>`

## Release Process

- Bump `__version__` in `src/bodyloop_sdk/__init__.py`.
- Create a GitHub release tagged `vX.Y.Z`.
- The `release.yml` workflow will build and publish to PyPI automatically.
