# Copilot instructions for this repository

## Repository overview

This repository is a very small Python utility workspace with two top-level modules:

- `calculator.py` contains basic arithmetic helpers (`add` and `subtract`).
- `data_converter.py` is present in the repo root but currently empty.

There is no application framework, package structure, or build system configuration in the repository right now. The repo does not include a README, package manifest, test suite, or lint configuration, so instructions should be minimal and reflect the current state.

## Build, test, and lint commands

There is currently no automated build, test, or lint configuration in this repository.

- No `pyproject.toml`, `setup.cfg`, `tox.ini`, `requirements.txt`, or `pytest.ini` file is present.
- No tests are currently checked in.
- If a Python script is intended to be executed directly, run it with:
  - `python calculator.py`
  - `python data_converter.py`

When the repository grows and adds a formal Python test runner, prefer the project’s declared command in the relevant config file rather than inventing a new one.

## High-level architecture

The current architecture is intentionally simple:

- `calculator.py` is a standalone utility module exposing pure functions for arithmetic operations.
- `data_converter.py` is intended as a sibling utility module and may evolve independently without a shared framework or service layer.

The codebase does not currently have layered architecture, dependency injection, data models, or service boundaries. Treat it as a small collection of Python scripts rather than a packaged application.

## Key conventions

- Keep modules at the repository root unless the project grows into a package structure.
- Prefer simple, pure Python functions over application state and side effects.
- Because there is no existing test or lint infrastructure, maintain compatibility with the standard Python runtime and avoid adding project-specific tooling unless the repository later adopts it.
- If `data_converter.py` is expanded, keep its behavior consistent with the repository’s lightweight script-based style rather than introducing framework patterns that are not yet present.

## Notes for future Copilot sessions

- Do not assume a package layout, build step, or test framework exists unless a new configuration file is added.
- When editing Python files in this repo, keep changes minimal and compatible with the current top-level script pattern.
- If a future README or config appears, prefer those documented commands over the guidance in this repository-specific instruction file.
