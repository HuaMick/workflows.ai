# Milestone 3: Core Workflow as LangGraph

*Implement the core application logic as a LangGraph graph, connecting the CLI input, API interaction, and file output (FR1.5, TR1.1).*


- [ ] 1 [TASK][Design State]
    Design the `GraphState` TypedDict that will be passed between nodes. It should at least contain the `prompt` and `response`.
- [ ] 2 [NODE][`invoke_model_node`]
    This node is responsible for calling the Gemini API.
-   [ ] 2.1 [FUNCTION][`invoke_model`]
        This function takes the state, calls the `call_gemini_api` service, and updates the state with the response.
        - **Parameters:** `state` (GraphState).
        - **Returns:** A dictionary with the updated `response` field.
-   [ ] 2.2 [NODE INTEGRATION TEST][Test `invoke_model_node`]
        Write a test to ensure the node correctly calls the model and updates the state.
- [ ] 3 [TASK][Build Graph]
    Define the nodes and edges of the LangGraph, connecting the `invoke_model_node` and the `save_response_node` (from Milestone 4).
- [ ] 4 [TASK][Compile and Test Graph]
    Compile the graph and write an integration test to verify the end-to-end workflow. 