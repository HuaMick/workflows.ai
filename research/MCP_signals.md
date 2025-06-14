# MCP Server Signaling Mechanisms

This document outlines options for how a primary AI agent can signal the Master Control Program (MCP) server to initiate a workflow, such as the QA process. This decision is a key part of Milestone 3.

## Background: How Agent Tool Calls Work

In modern AI agent frameworks, a "tool" is essentially a function or an API that the agent can decide to call to interact with the outside world. The agent's underlying language model is trained to recognize when a user's request requires a specific capability that it doesn't possess on its own (e.g., accessing a live website, reading a file, or in our case, triggering a process).

When the model determines a tool is needed, it typically outputs a specific, structured format (like JSON) that specifies the tool's name and the parameters to use. The agent's orchestration code then parses this output, executes the corresponding function in the host programming language, and can even return the result back to the model.

For our use case, the primary agent would be given a tool, let's call it `trigger_qa_workflow`. The core of our task is to define what happens when this `trigger_qa_workflow` function is executed by the agent's runtime.

---

## Signaling Options

Here are the primary technical options for implementing the `trigger_qa_workflow` tool.

### 1. HTTP API Endpoint (Recommended)

The MCP server runs a lightweight web server (e.g., using Flask or FastAPI in Python) and exposes a specific endpoint, such as `POST /trigger`.

-   **How it Works:** The `trigger_qa_workflow` tool is a simple function that makes an HTTP POST request to `http://localhost:PORT/trigger`. The body of the request could contain optional parameters if needed in the future.
-   **Pros:**
    -   **Standard and Mature:** HTTP is the lingua franca of network communication. It's well-understood, robust, and has excellent library support in all languages.
    -   **Decoupled:** The agent and the MCP server don't need to know about each other's internal implementation, only the API contract. They can be developed, deployed, and scaled independently.
    -   **Easy to Test:** Endpoints can be easily tested with standard tools like `curl` or Postman.
    -   **Flexible:** Easily extendable to pass data (e.g., a session ID, file paths) as a JSON payload.
-   **Cons:**
    -   **Slightly More Overhead:** Involves setting up a web server, which adds a small amount of complexity compared to a file-based approach.

### 2. Message Queue

The agent and the MCP server communicate via a message broker like Redis (using its Pub/Sub feature), RabbitMQ, or a cloud-based service like AWS SQS.

-   **How it Works:** The `trigger_qa_workflow` tool publishes a message to a specific channel or queue (e.g., `mcp-triggers`). The MCP server is a subscriber to this channel and reacts when a new message appears.
-   **Pros:**
    -   **Highly Decoupled & Scalable:** This is a very robust pattern for asynchronous communication. It allows for multiple agents to publish triggers and multiple MCP workers to process them.
    -   **Resilient:** Message queues can typically handle backpressure and temporary downtime of the consumer (MCP server).
-   **Cons:**
    -   **Infrastructure Dependency:** Requires setting up and managing a message broker, which adds significant operational complexity for a simple use case.
    -   **Overkill for a POC:** This is likely too complex for the initial proof-of-concept.

### 3. File-based Trigger

The agent signals the MCP server by creating or modifying a file in a specific, shared directory.

-   **How it Works:** The MCP server continuously watches a directory (e.g., `/tmp/mcp_triggers/`). The `trigger_qa_workflow` tool's implementation is simply `touch /tmp/mcp_triggers/qa.trigger`. The MCP server detects the new file and starts the workflow.
-   **Pros:**
    -   **Extremely Simple:** Very easy to implement on both the agent and server side.
-   **Cons:**
    -   **Brittle and Error-Prone:** Relies on the filesystem, which can have issues with permissions, race conditions, and cleanup.
    -   **Hard to Pass Data:** Passing contextual information from the agent to the server is clumsy (e.g., writing to the file).
    -   **Poor Scalability:** Does not scale well and is not a standard practice for inter-process communication in modern applications.

---

## Recommendation

For the initial implementation, the **HTTP API Endpoint** approach is strongly recommended. It strikes the best balance between simplicity, robustness, and future extensibility. It aligns with standard microservice architecture patterns and provides a solid foundation to build upon, without introducing the heavy infrastructure requirements of a dedicated message queue. 