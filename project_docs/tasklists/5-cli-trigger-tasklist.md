## 5. CLI Trigger

- [ ] 1. [TASK] Set up the main application entrypoint (`main.py` or similar). This script will orchestrate the full workflow from parsing to execution and storage.
    > ⚠️ **Note:** Post-POC, the main entrypoint can be extended to handle multiple workflows.
- [ ] 2. [NODE] Create the `promptLLMandStore` node. This will be the core of the application, bringing together the `WorkflowParser`, `LLMCaller`, and `OutputStorage` nodes to execute the end-to-end workflow.
- [ ] 3. [CLASS] Implement a `CLI` class. This class will use a library like `argparse` or `click` to define the command-line interface. It should accept a command to trigger the workflow execution.
    > ⚠️ **Note:** For the initial POC, the CLI will use a hardcoded path to the workflow file.
- [ ] 4. [NODE INTEGRATION TEST] Create an end-to-end integration test. This test will invoke the CLI to run the full workflow using the `example_workflow.md` and verify that the output file is created with the expected content.
- [ ] 5. [SERVICE] Define a `Dockerfile` for the MCP server to containerize the application and its dependencies.
- [ ] 6. [SERVICE] Create a `docker-compose.yml` file to define the MCP server as a service, making it easy to run. 