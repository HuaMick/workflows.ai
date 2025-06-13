# Project Technology Stack

## Core Technologies

### Package Management & Environment
- **Nix**: Primary package and environment management system
- **uv2nix**: Python package management integration with Nix
- **Python 3.12**: Core programming language

### Build System
- **pyproject.nix**: Nix integration for Python projects
- **hatchling**: Python build backend

### Testing Framework
- **pytest**: Core testing framework

## Infrastructure

### Development Environment
- **flake-utils**: Nix flake utilities for multi-system support
- **pyproject-build-systems**: Build system integration for Python packages

## Notes
- The project uses a Nix-based development environment for reproducible builds
- Python package management is handled through uv2nix, integrated with Nix
- Testing is implemented using pytest
- Build system is configured using hatchling and pyproject.nix 