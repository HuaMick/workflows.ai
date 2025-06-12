# Context Passing for Multi-Agent Workflows

Passing context from a primary AI assistant to a subsequent Quality Assurance (QA) agent is crucial for the QA agent to understand what changes to verify. The core challenge lies in capturing the "after" state from the primary AI's work and making it available to the QA agent. This document outlines common strategies for achieving this.

## Strategies for Context Passing

Here are three common strategies and mechanisms for passing context:

### 1. State Snapshot

The most straightforward approach is to take a complete snapshot of the relevant data or environment after the primary AI assistant has finished its task.

**How it works:** The Main Control Program (MCP) server saves the entire state of the files, database, or any other resources modified by the first agent. This snapshot is then loaded into the QA agent's environment.

**Example:** If the primary AI's task was to write code in a file, the MCP server would save the entire modified file. The QA agent then receives this complete file to perform its checks.

**Advantages:**
- Simple to implement.
- Ensures the QA agent has the full picture.

**Disadvantages:**
- Can be inefficient if the changes are small within a large context.

### 2. Diff or Patch

A more efficient method is to capture only the changes made by the primary AI assistant, similar to how version control systems like Git track changes.

**How it works:** The MCP server compares the state of the project before and after the primary AI's execution. This generates a "diff" or "patch" file that only contains the modifications. The QA agent is then provided with both the original state and this diff.

**Example:** If the AI assistant refactors a function in a large code file, the diff would only contain the lines of code that were altered.

**Advantages:**
- Highly efficient in terms of data transfer.
- Allows the QA agent to focus its attention on the specific changes.

**Disadvantages:**
- Can be more complex to implement and apply the diff correctly in the QA agent's context.

### 3. Structured Context Object

A more sophisticated approach involves the primary AI assistant creating a structured object that encapsulates its changes. This is often managed using frameworks like LangChain or CrewAI.

**How it works:** The primary AI doesn't just perform the task; it also logs its actions and outputs into a predefined data structure (like a JSON object or a Pydantic model). This "context object" is then passed to the QA agent via the MCP server.

**Example:** An AI assistant tasked with updating a user profile in a database might output a JSON object like this:

```json
{
  "action": "update_user",
  "user_id": 123,
  "changes": {
    "email": "new.email@example.com",
    "phone_number": "555-1234"
  },
  "status": "success"
}
```

The QA agent then parses this object to understand what was changed and how to verify it.

**Advantages:**
- Provides a clear, machine-readable summary of the changes.
- Makes the QA process more robust and targeted.

**Disadvantages:**
- Requires the primary AI to be designed to produce this structured output.

## The Role of the MCP Server

The MCP server acts as the central nervous system in this workflow. It orchestrates the entire process:

1.  **Invokes the Primary Agent:** It initiates the primary AI assistant with the initial task.
2.  **Captures the Context:** Once the primary agent completes its work, the MCP server uses one of the methods above (snapshot, diff, or structured object) to capture the resulting context.
3.  **Invokes the QA Agent:** It then calls the QA agent, providing it with the captured context. This could be by passing a file, a data object, or a pointer to a shared memory location.

## The Model Context Protocol (MCP)

The emerging Model Context Protocol (MCP) standardizes this interaction. Think of it as a universal adapter for AI agents. By adhering to MCP, different agents (even from different developers) can seamlessly exchange context and data through an MCP-compliant server. This will make creating complex, multi-agent workflows much more straightforward in the future.