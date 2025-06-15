#!/bin/bash

# Exit on error
set -e

echo "Setting up Python development environment with uv on WSL2..."

# 1. Install prerequisites (python, pip, etc.)
# This may require passwordless sudo to be configured.
if ! command -v python3 &> /dev/null || ! command -v pip3 &> /dev/null; then
    echo "Installing Python and Pip..."
    sudo -n apt-get update
    sudo -n apt-get install -y python3 python3-pip python3-venv
fi

# 2. Install uv
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    pip3 install --user uv
fi

# Ensure .local/bin is in the PATH for this script's session
export PATH="$HOME/.local/bin:$PATH"


# 3. Check for pyproject.toml
if [ ! -f "pyproject.toml" ]; then
    echo "Error: pyproject.toml not found!"
    echo "Please create a pyproject.toml file before continuing."
    echo "This file should define your project's metadata and dependencies."
    exit 1
fi

# 4. Create a virtual environment with uv
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    uv venv
else
    echo "Virtual environment .venv already exists."
fi

# 5. Sync dependencies
echo "Syncing dependencies from pyproject.toml..."
uv pip sync pyproject.toml


# 6. Provide activation instructions
echo ""
echo "Setup complete!"
echo "To activate the virtual environment, run:"
echo "source .venv/bin/activate"
echo ""
echo "Dependencies are up to date."
