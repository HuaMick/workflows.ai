#!/bin/bash
# Example entrypoint script for Python API Service
# This script launches the API service using environment variables

set -e

# Use environment variables with defaults
HOST=${API_HOST:-0.0.0.0}
PORT=${API_PORT:-8000}

echo "Starting API service on $HOST:$PORT"

# Launch the application using uvicorn
exec uvicorn src.api.main:app --host "$HOST" --port "$PORT"
