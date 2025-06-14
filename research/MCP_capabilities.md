# MCP Server Capabilities

This document addresses key architectural questions about the capabilities of the Master Control Program (MCP) server.

---

### 1. Can the MCP Store Information?

**Yes.** The MCP is a persistent, long-running server process, not a one-off script. As such, it can and should manage its own state. The method for storing this information can range from simple to complex, depending on the requirements.

For example, to store a "task list" derived from a workflow, the MCP could use several strategies:

-   **In-Memory Storage (Simplest):** The MCP can hold the task list in a variable (e.g., a Python list or dictionary).
    -   **Pros:** Extremely fast and simple for a single, running instance.
    -   **Cons:** The data is volatile and will be lost if the MCP server restarts. Not suitable for any critical or persistent information.

-   **File-Based Storage (Recommended for this project):** The MCP can read from and write to a file on disk (e.g., `tasks.json`, `workflow_state.yaml`).
    -   **Pros:** Provides persistence across server restarts. It's simple to implement, easy to inspect manually, and doesn't require external dependencies. This is ideal for storing the parsed QA workflow.
    -   **Cons:** Can become slow or clumsy if data is large or needs frequent, complex updates. Doesn't handle simultaneous access well (though this is not a concern for our current scope).

-   **Database:** For more advanced needs, the MCP could use a database.
    -   **Pros:** Robust, scalable, and handles transactions and concurrent access safely.
    -   **Cons:** Adds an external dependency (e.g., SQLite, PostgreSQL) and increases the project's operational complexity. This is overkill for our current needs but is a viable path for future expansion.

**Recommendation:** For the initial implementation, **file-based storage** is the most appropriate choice. The MCP will parse the `qa-workflow.md` file and can store the resulting task list in a simple JSON file that it manages.

---

### 2. Can the MCP Make its Own LLM Calls?

**Yes, absolutely.** The MCP is a standard software application (e.g., a Python program). Like any other application, it can have its own API keys and use libraries (e.g., the `openai` Python library) to communicate with an LLM.

This capability makes the MCP much more powerful than a simple script runner. It effectively becomes a secondary, specialized agent focused on orchestration and execution.

Here are a few examples of how the MCP could leverage its own LLM calls:

-   **Workflow Parsing:** Instead of writing a rigid parser for the `qa-workflow.md` file, the MCP could pass the file's contents to an LLM with a prompt like: *"Convert the following user-written QA steps into a JSON array of tasks. Each task should have a 'name' and a 'command' field. Here is the text: [contents of qa-workflow.md]"*. This makes the workflow format incredibly flexible.
-   **Result Summarization:** If a test script produces a long, verbose log file, the MCP could send the log to an LLM and ask it to *"Summarize this test failure into a single paragraph for a Slack notification."*
-   **Error Handling and Recovery:** If a step in the workflow fails, the MCP could use an LLM to analyze the error message and suggest a potential fix or a next step.

By giving the MCP its own access to an LLM, we transform it from a simple trigger-based executor into an intelligent orchestrator that can interpret, summarize, and react to events in a more sophisticated way. 

---

### 3. Can the MCP interact with the Cursor agent?

**Short answer: Not directly, but it can communicate indirectly through files.** This creates a powerful human-in-the-loop workflow.

-   **MCP to Agent (Passing Information):** The MCP server cannot directly trigger the agent or send it messages. However, it can write its status, results, or logs to a file (e.g., `run_output.json`). You can then instruct the agent to read this file, effectively passing information from the MCP to the agent.

-   **Agent to MCP (Triggering Calls):** The agent cannot start the MCP server itself. Instead, the agent can provide you with the exact terminal command needed to run the MCP with the correct parameters (e.g., `python mcp_server.py --run-test "login"`). You then execute this command.

This architecture establishes a clear separation of roles:

-   The **MCP Server** is the **executor**, running tasks in your local environment.
-   The **Cursor Agent** is the **orchestrator and analyst**, helping you generate commands and interpret results.
-   **You** are the **operator**, bridging the two by running commands and prompting the agent.

---

### 4. How are MCP workflows triggered?

**Yes, the user is the primary trigger for MCP workflows.** The MCP is designed to be a tool that you, the developer, control directly from your terminal.

The main way to trigger a workflow is by running the MCP server script with specific command-line arguments. This gives you precise control over what the MCP does and when.

For example, to have the MCP check for the existence of a `prd.md` file, you might run a command like this:

```bash
python mcp_server.py --run-task check_for_prd
```

Inside the MCP server's code, you would define a task named `check_for_prd` that looks for the `prd.md` file in the project's root directory.

This command-line interface makes the MCP:

-   **Explicit:** There's no "magic" happening in the background. You explicitly tell it what to do.
-   **Agent-Friendly:** As an agent, I can easily construct these commands for you to run, ensuring the right parameters are always used.
-   **Composable:** You can chain MCP commands with other shell commands, integrating them into larger scripts or workflows.

For more complex triggers, we could explore other mechanisms like watching for file changes or setting up a simple API, but for now, direct command-line execution is the simplest and most effective approach. 

---

### 5. Can the MCP provide instructions to the Agent?

**Yes, this is an advanced use case that is absolutely possible.** It positions the MCP as a more sophisticated orchestrator that doesn't just execute tasks, but also directs the agent on the next steps.

The mechanism follows the same file-based communication pattern:

1.  **Store Instructions:** We can create a directory, for example `project_docs/rules/`, to store instruction files in Markdown format (e.g., `generate-prd-rule.md`). These files would contain prompts or guidelines for the agent, similar to the `@documents-generate-prd.mdc` example.

2.  **MCP Identifies the Rule:** The MCP can be programmed with logic to determine when a specific instruction is needed. For instance, if a workflow to set up the project runs and it doesn't find a `prd.md`, it can conclude that the `generate-prd-rule.md` is the next logical step.

3.  **MCP Communicates the Rule:** The MCP would then write the path to this rule file into its output file (e.g., `mcp_output.json`). The output might look something like this:
    ```json
    {
      "status": "pending_action",
      "next_step": "A prd.md file is missing.",
      "agent_instructions_file": "project_docs/rules/generate-prd-rule.md" 
    }
    ```

4.  **Agent Follows Instructions:** You would then instruct me (the agent) to read the `mcp_output.json`. I would see the `agent_instructions_file` path, read the content of that file, and use it to guide you on creating the `prd.md`.

This pattern effectively allows the MCP to dynamically load context and instructions for the agent, making the entire development process more automated and intelligent. The MCP acts as a "director," telling the agent what "scene" to act out next.

---

### 6. Can the MCP modify existing files?

**Yes.** The MCP can perform all standard file system operations, including creating, reading, updating, and deleting files and directories.

When we say the MCP can "write to a file," it includes both creating a new file from scratch and modifying an existing one.

This capability is critical for many of its functions:

-   **State Management:** It can update a `status.json` file to keep track of a workflow's progress, changing a task's status from `pending` to `in_progress` to `completed`.
-   **Logging:** It can append new log entries to a `run.log` file as it executes tasks, rather than overwriting the log each time.
-   **Data Transformation:** It could read a complex data file, process it, and write the transformed data back to the same file or a new one.

This gives the MCP the full range of capabilities it needs to manage a project's files autonomously based on the workflows you define. 