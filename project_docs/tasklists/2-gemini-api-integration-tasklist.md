# Milestone 2: Gemini API Integration

*Integrate with the Google Gemini API to send the user's prompt and receive a response (FR1.2, TR1.2).*


- [ ] 1 [TASK][Setup Gemini API]
    Set up a Google Cloud project, enable the Gemini API, and obtain API credentials.
- [ ] 2 [SERVICE][Gemini Service]
    A service module to encapsulate all interactions with the Gemini API.
-   [ ] 2.1 [FUNCTION][`call_gemini_api`]
        This function sends a prompt to the Gemini API and returns the response.
        - **Parameters:** `prompt` (string).
        - **Returns:** The raw response from the Gemini API as a string.
-   [ ] 2.2 [TASK][Implement Gemini Service]
        Implement the `call_gemini_api` function, including authentication and error handling.
-   [ ] 2.3 [TASK][Write unit tests]
        Write unit tests for the Gemini Service, mocking the API calls to test response and error handling. 