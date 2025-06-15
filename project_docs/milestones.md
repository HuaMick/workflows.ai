## Milestones

- [x] 1. **Initial Setup & Workflow Definition**
    Define the project structure and the format for `workflow.md` based on the product requirements.
- [x] 2. **Workflow Parser Implementation**
    Create a parser to read and extract actions, parameters, and output paths from `workflow.md`.
- [ ] 3. **LLM Caller Implementation**
    Implement the functionality to execute a call to the specified LLM (initially Google Gemini) using the parsed prompt.
- [ ] 4. **Output Storage Implementation**
    Develop the logic to save the LLM response to the file specified in the workflow.
- [ ] 5. **CLI Trigger**
    Build a command-line interface to start the MCP server and trigger the workflow execution.

## Out Of Scope

- [ ] **Complex Workflows**
    Support for multi-step workflows is out of scope for the POC.
- [ ] **Dynamic Context**
    Passing dynamic context into the prompt is not supported in this version.
- [ ] **User Interface**
    A graphical user interface is not part of the initial scope. 