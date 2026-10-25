# Changelog

## [0.1.4] - 2026-10-25

### Fixed
- Dashboard assets ship inside the package (`resk_mcp/static/`) and are
  declared as package data, so the UI works from an installed wheel. The
  0.1.0 release looked for a sibling `static/` directory that never exists
  under `site-packages` (“Dashboard HTML not found.”).
- `setup.py` metadata aligned with `pyproject.toml`: Python >=3.11, current
  dependency floors, real repository and documentation URLs, 3.11–3.13
  classifiers.

### CI
- flake8 ignores `.venv`, which crashed pyflakes with a RecursionError.
