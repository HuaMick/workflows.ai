## 2. Workflow Parser Implementation

- [ ] 1. [NODE] Create a `WorkflowParser` node. This node will be responsible for taking a workflow file path, reading the content, and using a parsing function to extract the workflow details.
-   [ ] 1.1 [FUNCTION] Implement a `parse_workflow` function. 
        Takes the string content of a workflow file, parses the markdown to extract `Action`, `LLM`, `Prompt`, `Output`, and `Description`, and returns a structured object.
-   [ ] 1.2 [NODE INTEGRATION TEST] Create an integration test for the `WorkflowParser` node. 
        This test will use the `example_workflow.md` to verify that the parser correctly extracts all the defined fields. 