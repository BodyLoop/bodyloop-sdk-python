"""Tests for the bodyloop_sdk package."""

import re

import bodyloop_sdk


def test_version_exists():
    """The package exposes a __version__ string."""
    assert hasattr(bodyloop_sdk, "__version__")
    assert isinstance(bodyloop_sdk.__version__, str)


def test_version_format():
    """__version__ matches the hatch-vcs version scheme used by this project."""
    assert re.match(
        r"^(?:\d+\.\d+\.\d+\.\d+(?:\.post\d+\.dev\d+)?|\d+\.\d+\.post\d+\.dev\d+)$",
        bodyloop_sdk.__version__,
    )
