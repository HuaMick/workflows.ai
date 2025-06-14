## Initial description of the product

This document outlines the requirements for a Proof of Concept (POC) of an MCP server that can trigger a background QA agent after each interaction with the primary AI assistant.

## Assumptions

*   The user has a Cursor IDE environment where this will be integrated.
*   The `qa-workflow.md` will be in the project root.
*   The primary AI assistant has a way to call a tool exposed by the MCP server.

## Goals

*   **G1:** An MCP server that can trigger a QA agent in the background.
*   **G2:** The system must discover a specific QA workflow file (e.g., `qa-workflow.md`) within the project root.
*   **G3:** The MCP server must expose a tool or mechanism that the AI assistant can call upon completion of its tasks.
*   **G4:** The server will then execute the QA workflow defined in the markdown file.

## User Stories

*   **US1:** As a developer and cursor user, I want to be able to define a workflow in a markdown file that will get triggered after each agent call.

## Functional Requirements

*   **FR1.1:** The system must discover a specific QA workflow file (e.g., `qa-workflow.md`) within the project root.
*   **FR1.2:** The MCP server must expose a tool or mechanism that the AI assistant can call upon completion of its tasks.
    > ⚠️ **TBC:** What is the exact mechanism for the primary agent to signal the MCP server? An explicit tool call is mentioned, but this needs to be confirmed.
*   **FR1.3:** The server will then execute the QA workflow defined in the markdown file.
*   **FR1.4:** As a POC the the QA agent will execute predefined tasks that don't require context from the primary AI assistant.
*   **FR1.5:** The `qa-workflow.md` file will contain the instructions for the QA agent. The format should be simple, human-readable markdown that the parser can easily interpret.
    > ⚠️ **TBC:** The exact format for the `qa-workflow.md` file needs to be defined.

## Technical Requirements

*   **TR1.1:** The system will be a custom **Model Context Protocol (MCP) server**.
*   **TR1.2:** The MCP server will be the core of the system, running as a persistent process, listening for a signal to trigger the QA workflow.
*   **TR1.3:** A workflow parser component is required to parse the `qa-workflow.md` file and translate its contents into executable actions.

## Out of Scope

*   **Complex, multi-step workflows:** The initial version will not support persistent, stateful workflows with advanced features like automatic retries or complex dependency chains. The focus is on a single, post-interaction QA task.
*   **Prompt engineering analytics:** The system will not log detailed prompt/response data for performance analysis or provide a diagnostics interface.
*   **Scheduled or recurring tasks:** The QA workflow will only be triggered after an agent interaction, not on a time-based schedule.
*   **Dynamic Context Passing:** For this POC, the QA agent will execute predefined tasks and will not receive dynamic context (e.g., file diffs or state snapshots) from the primary agent's actions. This advanced capability, as detailed in the research on context passing, is a goal for future iterations.

## High level design choices

*   **MCP Server:** The core of the system, running as a persistent process.
*   **Workflow Parser:** A simple component to parse the `qa-workflow.md` file. 