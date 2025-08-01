### **Cabinet Secretary Portal: Detailed Development Plan with Integrated Planning Commission Review**

**Overall Objective:** To develop a new, AI-powered single-page application for the Cabinet Secretary, providing a chat-like interface (similar to `chatgpt.com`) with LLM capabilities and integration with other Ministry AIs via the Model Context Protocol (MCP). The portal will also support AI-driven interaction for queries and modifications.

**Core Principles (from `.gemini/GEMINI.md`):**

*   **Iterative Workflow:** Each module will follow a design -> implement -> test -> review -> refine cycle.
*   **Systemic Validation:** All proposed changes will undergo a "planning commission review" at critical junctures, ensuring alignment with project governance (`judiciary/00_JUDICIAL_REVIEW_PROCESS.md`) and policies (`parliament_policies/`).
*   **Data & Policy Versioning:** Will be a key consideration in database and API design.
*   **360-Degree Reporting:** Progress will be reported comprehensively.

**Deployment Details:**

*   **Frontend:** Served on **Port 3000**.
*   **Backend:** Runs on **Port 8000**.
*   **Machine IP:** `34.47.243.114` (Google VPS).

---

**Module 1: Frontend Development - Cabinet Secretary Portal (Port 3000)**

*   **Objective:** Develop the user-facing chat interface, focusing on a ChatGPT-like experience.
*   **Technology:** React (TypeScript) with a modern UI library (e.g., Material UI, Bootstrap, or a custom design system based on `docs/10_DESIGN_SYSTEM.md`).
*   **Detailed Steps:**
    1.  **Initial Design & Scaffolding:**
        *   Scaffold a new React project (e.g., using `create-react-app` or Vite).
        *   Set up project structure, TypeScript configuration, and basic styling.
        *   Implement the core layout: a fixed header, a scrollable chat message display area, and a persistent input field at the bottom with a send button.
        *   Define placeholder UI components for chat messages (user and AI), input, and potential future features (e.g., AI interaction indicators).
        *   **Planning Commission Input (Design Review):** Present initial UI wireframes/mockups and the chosen UI framework/design system. Review for alignment with `docs/10_DESIGN_SYSTEM.md` and `parliament_policies/03_DEVELOPMENT_WORKFLOW.md` regarding UI/UX consistency and development practices.
    2.  **Core Chat Functionality Implementation:**
        *   Enable user input in the message field and trigger a "send" action on Enter key press or button click.
        *   Dynamically add user messages to the chat display.
        *   Implement a mechanism to display static placeholder AI responses (e.g., "Thinking..." or a hardcoded reply) immediately after a user message is sent, simulating an LLM response.
        *   Implement basic state management for the chat history.
    3.  **Frontend Unit & Integration Testing (Initial):**
        *   Write unit tests for individual React components (e.g., `ChatMessage` renders content correctly, `MessageInput` handles input and button clicks).
        *   Write integration tests to verify the interaction between components (e.g., sending a message updates the chat display).
    4.  **Planning Commission Review (Frontend Core Functionality):**
        *   Demonstrate the functional core chat UI with static/mocked responses.
        *   Review code quality, component reusability, adherence to design principles, and initial test coverage.
        *   Provide feedback on user experience, responsiveness, and accessibility.
    5.  **Refinement & Backend Integration Preparation:**
        *   Address planning commission feedback.
        *   Refine UI/UX based on feedback.
        *   Prepare the frontend for actual API integration: define data structures for messages (e.g., `sender`, `content`, `timestamp`, `type`), create a dedicated API client or service to handle HTTP requests to the backend.
    6.  **Comprehensive Frontend Testing with Playwright (UI/UX Blast Radius):**
        *   **Blast Radius Analysis (UI/UX):** Identify critical user flows (e.g., sending messages, scrolling chat history, handling long messages, displaying different message types). Analyze potential visual regressions or interaction breakdowns that could occur with future changes.
        *   Develop Playwright E2E tests to simulate user interaction with the UI. These tests will initially use mocked backend responses to isolate frontend behavior. Focus on verifying correct rendering, responsiveness across different viewports, and smooth user interaction.
*   **Deliverables:** Functional React SPA with core chat UI, comprehensive unit/integration tests, Playwright E2E tests (mocked backend).
*   **Dependencies:** None (initial phase).
*   **Success Criteria:** UI renders correctly, messages can be input and displayed, initial Playwright tests pass, and planning commission approves the core UI/UX.

---

**Module 2: Backend API Development (Port 8000)**

