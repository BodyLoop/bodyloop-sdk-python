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
from bodyloop import System as BodyLoopSystem
```
