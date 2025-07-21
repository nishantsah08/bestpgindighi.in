# Gemini Project Directives & Memories

## Core Principles
- **Iterative Workflow:** My workflow is highly iterative. I must always:
    1. Propose a clear plan, breakdown, or structure first.
    2. Await explicit user confirmation before creating or modifying files.
    3. Explain the real-world trade-offs of technical decisions.
- **Systemic Validation:** All proposed changes must be validated against the project's internal system model (`bludeprint validation tool`) for both local and global consistency, as per the project's governing documents.
- **Data & Policy Versioning:** All business logic changes must incorporate data and policy versioning to protect historical data integrity.
- **360-Degree Reporting:** When asked for project progress, I must provide a complete view, covering all aspects from design to implementation in a structured manner.
- **Ignore Directory:** The directory `bestpgindighi-ai` must be ignored as it is not part of the project.

## Response Formatting
- **Labeled Separator:** I must use a distinct horizontal rule with a label, like `--- [ Gemini Response ] ---`, to visually separate each of my responses.
- **Alternating Colors:** I will alternate my response text color between terminal default and green to improve readability.
- **Validation Status Signal:** Every response must end with a status line in blue indicating `model validation passed` or `model validation failed`, as per `docs/06_AI_INTERACTION_MODEL.md`.

---
# Mandatory Startup Procedure

On every session start within this project, I must adhere to the following sequence:

1.  **Ingest Core Governance:** Immediately perform a targeted read of the following files to load the project's constitutional rules:
    *   `constitution/00_CONSTITUTION.md`
    *   `docs/06_AI_INTERACTION_MODEL.md`
    *   `docs/03_DEVELOPMENT_WORKFLOW.md`

2.  **Activate Core Directives:** The principles from these documents are my primary operational directives, overriding any of my general defaults. The `bludeprint validation` process is now engaged.

3.  **Confirm Governance Lock:** My first response in the session must explicitly confirm that these governance protocols are loaded and active. The confirmation message shall be: "Governance protocols from CONSTITUTION.md and AI_INTERACTION_MODEL.md are loaded. Bludeprint validation is engaged. I am ready."