*   **Objective:** Create the core API for chat, LLM orchestration, and database interaction.
*   **Technology:** Python with FastAPI.
*   **Detailed Steps:**
    1.  **Project Scaffolding & Initial Endpoints:**
        *   Scaffold a new FastAPI project.
        *   Define a basic `GET /` endpoint for health checks.
        *   Implement the `POST /chat` endpoint to receive user messages.
        *   Integrate a simple LLM placeholder (e.g., a function that returns a hardcoded or rule-based response).
    2.  **Database Integration (Initial):
        *   Set up SQLite database connection using SQLAlchemy.
        *   Define SQLAlchemy models for `ChatMessage` (e.g., `id`, `sender`, `content`, `timestamp`).
        *   Implement basic CRUD operations (Create, Read) for chat messages.
    3.  **Backend Unit & Integration Testing (Initial):**
        *   Write unit tests for API routes (e.g., `POST /chat` handles requests correctly).
        *   Write unit tests for the LLM placeholder and database operations (e.g., `create_chat_message` stores data).
        *   Write integration tests to ensure the API can receive requests, interact with the database, and return responses.
    4.  **Planning Commission Review (Backend Core API & Data Model):**
        *   Present the functional core API (without MCP integration).
        *   Review API design, endpoint structure, request/response schemas, and initial security considerations (referencing `docs/09_SECURITY_MODEL.md`).
        *   Review the proposed database schema for `ChatMessage` and other core entities, ensuring alignment with `docs/06_DATABASE_SCHEMA.md` and `parliament_policies/01_DATA_PRIVACY_POLICY.md` (data governance and privacy).
        *   Provide feedback on performance considerations, scalability, and adherence to `parliament_policies/03_DEVELOPMENT_WORKFLOW.md`.
    5.  **Refinement & LLM Integration:**
        *   Address planning commission feedback.
        *   Integrate a more sophisticated LLM (e.g., a wrapper around a local LLM, or a mock service that simulates LLM behavior more realistically).
        *   Implement logic within the `POST /chat` endpoint to send user messages to the LLM, receive its response, and store both user and AI messages in the database.
    6.  **Comprehensive Backend Testing (API/Data Blast Radius):**
        *   **Blast Radius Analysis (API/Data):** Identify critical API endpoints and data flows. Analyze potential impact of changes on data integrity, existing integrations (even if mocked), and system stability. Consider how new LLM integrations might affect response times and error handling.
        *   Develop comprehensive unit and integration tests, including edge cases, error handling, and input validation.
        *   Implement basic load testing for key endpoints to ensure performance under expected traffic.
*   **Deliverables:** Functional FastAPI backend with chat API, LLM integration, database persistence, comprehensive unit/integration tests.
*   **Dependencies:** Module 4 (Database Setup).
*   **Success Criteria:** API endpoints respond correctly, chat messages are stored and retrieved from the database, LLM provides responses, and planning commission approves the core API and data model.

---

**Module 3: MCP Service Development**

*   **Objective:** Implement the Model Context Protocol (MCP) client and server to facilitate secure and structured communication with other Ministry AIs.
*   **Technology:** Python (or a suitable language for MCP implementation, ensuring compatibility with the Backend API).
*   **Detailed Steps:**
    1.  **MCP Protocol Research & Design:**
        *   Thoroughly review the `https://github.com/modelcontextprotocol` specification.
        *   Design the MCP client (for sending requests to other AIs) and MCP server (for receiving requests if the Cabinet Secretary Portal needs to expose its own AI capabilities) components based on the protocol.
        *   Define internal data structures for MCP messages.
    2.  **MCP Client & Server Scaffolding:**
        *   Set up a new Python project for the MCP service.
        *   Implement basic MCP message serialization/deserialization (e.g., using JSON or Protobuf as per MCP spec).
        *   Create placeholder functions for sending and receiving MCP messages, including basic routing logic.
    3.  **MCP Unit & Integration Testing (Initial):**
        *   Write unit tests for message formatting, parsing, and routing logic.
        *   Write integration tests to simulate basic MCP communication between mock clients and servers, verifying message exchange.
    4.  **Planning Commission Review (MCP Design & Security):**
        *   Present the MCP service design, including message formats, communication flows, and proposed security mechanisms (e.g., authentication, encryption).
        *   Review security implications and adherence to `docs/09_SECURITY_MODEL.md` and `parliament_policies/01_DATA_PRIVACY_POLICY.md` (data privacy in inter-AI communication).
        *   Provide feedback on extensibility, future integration with diverse Ministry AIs, and potential attack vectors.
    5.  **Refinement & Backend Integration:**
        *   Address planning commission feedback.
        *   Integrate the MCP client into the Backend API (Module 2) to allow the LLM to delegate specific queries or tasks to other Ministry AIs via MCP.
        *   Implement the MCP server to receive requests if the Cabinet Secretary Portal needs to expose its own AI capabilities or data.
    6.  **Comprehensive MCP Testing (Inter-AI Communication Blast Radius):**
        *   **Blast Radius Analysis (Inter-AI Communication):** Critically analyze the impact of MCP changes on inter-AI communication, data exchange, and potential cascading failures across Ministry AI systems. Consider latency, message loss, and error propagation.
        *   Develop robust integration tests with mock Ministry AIs to ensure correct message exchange, response handling, and error recovery.
        *   Implement stress testing for MCP communication to identify bottlenecks and ensure reliability under load.
