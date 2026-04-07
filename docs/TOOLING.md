# Tooling Plan

## Scope

This repository currently supports Python tooling.

- Python: `pyproject.toml`, `uv`, `ruff`, `pre-commit`

These choices are the default unless a task explicitly changes them.

## Repository Rules

- Keep the repository docs-first until a task explicitly asks for scaffolding or implementation files.
- Use one root `.pre-commit-config.yaml` for repository-wide hooks.
- Avoid alternate dependency managers such as Poetry, Pipenv, or Conda unless the task requires them.
- Treat `pyproject.toml` as the authoritative Python metadata file.
- Commit `uv.lock` when the repository starts behaving like an application or analysis workspace rather than a reusable library.

## Planned File Locations

- Root: `pyproject.toml`
- Root: `.pre-commit-config.yaml`
- Root: `uv.lock` when dependency resolution is checked in
- `docs/`: design, workflow, and setup documentation
- `post-bacc/`: post-baccalaureate program materials
- `graduate-school/`: graduate program materials
- `shared/`: cross-program Python and reference resources

When shared implementation code is introduced, keep reusable helpers under `shared/` and keep course-specific scripts in their course folders.

If code is introduced later, prefer conventional layouts instead of ad hoc placement.

- Python code should normally live under `src/`.
- Tests should follow the structure chosen by the first substantive implementation and remain documented here.

Repository-level shared Python helpers may live under `shared/` when they are intended for direct reuse by standalone course scripts rather than a packaged application layout.

## Bootstrap Sequence

1. Document the intended structure and tooling changes.
2. Add root metadata and environment files for the language being introduced.
3. Add linting and formatting configuration.
4. Wire the workflow into one `.pre-commit-config.yaml`.
5. Run only the commands supported by files that already exist.

## Agent Guidance

- Prefer `uv` commands for Python environment work once `pyproject.toml` exists.
- Do not add duplicate linting or formatting tools when `ruff` already covers the task.
- When configuration changes affect developer workflow, update `.github/copilot-instructions.md` only if the guidance is important for nearly every task.
- For standalone Python scripts that need local data files, prefer a shared helper under `shared/` that resolves resources from the caller script's directory instead of relying on the shell working directory.

## Expected Commands After Bootstrap

Python:

- `uv sync`
- `uv run ruff check .`
- `uv run ruff format --check .`
- `pre-commit run --all-files`

## Current Bootstrap Status

- Root Python metadata is scaffolded in `pyproject.toml` with `ruff` and `pre-commit` in the dev dependency group.
- Shared hooks live in `.pre-commit-config.yaml` and focus on Python formatting and linting.
