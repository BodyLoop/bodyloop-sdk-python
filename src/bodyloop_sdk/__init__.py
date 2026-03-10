"""BodyLoop SDK – Python client for the BodyLoop API."""

from __future__ import annotations

try:
    # Python 3.8+
    from importlib.metadata import version as _pkg_version
except ImportError:  # pragma: no cover (for very old Pythons)
    from importlib_metadata import version as _pkg_version  # type: ignore


def _read_version() -> str:
    # This must match the distribution name in pyproject.toml ([project].name)
    return _pkg_version("bodyloop-sdk")


__version__ = _read_version()
