# Dad Joke Workflow Example

This document outlines a sample workflow that can be executed by the MCP server to generate a dad joke.

## 1. Generate Dad Joke

-   **Action:** `llm-call`
-   **LLM:** `openai/gpt-4`
-   **Prompt:** "Tell me a 1 sentence dad joke."
-   **Output:** `project_docs/assets/dad_joke.txt`
-   **Description:** "Call an LLM to generate a single dad joke and save it to a file." 