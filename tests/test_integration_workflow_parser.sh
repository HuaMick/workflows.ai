#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Always use `python -m pytest` when running tests to ensure proper module resolution
# Run the test with -s flag to show print statements and -v for verbose output
python -m pytest tests/test_integration_workflow_parser.py::test_workflow_parser_integration -v -s

# Deactivate virtual environment if it was activated
if [ -n "$VIRTUAL_ENV" ]; then
    deactivate
fi 