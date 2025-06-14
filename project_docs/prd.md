## Initial description of the product

A Proof of Concept (POC) for a simple MCP server that can execute a Large Language Model (LLM) call based on a markdown workflow file and save the result to a specified output file.

## Assumptions

*   The workflow file is located in the project root.
*   The workflow file is named `workflow.md`.
*   The user has the necessary credentials to make LLM calls configured in their environment.

## Goals

*   **G1:** Execute an LLM call based on instructions in a workflow file.
*   **G2:** Save the result of the LLM call to a file.
*   **G3:** The process should be triggerable via a command-line interface.

## User Stories

*   **US1:** As a developer, I want to define an LLM call in a markdown workflow file so that I can specify the prompt and model for the AI.
*   **US2:** As a developer, I want to trigger the MCP server to execute the workflow so that I can run the LLM call on demand.
*   **US3:** As a developer, I want to see the LLM response saved to a file so that I can inspect and use the output.

## Functional Requirements

### 1. Workflow Discovery
*   **FR1.1:** The system must discover a specific workflow file (`project_docs/workflows/example_workflow.md`).
    > ⚠️ **Note:** For the initial POC, we will use a hardcoded path. We will expand to make the workflow path configurable once the POC is complete.

### 2. Workflow Parsing
*   **FR2.1:** The MCP server must parse the workflow file to extract the following components:
    - **Action:** The type of action to perform (e.g., `llm-call`)
    - **LLM:** The target language model to use (e.g., `openai/gpt-4`)
    - **Prompt:** The text prompt to send to the LLM
    - **Output:** The file path where the response should be saved
    - **Description:** (Optional) A human-readable description of the action

    > 📝 **Decision:** The workflow format will follow a structured markdown format with clearly labeled sections as shown in `project_docs/workflows/example_workflow.md`.

### 3. LLM Execution
*   **FR3.1:** The server must execute the LLM call using the parsed information.
    > 📝 **Decision:** Initially, we will only support Google's Gemini model. API keys will be managed through environment variables.

### 4. Output Storage
*   **FR4.1:** The server must save the LLM's response to the file path specified in the workflow.

## Technical Requirements

### 1. Architecture
*   **TR1.1:** The system will be built as a custom **Model Context Protocol (MCP) server**.
*   **TR1.2:** The server will run as a persistent process.

### 2. Interface
*   **TR2.1:** The MCP server will be triggered via a command-line interface.

## Out of Scope

*   Complex, multi-step workflows. The POC will only support a single LLM call per workflow.
*   Dynamic context passing into the prompt.
*   A user interface (UI). All interaction is via the CLI and file system.

## High level design choices

*   **Workflow Parser:** A simple component to parse `workflow.md`.
*   **LLM Caller:** A component responsible for making the API call to the specified LLM. 