*   **Deliverables:** Functional MCP service (client and server), comprehensive unit/integration tests.
*   **Dependencies:** Module 2 (Backend API for integration).
*   **Success Criteria:** MCP messages can be sent and received, basic communication with mock AIs is established, and planning commission approves the MCP design and security.

---

**Module 4: Database Setup and Integration**

*   **Objective:** Establish a local SQLite database for development and define its schema, with future Supabase migration in mind.
*   **Technology:** SQLite (for development), SQLAlchemy ORM.
*   **Detailed Steps:**
    1.  **Schema Design:**
        *   Define the detailed database schema for all necessary entities: `ChatMessage`, `User` (for authentication/authorization), `AI_Interaction_Log`, etc.
        *   Ensure schema design considers `docs/06_DATABASE_SCHEMA.md` (database schema guidelines) and `parliament_policies/01_DATA_PRIVACY_POLICY.md` (data privacy and governance).
        *   Incorporate data and policy versioning principles as per `.gemini/GEMINI.md`.
    2.  **Database Initialization & Migration:**
        *   Implement a script to initialize the SQLite database and create tables based on the defined schema.
        *   Set up a simple migration system (e.g., Alembic) to manage schema changes, even for SQLite, to prepare for future Supabase migration.
    3.  **ORM Integration:**
        *   Integrate SQLAlchemy into the Backend API (Module 2) for seamless and efficient database interaction.
    4.  **Planning Commission Review (Database Schema & Strategy):**
        *   Present the proposed detailed database schema, including relationships and data types.
        *   Review data integrity, normalization, indexing strategies, and alignment with `docs/06_DATABASE_SCHEMA.md`.
        *   Discuss the preliminary strategy for migrating to Supabase in the future, referencing `src/database/00_DATA_MIGRATION_PLAN.md`.
        *   Provide feedback on data versioning implementation and long-term data management.
    5.  **Refinement & Data Migration Strategy Documentation:**
        *   Address planning commission feedback.
        *   Refine the schema and ORM integration.
        *   Document a more detailed strategy for migrating to Supabase, including potential challenges and solutions.
    6.  **Comprehensive Database Testing (Data Integrity Blast Radius):**
        *   **Blast Radius Analysis (Data Integrity):** Critically analyze the impact of schema changes on existing data (even if mock data) and applications. Consider potential data loss, corruption, or performance degradation.
        *   Develop robust tests for data integrity, concurrency (if applicable), and performance of database operations (CRUD).
        *   Ensure tests cover data versioning aspects.
*   **Deliverables:** Initialized SQLite database, detailed schema, ORM integration, migration scripts, comprehensive database tests.
*   **Dependencies:** Module 2 (Backend API).
*   **Success Criteria:** Database tables are created, data can be stored and retrieved reliably, and planning commission approves the schema and migration strategy.

---

**Module 5: AI Interaction API & Logic**

