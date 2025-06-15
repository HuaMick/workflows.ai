import re

def parse_workflow(workflow_content: str):
    """
    Parses the string content of a workflow file to extract details.

    Args:
        workflow_content: The string content of the workflow file.

    Returns:
        A dictionary with success status, a message, and the parsed result.
        The result is a dictionary with the extracted workflow details.
    """
    try:
        workflow_details = {}
        # Regex to find lines like "-   **Action:** `llm-call`"
        pattern = re.compile(r"-\s+\*\*(.*?):\*\*\s+`?(.*?)`?$")

        for line in workflow_content.splitlines():
            match = pattern.search(line)
            if match:
                key = match.group(1).strip()
                value = match.group(2).strip()
                workflow_details[key.lower()] = value

        if not workflow_details:
            return {"success": False, "message": "No workflow details found in content.", "result": {}}

        return {"success": True, "message": "Workflow parsed successfully.", "result": workflow_details}

    except Exception as e:
        return {"success": False, "message": f"An error occurred during parsing: {e}", "result": {}} 