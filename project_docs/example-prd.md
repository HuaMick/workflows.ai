*The prd document should be a markdown document with extension .md*


## Intial description of the product

*This is the inital description of the product provided by the user.*

## Assumptions

*Assumptions made due to ambiguity of intial description provided*

## Goals

*List the goals of the product here.*

*   **G1:** Successfully extract data from O*NET's `Occupation.txt`, `Skills.txt`, and `Scales.txt`.
*   **G2:** Design and implement a normalized relational database schema in MySQL to store the extracted and processed data.
*   ...

## User Stories

*User narratives describing feature usage and benefits*

*   **US1 (API Consumer - HR Software):** As an HR software system, I want to call the `/skill-gap` API with two occupation codes so that I can retrieve a list of skills (including their names, IDs, and proficiency differences) required for the target occupation that the source occupation lacks or has at a lower level, enabling me to guide employee development or assess candidate suitability.
*   **US2 (Data Engineer):** As a Data Engineer, I want the ETL process to be idempotent and robust, correctly handling data extraction, transformation (including LLM-based proficiency scoring), and loading, so that the database is reliably populated with accurate O*NET data.
*   ...

## Functional Requirements

*Specific functionalities the feature must have. Number these requirements*

### 1 Data Extraction
*   **FR1.1:** The system must download or use local copies of `Occupation Data (Occupation.txt)`, `Skills (Skills.txt)`, and `Scales (Scales.txt)` from the O*NET website/provided files as the primary source for initial data population. 

*   **FR1.2:** If occupation data is not available in the local db then data is fetched using the public O*NET API.

*   ...

## Technical Requirements

*If specific technologies or tools are mentioned as requirements, list them here. Number these requirements*

### 1 Database
*   **TR1.1:** MySQL must be used for the local db.

*   ...

## Out of Scope

*Clearly state what this feature will not include to manage scope*

## High level design choices

*Link to mockups, describe UI/UX requirements, or mention relevant components/styles if applicable.*