## 3. Core Workflow as LangGraph

Implement the core application logic as a LangGraph graph, connecting the CLI input, API interaction, and file output (FR1.5, TR1.1).

- [ ] 1 [TASK] Add `langgraph` to the project dependencies.
- [ ] 2 [WORKFLOW] Create the main application workflow as a LangGraph graph in `src/workflows/main_workflow.py`.
    - Description: This workflow will orchestrate the entire process from user input to file output.
    - [ ] 2.1 [FUNCTION] Integrate the `prompt_for_user_input()` function from milestone 1.
    - [ ] 2.2 [FUNCTION] Integrate the `send_prompt_to_gemini()` function from milestone 2.
    - [ ] 2.3 [FUNCTION] Create a new function `save_response_to_file(response: str)` in `src/functions/file_io.py`.
        - > ⚠️ **TBC:** This function will be fully implemented in the next milestone. For now, a placeholder is sufficient.
    - [ ] 2.4 [WORKFLOW INTEGRATION TEST] Create a test `tests/test_main_workflow.sh` to verify the end-to-end LangGraph workflow. 