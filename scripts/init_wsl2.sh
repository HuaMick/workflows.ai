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