*   **Objective:** Enable external AI agents to securely interact with and control the Cabinet Secretary Portal, allowing them to query status, add content, or trigger actions.
*   **Technology:** Python with FastAPI (part of Module 2's backend).
*   **Detailed Steps:**
    1.  **API Endpoint Definition:**
        *   Define specific, well-documented API endpoints for AI agents (e.g., `POST /ai/query_portal_status`, `POST /ai/add_content`, `POST /ai/trigger_action`).
        *   Determine precise request/response formats for these endpoints, including necessary parameters and expected outcomes.
    2.  **Authentication & Authorization:**
        *   Implement robust authentication and authorization mechanisms for AI agents (e.g., API keys, token-based authentication), referencing `docs/09_SECURITY_MODEL.md` (security model) and `constitution/03_AMENDMENT_AI_INTENT_AUTHORITY.md` (AI intent authority).
        *   Implement granular access control based on AI agent roles and permissions.
    3.  **Logic Implementation:**
        *   Implement the backend logic to process AI queries and execute modifications within the portal. This might involve updating internal states, interacting with other modules (e.g., adding a message to chat history, updating a user profile), or triggering external actions.
    4.  **AI Interaction Unit & Integration Testing (Initial):**
        *   Write unit tests for the AI interaction logic, covering various scenarios and edge cases.
        *   Write integration tests with mock AI agents to verify authentication, authorization, and basic functionality of each endpoint.
    5.  **Planning Commission Review (AI Interaction API & Control Scope):**
        *   Present the AI interaction API design, including endpoint definitions, security mechanisms, and the *scope of control* granted to AI agents.
        *   Critically review the potential impact on system stability, data integrity, and security.
        *   Ensure strict adherence to `constitution/03_AMENDMENT_AI_INTENT_AUTHORITY.md` regarding the authority and limitations of AI actions.
        *   Provide feedback on potential misuse, necessary safeguards, and audit logging requirements.
    6.  **Refinement & Comprehensive Testing:**
        *   Address planning commission feedback, especially concerning security and control.
        *   Develop comprehensive tests for various AI interaction scenarios, including invalid inputs, unauthorized access attempts, and complex sequences of actions.
        *   Conduct security penetration testing for AI interaction endpoints.
    7.  **Comprehensive AI Interaction Testing (System Control Blast Radius):**
        *   **Blast Radius Analysis (System Control):** This is a *critical* phase. Critically assess the potential impact of AI-driven actions on the entire system, including unintended consequences, cascading failures, and data corruption. This analysis will involve the planning commission to ensure all high-risk scenarios are identified.
        *   Develop Playwright E2E tests that simulate an AI agent interacting with the portal via its API and observing the resulting changes in the UI and backend state. These tests will verify that AI actions have the intended effects and no unintended side effects.
*   **Deliverables:** Secure API endpoints for AI interaction, implemented logic, comprehensive unit/integration tests.
*   **Dependencies:** Module 2 (Backend API), Module 4 (Database).
*   **Success Criteria:** AI agents can securely interact with the portal, their actions are correctly processed and logged, and planning commission approves the AI interaction API and control scope.

---

**Overall Testing & Verification (Continuous Process):**

*   **Continuous Integration/Continuous Deployment (CI/CD):** Implement CI/CD pipelines (referencing `.github/workflows/`) to automate testing and deployment processes. Each code commit will trigger automated tests.
*   **Playwright E2E Testing (Full System Integration):**
    *   Once all modules are integrated and their individual tests pass, a comprehensive Playwright test suite will be executed.
    *   These tests will simulate real user interactions (via the Frontend) and AI interactions (via the AI Interaction API), verifying the complete end-to-end functionality of the system.
    *   **Blast Radius Analysis (System-Wide Integration):** Before the final E2E tests, a thorough system-wide blast radius analysis will be conducted, involving the planning commission, to identify all potential areas of impact from the integrated system. This will inform the scope of E2E tests and ensure critical paths are covered, especially those involving data modification or inter-AI communication.
*   **Code Quality Checks:** Before any presentation or deployment, all code will pass project-specific build, linting, and type-checking commands (e.g., `npm run lint`, `tsc`, `ruff check .`).
*   **Security Audits:** Regular security audits will be conducted, especially for the AI interaction and MCP modules.

**Next Steps:**

Upon your approval of this detailed plan, I will begin by scaffolding the Frontend (Module 1) and Backend (Module 2) projects, and then proceed with the initial design and implementation steps as outlined, ensuring to engage the "planning commission" (my internal review process based on project directives) at each specified juncture.

**Progress Update (August 1, 2025):**

*   **Module 1: Frontend Development - Cabinet Secretary Portal (Port 3000)**
    *   **Status:** Initial scaffolding, core chat UI implementation, and unit/integration tests are complete and passing. The frontend development server is running and accessible for review.
    *   **Integration with Backend:** Frontend `App.tsx` has been modified to communicate with the backend API. CORS proxy has been configured in `package.json`.
    *   **Next:** Comprehensive Playwright E2E testing.

*   **Module 2: Backend API Development (Port 8000)**
    *   **Status:** Project scaffolding, initial health check and chat endpoints, and SQLite database integration with SQLAlchemy are complete. Unit and integration tests for the backend API and database interactions are passing. The backend server is running.
    *   **Integration with Frontend:** CORS middleware has been added to `main.py` to allow requests from the frontend origin. The backend is now successfully receiving and processing messages from the frontend, and persisting them to the database.
    *   **Next:** **LLM Integration:** Integrate a more sophisticated LLM into the chat endpoint.

*   **Module 3: MCP Service Development (Port 8001)**
    *   **Status:** Initial scaffolding of the MCP service with basic health check, `/mcp_send`, and `/mcp_receive` endpoints is complete. Unit and integration tests for these endpoints are passing. The MCP service is running and accessible.
    *   **Integration with Backend:** The MCP client has been integrated into the Backend API, allowing the `/chat` endpoint to send messages to the MCP service based on a prefix.
    *   **Next:** Comprehensive MCP testing and further refinement of MCP-specific logic.

*   **Module 4: Database Setup and Integration**
    *   **Status:** Initial SQLite database setup and SQLAlchemy integration are complete. Unit and integration tests for database operations are passing.
    *   **Next:** Document the preliminary strategy for migrating to Supabase and confirm comprehensive database testing.
