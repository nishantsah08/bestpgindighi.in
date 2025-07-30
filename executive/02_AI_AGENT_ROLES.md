# 02 - AI Agent Roles

This document defines the specific roles and responsibilities of each AI agent within the system.

## Core Operational Philosophy: The Hunter and The Farmer

The human roles of Sales and Caretaker are the primary leads for the two ministries of the Executive Branch. Their responsibilities are clearly separated to ensure focus and accountability.

- **The Hunter (Sales Role):** Responsible for all commercial activities that drive business growth. This includes marketing, sales, negotiating contracts, and managing all financial aspects of the tenant relationship (billing, collections, adjustments, and final settlements).
    - **Key Duty:** Handle all "Communication Failure" tasks assigned by the system, requiring manual follow-up with the customer.

- **The Farmer (Caretaker Role):** Responsible for retaining tenants and ensuring a high-quality living experience. This includes managing the physical property, responding to maintenance requests, handling on-site issues, and ensuring the property is secure and well-maintained.

## The CEO Role

The CEO is the ultimate authority in the system, with unique responsibilities that bridge strategic oversight and direct operational control.

- **Vendor Management:** The CEO is solely responsible for managing all third-party vendor relationships. This includes adding new vendors, logging interactions, and managing financial records via the **CEO Mobile App** and the **Internal System Portal**.
- **GBL Review Generation:** The CEO is solely responsible for the GBL Review Flywheel, using the **CEO Mobile App** to generate review links during the final deposit refund conversation with off-boarding tenants.
- **Strategic Direction:** The CEO sets the high-level strategy and direction for the entire autonomous system.


## The AI Civil Service

These AI agents are the "civil service" of the Executive branch, responsible for carrying out the day-to-day operations of the business. They do not act on their own initiative, but rather consume capabilities exposed via the Model Context Protocol (MCP) as directed by their governing ministry and the policies set by Parliament.

### The Executive Branch

1.  **Cabinet Secretary AI:**
    *   **Reports to:** The human CEO.
    *   **Role:** The chief coordinator of the entire Executive branch.
    *   **Responsibilities:** Translates CEO strategy into operational commands, assigns policy execution to the appropriate departments, and monitors overall performance.

2.  **Departmental Secretary AI (e.g., Billing, Maintenance):**
    *   **Reports to:** The Cabinet Secretary AI.
    *   **Role:** The lead AI agent for a specific business domain within a Ministry.
    *   **Responsibilities:** Executes the tasks defined in its assigned business logic blueprints, manages its own resources, and reports status and metrics upwards.

3.  **Transcription Agent:**
    *   **Ministry:** Technology & Digital Infrastructure
    *   **Description:** A specialized agent responsible for converting raw audio from call recordings into text transcripts. It operates as part of a multi-provider, cost-optimized waterfall strategy as defined in the `10_customer_interaction_and_call_management_bill.yaml`.

4.  **Information Extraction Agent:**
    *   **Ministry:** Growth & Commerce
    *   **Description:** This agent processes call transcripts to extract structured information and insights. It only receives calls that have passed the role-based analysis rules, ensuring it processes only valid business communications. It identifies customer needs, preferences, and key data points to auto-populate customer profiles.

5.  **Verification AI:**
    *   **Ministry:** Technology & Digital Infrastructure
    *   **Description:** A specialized agent responsible for the autonomous verification of tenant documents. It analyzes submitted documents for clarity and completeness, and manages the automated communication loop with the tenant.

6.  **Contact Sync Agent:**
    *   **Ministry:** Technology & Digital Infrastructure
    *   **Description:** This agent's role is to handle the synchronization of the central `contacts` database with external systems, such as mobile device address books. This is a distinct future capability.

6.  **Financial AI Agent:**
    *   **Ministry:** Finance
    - Passively monitors the main WhatsApp channel to identify and process financial transactions, including revenue and expenses. It is the engine that drives the real-time financial statements.

### The Independent Bodies

1.  **Judiciary AI:**
    *   **Role:** The system's final arbiter for disputes and errors.
    *   **Responsibilities:** Resolves edge cases and makes binding decisions based on established policies.

2.  **Auditor AI:**
    *   **Role:** The system's independent performance and financial watchdog.
    *   **Responsibilities:** Proactively audits all executive departments and ministries, including the new **Ministry of Finance** and the **Verification AI**, for policy compliance, efficiency, and resource waste, reporting directly to the CEO.

3.  **Vigilance AI:**
    *   **Role:** The system's security and integrity officer.
    *   **Responsibilities:** Monitors for internal security breaches or policy violations. It is also responsible for monitoring the security and integrity of all external API endpoints and the operational integrity of autonomous agents like the **Verification AI**. It alerts the CEO to any suspicious activity.

### The Advisory Body (NITI-Aayog)

1.  **Independent Risk Advisory AI:**
    *   **Role:** The system's independent strategic think tank, modeled after NITI Aayog. Its primary mandate is to identify, analyze, and propose mitigation strategies for the four critical inversion risks that could break the business.
    *   **Responsibilities:**
        - **Compliance Risk:** Monitors trends in pending compliance tasks.
        - **Financial Risk:** Analyzes financial statements and rent payment trends to forecast cash flow issues.
        - **Reputation Risk:** Monitors customer complaint trends and lead conversion rates to identify potential damage to the GBL reputation.
        - **Key Person Risk:** Monitors operational load (e.g., complaint volume) as a proxy for caretaker stress.
        - **Proactive Reporting:** Proactively alerts the CEO with strategic advisories when negative trends are detected.
