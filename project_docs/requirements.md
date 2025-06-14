# AI-Powered Dad Joke Generator (Proof of Concept)

This document outlines the requirements for a Proof of Concept (POC) of a simple MCP server that makes LLM calls.

## 1. Core Feature: LLM Call Execution

**Goal:** An MCP server that can execute an LLM call based on a workflow file and save the result.

**User Stories:**

*   As a developer, I want to define an LLM call in a markdown workflow file.
*   As a developer, I want to trigger the MCP server to execute the workflow.
*   As a developer, I want to see the LLM response saved to a file.

**Functional Requirements:**

*   The system must discover a specific workflow file (e.g., `workflow.md`) within the project root.
*   The MCP server must parse the workflow file to get the LLM, prompt, and output file path.
*   The server will then execute the LLM call.
*   The server will save the LLM's response to the specified output file.

## 2. Technical Approach & Architecture

The proposed architecture is to build this system as a custom **Model Context Protocol (MCP) server**.

### Key Architectural Components:

*   **MCP Server:** The core of the system, running as a persistent process. It will be triggered via command line.
*   **Workflow Parser:** A simple component to parse the `workflow.md` file and translate its contents into executable actions.
*   **LLM Caller:** A component responsible for making the API call to the specified LLM.

### Implementation Considerations:

*   **Trigger Mechanism:** The MCP server will be triggered via a command line interface.
*   **Workflow Definition:** The `workflow.md` file will contain the instructions. The format should be simple, human-readable markdown. See [example_workflow.md](./assets/example_workflow.md) for a reference implementation.

## 3. Out of Scope

*   **Complex, multi-step workflows:** The initial version will only support a single LLM call.
*   **Dynamic Context Passing:** The prompt will be statically defined in the workflow file.
*   **User Interface:** There will be no UI, interaction is via CLI and file inspection.