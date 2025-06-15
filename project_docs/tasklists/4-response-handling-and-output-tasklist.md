# Milestone 4: Response Handling and Output

*Process the response from the Gemini API and save it to a new markdown file (FR1.3, FR1.4).*


- [ ] 1 [NODE][`save_response_node`]
    This node is responsible for saving the final response to a markdown file.
-   [ ] 1.1 [FUNCTION][`_generate_filename`]
        A helper function to generate the output filename based on the current date (e.g., `response_20240615.md`).
        - **Parameters:** None.
        - **Returns:** A string with the formatted filename.
-   [ ] 1.2 [FUNCTION][`save_response`]
        This function takes the state and writes the `response` to the generated filename.
        - **Parameters:** `state` (GraphState).
        - **Returns:** None.
-   [ ] 1.3 [NODE INTEGRATION TEST][Test `save_response_node`]
        Write a test to ensure the node correctly saves the response to a file with the correct name. 