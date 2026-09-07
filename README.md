# BodyLoop SDK for Python

Python SDK for the BodyLoop API for seamless ecosystem integration

The URL of the source repository <https://github.com/bodyloop/bodyloop-sdk-python> has suffix `python` to enable adding SDKs for other lanuages such as JavaScript/TypeScript, C/C++, Rust, etc.

The distribution name (install) of the Python Package name is `bodyloop-sdk` and is available in the global Package Index PyPi at <https://pypi.org/project/bodyloop-sdk>. It omits the suffix since PyPi already tells us that we are in the Python ecosystem.

Examples how to get the package are:

```bash
pip install bodyloop-sdk

poetry add bodyloop-sdk

uv add bodyloop-sdk

pipx install bodyloop-sdk

uv tool install bodyloop-sdk
```

The top-level import of the package is the Python module `bodyloop`.

Usage:

```python
from bodyloop_sdk.client import AuthenticatedClient

base_url = "https://bodyloop-control-pc"
api_token = "<YOUR_API_TOKEN_HERE>"

# Create Auth Client with Access Token
client = AuthenticatedClient(
    base_url=base_url,
    verify_ssl=False,
    token=api_token,
    timeout=10.0
)

from functools import partial
from bodyloop_sdk.client.api.probands import get_probands_api_v2_probands_get

get_probands = partial(get_probands_api_v2_probands_get.sync_detailed, client=client)
probands_response = get_probands()

print(probands_response.status_code)
```

## Contribute

Local workflow

```bash
git clone git@github.com:BodyLoop/bodyloop-sdk-python.git
cd bodyloop-sdk-python

uv sync
uv run pytest
uv build
```

## Working on both bodyloop-sdk and another project

In the project which depends on the bodyloop-sdk-python, you can install the SDK in editable mode. This allows you to work on both projects simultaneously without needing to publish the SDK to PyPI.

There you do (assumed that the bodyloop-sdk-python is located at `/d/github/bodyloop/bodyloop-sdk-python`):

```bash
uv sync --no-install-project  --inexact

uv pip install -e /d/github/bodyloop/bodyloop-sdk-python

uv run --no-sync python some_script.py
```

Mind the `--no-sync` flag in the last command, which prevents the SDK from being reinstalled from PyPi.

## Release Procedure

The release / publish workflow is defined as:

- Push to the `main` branch
- Create a new tag `vYYYY.MM.DD.r` where `YYYY.MM.DD` is the current date and `r` is the sequential release number we increment over all releases, independent of the date and push the tag as well.
- Create a new GitHub release based on that tag, baptize the release identical to the tag and add release notes.
- Triggered by the release creation the GitHub Action `publish.yml` will build the package and publish it to PyPi.

Update the API client

The API generator <https://pypi.org/project/openapi-python-client/> is used.

```bash
./generate_api_client.sh <ip_or_hostname_of_my_bodyloop_instance>
```

Use the experiments to get your feet wet:

```bash
touch .env
echo "BODYLOOP_BASE_URL='https://bodyloop-control-pc'" >> .env
echo "BODYLOOP_API_TOKEN='your_api_token_here'" >> .env

uv run experiments/a_create_client.py
uv run experiments/b_load_probands.py
```

### Actions

- Make sure that you are on the `main` branch and that all changes are committed and pushed.
- Create a new tag `vYYYY.MM.DD.r` where `YYYY.MM.DD` is the current date and `r` is the sequential release number we increment over all releases, independent of the date and push the tag as well.

```bash
git checkout main
git pull origin main

git tag | tail -1

git tag v2026.04.13.2
git push --tags
```

- Create a new GitHub release based on that tag, baptize the release identical to the tag and add release notes. You can use the web frontend or the GitHub CLI:

```bash
version=$(git tag | tail -1)

gh release create $version --title $version --notes "Release notes here"
```

Double-check that ...

- GitHub Actions release run starts and runs through green at https://github.com/BodyLoop/bodyloop-sdk-python/actions
- Package has been arrived at https://pypi.org/project/bodyloop-sdk/

## License

See [LICENSE](LICENSE)
