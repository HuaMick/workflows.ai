## 3. LLM Caller Implementation

- [ ] 1. [NODE] Create an `LLMCaller` node. 
        This node will take the parsed workflow data, manage API key access from environment variables, and use the `call_gemini` function to execute the LLM call.
-   [ ] 1.1 [FUNCTION] Implement a `call_gemini` function.
        Takes a prompt string as input, makes a request to the Google Gemini API, and returns the text response. It should also handle potential API errors.
-   [ ] 1.2 [NODE INTEGRATION TEST] Create an integration test for the `LLMCaller` node.
        This test will use a mock prompt and verify that the node correctly calls the `call_gemini` function and handles the response. 