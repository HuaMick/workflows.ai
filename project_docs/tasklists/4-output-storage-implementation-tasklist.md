## 4. Output Storage Implementation

- [ ] 1. [NODE] Create an `OutputStorage` node. 
        This node will take the LLM response and the output file path from the workflow data and use a function to save the response to the specified file.
-   [ ] 1.1 [FUNCTION] Implement a `save_to_file` function.
        Takes a file path and content string, and writes the content to the file. It should handle file system errors, for example, creating the directory if it doesn't exist.
-   [ ] 1.2 [NODE INTEGRATION TEST] Create an integration test for the `OutputStorage` node.
        This test will provide a mock response and an output path, and verify that the file is created with the correct content. 