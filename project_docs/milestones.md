## Milestones

- [ ] 1. CLI for User Input
    Implement a command-line interface (CLI) to accept a user's text prompt, as detailed in FR1.1 and TR1.3.

- [ ] 2. Gemini API Integration
    Integrate with the Google Gemini API to send the user's prompt and receive a response (FR1.2, TR1.2).

- [ ] 3. Core Workflow as LangGraph
    Implement the core application logic as a LangGraph graph, connecting the CLI input, API interaction, and file output (FR1.5, TR1.1).

- [ ] 4. Response Handling and Output
    Process the response from the Gemini API and save it to a new markdown file (FR1.3, FR1.4).
    **Note:** For the output markdown file naming convention, we'll use `response_yyyymmdd.md` format for now (e.g., `response_20240615.md`). This is just to ensure the proof of concept is working properly.

- [ ] 5. Basic Server Implementation
    Create a basic server to host and execute the LangGraph graph, enabling the system to run as a server-based application (FR1.6, US3).

## Out Of Scope
The following items are out of scope for the initial MVP, as defined in the PRD:

- [ ] Advanced workflow customization and configuration.
- [ ] Agent context management.
- [ ] Job scheduling and automation features.
- [ ] Support for any AI models besides Gemini.
- [ ] A graphical user interface (GUI). 