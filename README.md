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
import bodyloop
from bodyloop import Viatar, Proband
from bodyloop import ScanUnit
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

## License

See [LICENSE](LICENSE)
