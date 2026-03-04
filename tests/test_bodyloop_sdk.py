"""Tests for the bodyloop_sdk package."""

import bodyloop_sdk


def test_version_exists():
    """The package exposes a __version__ string."""
    assert hasattr(bodyloop_sdk, "__version__")
    assert isinstance(bodyloop_sdk.__version__, str)


def test_version_format():
    """__version__ follows semver major.minor.patch format."""
    parts = bodyloop_sdk.__version__.split(".")
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)
