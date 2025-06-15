## 4. Response Handling and Output

Process the response from the Gemini API and save it to a new markdown file (FR1.3, FR1.4).
**Note:** For the output markdown file naming convention, we'll use `response_yyyymmdd.md` format for now (e.g., `response_20240615.md`). This is just to ensure the proof of concept is working properly.

- [ ] 1 [WORKFLOW] Enhance the response handling in the main workflow.
    - [ ] 1.1 [FUNCTION] Fully implement the `save_response_to_file(response: str)` function in `src/functions/file_io.py`.
        - Description: Saves the given response text to a markdown file.
        - Parameters: `response` (string)
        - Returns: None
        - Note: The filename should be in the format `response_yyyymmdd.md`.
    - [ ] 1.2 [WORKFLOW INTEGRATION TEST] Update the test `tests/test_main_workflow.sh` to verify that the file is created with the correct content and filename. 