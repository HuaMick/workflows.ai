# AI-Powered QA Agent (Proof of Concept) Task List

This document breaks down the development of the AI-Powered QA Agent into milestones, nodes, and functions.

## Functions

- **start_mcp_server**
  - description: Starts the MCP server process.
- **stop_mcp_server**
  - description: Stops the MCP server process.
- **find_workflow_file**
  - description: Searches for the `qa-workflow.md` file in the project root.
  - parameters: `root_path`
  - returns: `file_path` or `null`
- **parse_workflow_file**
  - description: Parses the markdown `qa-workflow.md` file into a list of executable tasks.
  - parameters: `file_path`
  - returns: `list_of_tasks`
- **register_qa_trigger_tool**
  - description: Registers a tool that the primary AI assistant can call to trigger the QA workflow.
- **execute_qa_task**
  - description: Executes a single, predefined QA task.
  - parameters: `task`

## Milestones

- [ ] **Milestone 1: MCP Server Foundation**
  - [ ] **Task:** Setup the basic scaffolding for the MCP server.
  - [ ] **Node:** `mcp_server_node` - Manages the lifecycle of the MCP server.
    - [ ] `start_mcp_server`
    - [ ] `stop_mcp_server`

- [ ] **Milestone 2: QA Workflow Discovery and Parsing**
  - [ ] **Node:** `workflow_discovery_node` - Finds the `qa-workflow.md` file.
    - [ ] `find_workflow_file`
  - [ ] **Node:** `workflow_parser_node` - Parses the workflow file.
    - [ ] `parse_workflow_file`

- [ ] **Milestone 3: Workflow Triggering**
  - [ ] **Node:** `workflow_trigger_node` - Exposes a mechanism for the primary AI assistant to trigger the QA workflow.
    - [ ] `register_qa_trigger_tool`
  > ⚠️ **TBC:** The PRD mentions that the trigger mechanism is a key design decision and could be an explicit tool call or a hook. This needs clarification to determine the final implementation.

- [ ] **Milestone 4: QA Agent Execution**
  - [ ] **Node:** `qa_agent_execution_node` - Executes the predefined tasks from the QA workflow.
    - [ ] `execute_qa_task` 