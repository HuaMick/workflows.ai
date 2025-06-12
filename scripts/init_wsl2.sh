#!/bin/bash

# Exit on error
set -e

echo "Setting up WSL2 development environment..."

# Install Nix if not already installed
if ! command -v nix &> /dev/null; then
    echo "Installing Nix..."
    sh <(curl -L https://nixos.org/nix/install) --daemon
    # Source nix environment
    . ~/.nix-profile/etc/profile.d/nix.sh
fi

# Create necessary directories if they don't exist
mkdir -p tests
mkdir -p nix

# Create shell.nix if it doesn't exist
if [ ! -f "nix/shell.nix" ]; then
    echo "Creating shell.nix..."
    cat > nix/shell.nix << 'EOF'
{ pkgs ? import <nixpkgs> {} }:

let
  pythonEnv = pkgs.python3.withPackages (ps: with ps; [
    # Testing
    pytest
    pytest-cov
    pytest-mock
    
    # Development tools
    black
    mypy
    ruff
  ]);
in

pkgs.mkShell {
  buildInputs = with pkgs; [
    # Python environment
    pythonEnv
    
    # Development tools
    black
    mypy
    ruff
    
    # Git
    git
  ];

  shellHook = ''
    # Set up Python path
    export PYTHONPATH=$PWD/src:$PYTHONPATH
  '';
}
EOF
fi

# Create test scripts if they don't exist
if [ ! -f "tests/example_test_unit.sh" ]; then
    echo "Creating example_test_unit.sh..."
    cat > tests/example_test_unit.sh << 'EOF'
#!/bin/bash

# Ensure we're in the Nix development environment
nix-shell nix/shell.nix --command "python -m pytest tests/example_test_unit.py::test_example_function_operation -v --tb=short"
EOF
fi

if [ ! -f "tests/example_test_integration.sh" ]; then
    echo "Creating example_test_integration.sh..."
    cat > tests/example_test_integration.sh << 'EOF'
#!/bin/bash

# Ensure we're in the Nix development environment
nix-shell nix/shell.nix --command "python -m pytest tests/example_test_integration.py::test_example_integration -v -s --capture=no --tb=short"
EOF
fi

echo "Setup complete! You can now run the tests using:"
echo "./tests/example_test_unit.sh"
echo "./tests/example_test_integration.sh"

