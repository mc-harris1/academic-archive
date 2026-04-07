"""Helpers for resolving script-local resources across the repository."""

from __future__ import annotations

from pathlib import Path


def find_repo_root(start_path: str | Path, marker: str = "pyproject.toml") -> Path:
    """Return the nearest ancestor directory containing the repository marker."""

    candidate = Path(start_path).resolve()
    search_root = candidate if candidate.is_dir() else candidate.parent

    for directory in (search_root, *search_root.parents):
        if (directory / marker).exists():
            return directory

    raise FileNotFoundError(
        f"Could not find repository root above {candidate} using marker {marker!r}."
    )


def resolve_local_resource_path(
    caller_file: str | Path,
    resource_name: str | Path,
    relative_dir: str | Path = "data",
    *,
    require_exists: bool = True,
) -> Path:
    """Resolve a resource path relative to the caller script's directory."""

    caller_path = Path(caller_file).resolve()
    resource_dir = caller_path.parent / Path(relative_dir)
    resource_path = resource_dir / Path(resource_name)

    if require_exists and not resource_path.exists():
        resource_label = Path(resource_name).name
        raise FileNotFoundError(f"Resource {resource_label!r} was not found in {resource_dir}.")

    return resource_path
