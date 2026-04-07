# Tooling Plan

## Scope

This repository is intended to support both Python and R in one workspace.

- Python: `pyproject.toml`, `uv`, `ruff`, `pre-commit`
- R: `renv.lock`, `renv`, `lintr`, `styler`, `precommit`

These choices are the default unless a task explicitly changes them.

## Repository Rules

- Keep the repository docs-first until a task explicitly asks for scaffolding or implementation files.
- Use one root `.pre-commit-config.yaml` for repository-wide hooks.
- Avoid alternate dependency managers such as Poetry, Pipenv, Conda, or `pak` unless the task requires them.
- Treat `pyproject.toml` as the authoritative Python metadata file, and keep R environment state in `renv.lock`.
- Commit `renv.lock` for reproducibility. Commit `uv.lock` when the repository starts behaving like an application or analysis workspace rather than a reusable library.

## Planned File Locations

- Root: `pyproject.toml`
- Root: `.pre-commit-config.yaml`
- Root: `.lintr`
- Root: `renv.lock`
- Root: `uv.lock` when dependency resolution is checked in
- `docs/`: design, workflow, and setup documentation
- `post-bacc/`: post-baccalaureate program materials
- `graduate-school/`: graduate program materials
- `shared/`: cross-program Python, R, and reference resources

When shared implementation code is introduced, keep reusable helpers under `shared/` and keep course-specific scripts in their course folders.

If code is introduced later, prefer conventional layouts instead of ad hoc placement.

- Python code should normally live under `src/`.
- R package-style code should normally live under `R/`.
- Tests should follow the structure chosen by the first substantive implementation and remain documented here.

Repository-level shared Python helpers may live under `shared/` when they are intended for direct reuse by standalone course scripts rather than a packaged application layout.

## Bootstrap Sequence

1. Document the intended structure and tooling changes.
2. Add root metadata and environment files for the language being introduced.
3. Add linting and formatting configuration.
4. Wire both ecosystems into one `.pre-commit-config.yaml`.
5. Run only the commands supported by files that already exist.

## Agent Guidance

- Distinguish Python `pre-commit` from the R `precommit` package; they complement each other and should not be conflated.
- Prefer `uv` commands for Python environment work once `pyproject.toml` exists.
- Prefer `renv` restore and project-local R package state once `renv.lock` exists.
- Do not add duplicate linting or formatting tools when `ruff`, `lintr`, and `styler` already cover the task.
- When configuration changes affect developer workflow, update `.github/copilot-instructions.md` only if the guidance is important for nearly every task.
- For standalone Python scripts that need local data files, prefer a shared helper under `shared/` that resolves resources from the caller script's directory instead of relying on the shell working directory.

## Expected Commands After Bootstrap

Python:

- `uv sync`
- `uv run ruff check .`
- `uv run ruff format --check .`
- `pre-commit run --all-files`

R:

- `Rscript -e "renv::restore(prompt = FALSE)"`
- Run `lintr` and `styler` through the project configuration that is checked in at the time of the task.
- Use `precommit` only to support the shared hook workflow; do not create a second hook system.

## Current Bootstrap Status

- Root Python metadata is scaffolded in `pyproject.toml` with `ruff` and `pre-commit` in the dev dependency group.
- A seed `renv.lock` is committed for R reproducibility.
- Shared hooks live in `.pre-commit-config.yaml` and rely on the project-managed Python and R environments.
- `.lintr` sets the initial repository-wide R linting defaults.
