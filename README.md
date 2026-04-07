# academic-archive

Academic archive scaffold for organizing selected graduate coursework projects.

This repository is a curated archive of selected work rather than a complete survey of every project or course artifact.

## Repository Layout

- `graduate-school/`: graduate coursework, selected course projects, and repository utilities
- `docs/`: repository-level planning and tooling documentation

This structure is expected to grow over time. Add new directories as needed while keeping the top-level organization clear.

## Active Workflows

- Python work is currently script-first and centered on course-owned `.py` files.
- Use `uv` from the repository root to manage the Python environment defined in `pyproject.toml`.
- Keep reusable helpers in `graduate-school/utilities/` and course-specific scripts in the course folder that owns them.

See `docs/TOOLING.md` for the repository toolchain details.
