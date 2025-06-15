## 5. Basic Server Implementation

Create a basic server to host and execute the LangGraph graph, enabling the system to run as a server-based application (FR1.6, US3).

- [ ] 1 [TASK] Add `fastapi` and `uvicorn` to project dependencies.
- [ ] 2 [SERVICE] Create a new FastAPI application in `src/services/server.py`.
    - Description: This service will expose an endpoint to trigger the main LangGraph workflow.
- [ ] 3 [WORKFLOW] Adapt the main workflow to be triggerable from the server.
    - Description: This might involve refactoring `main_workflow.py` to be callable as a function.
- [ ] 4 [TASK] Create a Dockerfile for the server service.
- [ ] 5 [TASK] Create a docker-compose.yml to run the server.
- [ ] 6 [WORKFLOW INTEGRATION TEST] Create a test `tests/test_server.sh` to send a request to the server and verify the workflow is executed. 