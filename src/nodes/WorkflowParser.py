"""
This node parses a workflow file and returns the extracted details.
"""

import sys
import os

# Add the root of the project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.functions.parse_workflow import parse_workflow

def main():
    """
    Parses a workflow file and prints the extracted details.
    """
    print("Starting WorkflowParser node...")

    if len(sys.argv) < 2:
        print("Error: Please provide the path to the workflow file.")
        sys.exit(1)

    workflow_file_path = sys.argv[1]

    if not os.path.exists(workflow_file_path):
        print(f"Error: File not found at '{workflow_file_path}'")
        sys.exit(1)

    print(f"Parsing workflow file: '{workflow_file_path}'")

    try:
        with open(workflow_file_path, 'r') as f:
            workflow_content = f.read()

        result = parse_workflow(workflow_content)

        if not result['success']:
            print(f"Error parsing workflow: {result['message']}")
            sys.exit(1)

        print("Workflow parsed successfully.")
        print("Result:")
        for key, value in result['result'].items():
            print(f"  {key}: {value}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

    print("\nWorkflowParser node process completed successfully.")

if __name__ == '__main__':
    main() 