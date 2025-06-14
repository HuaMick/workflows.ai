# How an Agent Knows When and How to Call a Tool

The ability of an AI agent to use tools doesn't come from traditional `if-then-else` programming. Instead, it's an emergent capability derived from the underlying Large Language Model's (LLM) training and the specific information it's given about the tools at its disposal.

The process can be broken down into two main parts: **1. The Tool Definition (The "Menu")** and **2. The Model's Reasoning (The "Chef")**.

---

### 1. The Tool Definition: Providing the "Menu"

Before an agent can use a tool, the developer must explicitly tell it that the tool exists. This is done by providing a "tool definition" or schema, which acts like a menu of available actions. This definition is provided to the agent system (e.g., via an API call to OpenAI, Anthropic, or a local model) at the beginning of a conversation.

This definition typically includes:

-   **Tool Name:** A clear, descriptive name for the tool, like `trigger_qa_workflow`.
-   **Description:** A detailed, natural language explanation of what the tool does, why it exists, and when it should be used. **This is the most critical part.** The model relies heavily on this description to decide *when* to use the tool. A good description might be: *"Triggers a quality assurance (QA) workflow on the codebase. This should be used after new code has been written or existing code has been changed to verify its correctness."*
-   **Parameters:** A structured definition of the arguments the tool accepts, including their names, data types (e.g., string, integer, boolean), and whether they are required. For a simple trigger, the parameters might be empty. For a more complex tool, you might define a parameter like `session_id` (a string) or `run_all_tests` (a boolean). This is often defined using a format like JSON Schema.

**Example Tool Definition (Conceptual):**

```json
{
  "name": "trigger_qa_workflow",
  "description": "Triggers an automated quality assurance (QA) workflow. Use this after making changes to the code to run tests and checks.",
  "parameters": {
    "type": "object",
    "properties": {},
    "required": []
  }
}
```

This entire definition is injected into the "system prompt" or context that the LLM processes with every user request.

### 2. The Model's Reasoning: Deciding How and When to Order

The LLM at the heart of the agent has been specifically trained (a process called "fine-tuning") on vast amounts of text and code. This training allows it to be exceptionally good at pattern matching and "intent recognition."

-   **"When" to Make the Call:** The model doesn't "know" in a human sense. Instead, when it processes the user's prompt (e.g., "Okay, the changes are done, please run the tests"), it analyzes this text against the descriptions of the tools it has been given. It calculates that the user's intent has a very high probability of matching the description for the `trigger_qa_workflow` tool. Its training has taught it that when a user request maps closely to a tool's purpose, the correct action is to "call" that tool.

-   **"How" to Structure the Call:** The fine-tuning process also trains the model to generate a specific, structured output when it decides to use a tool. It learns to generate a JSON object that perfectly matches the `name` and `parameters` defined in the tool's schema.

So, when the user says "run the tests," the LLM doesn't respond with plain text. Instead, its raw output would look something like this:

```json
{
  "tool_call": {
    "name": "trigger_qa_workflow",
    "arguments": {}
  }
}
```

The agent's orchestration code (the application logic wrapping the LLM) is designed to look for this specific `tool_call` structure in the model's output. When it sees it, it intercepts this message, parses the JSON, and then executes the actual application code that is mapped to the `trigger_qa_workflow` name—in our case, making the HTTP request to the MCP server. 