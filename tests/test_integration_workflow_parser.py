import pytest
import os
import sys

# Add the root of the project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.functions.parse_workflow import parse_workflow

def test_workflow_parser_integration():
    """
    Integration test for the WorkflowParser node.
    This test uses example_workflow.md to verify that the parser
    correctly extracts all the defined fields.
    """
    workflow_file_path = "project_docs/workflows/example_workflow.md"

    assert os.path.exists(workflow_file_path), f"Workflow file not found at {workflow_file_path}"

    with open(workflow_file_path, 'r') as f:
        workflow_content = f.read()

    result = parse_workflow(workflow_content)

    print("\nIntegration Test Results:")
    print(f"Result: {result}")

    assert result["success"] is True, "Parsing failed"
    assert result["result"]["action"] == "llm-call"
    assert result["result"]["llm"] == "openai/gpt-4"
    assert result["result"]["prompt"] == '"Tell me a 1 sentence dad joke."'
    assert result["result"]["output"] == "project_docs/assets/dad_joke.txt"
    assert result["result"]["description"] == '"Call an LLM to generate a single dad joke and save it to a file."'

    print("Integration test completed successfully!") 