"""BodyLoop SDK – Python client for the BodyLoop API."""

from __future__ import annotations

try:
    # Python 3.8+
    from importlib.metadata import PackageNotFoundError, version as _pkg_version
except ImportError:  # pragma: no cover (for very old Pythons)
    from importlib_metadata import (  # type: ignore
        PackageNotFoundError,
        version as _pkg_version,
    )


def _read_version() -> str:
    # This must match the distribution name in pyproject.toml ([project].name)
    try:
        return _pkg_version("bodyloop-sdk")
    except PackageNotFoundError:
        # Fallback for running directly from source without an installed package.
        return "0.0.0.0"


__version__ = _read_version()
