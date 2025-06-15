# Scripts Manifest

This document provides a manifest of the scripts located in this directory, intended for indexing and use by AI agents. Each entry includes the script's name and a concise description of its function.

---

### `init_uv.sh`

**Description:** Sets up a Python development environment on WSL2 using the `uv` package manager. This script handles the installation of `python3`, `pip3`, and `uv`. It then creates a virtual environment `.venv` in the project root and verifies the presence of a `pyproject.toml` file. This is the first script to run for setting up the Python environment.

---

### `init_pydependancies.sh`

**Description:** Synchronizes the Python project dependencies based on the `pyproject.toml` file. This script uses `uv pip sync` to install or update packages within the existing `.venv` virtual environment. It should be run after the environment has been set up by `init_uv.sh`.

---

### `init_gitmodules.sh`

**Description:** Initializes and updates all git submodules for the repository. This script runs `git submodule init` followed by `git submodule update` to ensure that any submodules are correctly cloned and checked out to the specified commit.

---
