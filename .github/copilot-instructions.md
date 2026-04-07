# Project Guidelines

## Workflow
- Treat this repository as docs-first unless a task explicitly asks for scaffolding or implementation files.
- Update the linked docs when Python or R tooling decisions change before expanding the repo structure.
- Keep changes minimal and consistent with the selected toolchain; do not introduce alternate package managers, linters, or formatters without an explicit reason.

## Toolchain
- Python uses `pyproject.toml` as the source of truth, `uv` for dependency and environment management, `ruff` for linting and formatting, and `pre-commit` for repository hooks.
- R uses `renv.lock` for dependency state, `renv` for environment management, `lintr` for linting, `styler` for formatting, and `precommit` for R hook helpers.
- Keep one root `.pre-commit-config.yaml` that coordinates both ecosystems.
- See `docs/TOOLING.md` for the bootstrap plan, file locations, and command expectations.

## Build And Test
- Do not assume Python or R commands are runnable until the corresponding bootstrap files exist in the repository.
- When Python scaffolding is requested, prefer `uv` commands over direct `pip` usage.
- When R scaffolding is requested, prefer `renv`-managed commands and project-local package state.

## Conventions
- Prefer root-level shared configuration for cross-language tooling unless a subdirectory clearly needs isolated settings.
- Reuse the existing `.gitignore` conventions for `uv`, `ruff`, and `renv` artifacts instead of adding competing ignore patterns.
- If implementation files are introduced later, document any new directory conventions in `docs/TOOLING.md` rather than duplicating them here.
