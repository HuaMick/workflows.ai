#!/bin/bash

# Exit on error
set -e

echo "Updating Python dependencies with uv..."

# This script assumes it is run from the project root, where pyproject.toml is located.

# Ensure .local/bin is in the PATH to find uv if not in a venv
export PATH="$HOME/.local/bin:$PATH"

# 1. Check for uv command
if ! command -v uv &> /dev/null; then
    echo "Error: 'uv' command not found."
    echo "Please ensure uv is installed and in your PATH."
    echo "You may need to run 'scripts/init_uv.sh' first."
    exit 1
fi

# 2. Check for pyproject.toml
if [ ! -f "pyproject.toml" ]; then
    echo "Error: pyproject.toml not found in the current directory."
    exit 1
fi

# 3. Check for virtual environment
if [ ! -d ".venv" ]; then
    echo "Error: Virtual environment '.venv' not found."
    echo "Please run 'scripts/init_uv.sh' to create the environment."
    exit 1
fi

# 4. Sync dependencies
echo "Syncing dependencies from pyproject.toml..."
uv pip sync pyproject.toml

echo "Dependencies are up to date."
