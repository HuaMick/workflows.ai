## 2. Gemini API Integration

Integrate with the Google Gemini API to send the user's prompt and receive a response (FR1.2, TR1.2).

- [ ] 1 [TASK] Add `google-generativeai` to the project dependencies.
- [ ] 2 [TASK] Create a configuration file for the Gemini API key.
- [ ] 3 [WORKFLOW] Create a workflow to interact with the Gemini API.
    - [ ] 3.1 [FUNCTION] Implement a function `send_prompt_to_gemini(prompt: str)` in `src/functions/gemini.py`.
        - Description: Sends a text prompt to the Google Gemini API and returns the response.
        - Parameters: `prompt` (string)
        - Returns: string (the API's response)
    - [ ] 3.2 [WORKFLOW INTEGRATION TEST] Create a test `tests/test_gemini_integration.sh` to verify the Gemini API integration. 