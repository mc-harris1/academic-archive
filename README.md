# academic-archive

Academic archive scaffold for organizing post-baccalaureate work, graduate coursework, and shared Python resources.

## Repository Layout

- `post-bacc/`: post-baccalaureate notes and course materials
- `graduate-school/`: graduate coursework and related materials
- `shared/`: cross-program Python resources, utilities, and reference notes
- `docs/`: repository-level planning and tooling documentation

This structure is expected to grow over time. Add new directories as needed while keeping the top-level organization clear.

## Active Workflows

- Python work is currently script-first and centered on course-owned `.py` files.
- Use `uv` from the repository root to manage the Python environment defined in `pyproject.toml`.
- Keep reusable helpers in `shared/` and course-specific scripts in the course folder that owns them.

See `docs/TOOLING.md` for the repository toolchain details.
