## Milestones

- [ ] 1. **MCP Server Setup**
    Create the basic MCP server that can run as a persistent process, listening for a signal to trigger the QA workflow. This covers the core technical requirements for the system's foundation.
- [ ] 2. **Workflow Discovery**
    Implement the logic for the server to discover the `qa-workflow.md` file within the project root. This enables the system to locate the user-defined QA instructions.
- [ ] 3. **Expose Triggering Mechanism**
    Expose a tool or mechanism that the AI assistant can call upon completion of its tasks. This is the entry point for initiating the QA workflow.
    - - - > ⚠️ **TBC:** What is the exact mechanism for the primary agent to signal the MCP server? An explicit tool call is mentioned, but this needs to be confirmed.
- [ ] 4. **Workflow Parsing and Execution**
    Build the workflow parser to interpret the `qa-workflow.md` file and execute the defined actions. This brings the QA automation to life.
    - - - > ⚠️ **TBC:** The exact format for the `qa-workflow.md` file needs to be defined.

## Out Of Scope

- [ ] **Complex, multi-step workflows**
    The initial version will not support persistent, stateful workflows with advanced features like automatic retries or complex dependency chains.
- [ ] **Prompt engineering analytics**
    The system will not log detailed prompt/response data for performance analysis or provide a diagnostics interface.
- [ ] **Scheduled or recurring tasks**
    The QA workflow will only be triggered after an agent interaction, not on a time-based schedule.
- [ ] **Dynamic Context Passing**
    The QA agent will not receive dynamic context (e.g., file diffs or state snapshots) from the primary agent's actions in this POC. 