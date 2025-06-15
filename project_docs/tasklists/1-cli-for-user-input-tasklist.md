## 1. CLI for User Input

Implement a command-line interface (CLI) to accept a user's text prompt, as detailed in FR1.1 and TR1.3.

- [ ] 1 [TASK] Setup Typer for CLI argument parsing.
- [ ] 2 [WORKFLOW] Create a CLI workflow in `src/workflows/cli.py`.
    - [ ] 2.1 [FUNCTION] Implement a function `prompt_for_user_input()` in `src/functions/cli.py` to handle user input.
        - Description: Prompts the user for text input from the command line.
        - Parameters: None
        - Returns: string (the user's input)
    - [ ] 2.2 [WORKFLOW INTEGRATION TEST] Create a test `tests/test_cli_workflow.sh` to verify the CLI workflow. 