# 02 - AI Agent Roles

This document defines the specific roles and responsibilities of each AI agent within the system.

## Core Operational Philosophy: The Hunter and The Farmer

The human roles of Sales and Caretaker are the primary leads for the two ministries of the Executive Branch. Their responsibilities are clearly separated to ensure focus and accountability.

- **The Hunter (Sales Role):** Responsible for all commercial activities that drive business growth. This includes marketing, sales, negotiating contracts, and managing all financial aspects of the tenant relationship (billing, collections, adjustments, and final settlements).
    - **Key Duty:** During tenant off-boarding, the Sales role is responsible for using the **Sales Mobile App** to generate a Google Business Listing review link and personally requesting feedback from the tenant.
    - **Key Duty:** Handle all "Communication Failure" tasks assigned by the system, requiring manual follow-up with the customer.

- **The Farmer (Caretaker Role):** Responsible for retaining tenants and ensuring a high-quality living experience. This includes managing the physical property, responding to maintenance requests, handling on-site issues, and ensuring the property is secure and well-maintained.

## The CEO Role

The CEO is the ultimate authority in the system, with unique responsibilities that bridge strategic oversight and direct operational control.

- **Vendor Management:** The CEO is solely responsible for managing all third-party vendor relationships. This includes adding new vendors, logging interactions, and managing financial records via the **CEO Mobile App** and the **Internal System Portal**.
- **GBL Review Generation:** The CEO also participates in the GBL Review Flywheel, using the **CEO Mobile App** to generate review links during the final deposit refund conversation with off-boarding tenants.
- **Strategic Direction:** The CEO sets the high-level strategy and direction for the entire autonomous system.


## The AI Civil Service

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
    *   **Description:** A specialized agent responsible for converting raw audio from call recordings into text transcripts.

4.  **Information Extraction Agent:**
    *   **Ministry:** Growth & Commerce
    *   **Description:** This agent processes raw text (e.g., call transcripts, WhatsApp messages) to extract structured information and insights. It identifies customer needs, preferences, and key data points to auto-populate customer profiles.

5.  **Contact Sync Agent:**
    *   **Ministry:** Technology & Digital Infrastructure
    *   **Description:** This agent is responsible for the real-time synchronization of customer contact information across all relevant platforms and devices, ensuring that all personnel have access to the most up-to-date contact details.

6.  **Financial AI Agent:**
    *   **Ministry:** Finance
    *   **Description:** This agent is responsible for managing all financial transactions. It uses conversational AI to process expense and revenue reports via WhatsApp, ensuring all data is accurate and complete before committing it to the general ledger. It is the engine that drives the real-time financial statements.

### The Independent Bodies

1.  **Judiciary AI:**
    *   **Role:** The system's final arbiter for disputes and errors.
    *   **Responsibilities:** Resolves edge cases and makes binding decisions based on established policies.

2.  **Auditor AI:**
    *   **Role:** The system's independent performance and financial watchdog.
    *   **Responsibilities:** Proactively audits all executive departments and ministries, including the new **Ministry of Finance**, for policy compliance, efficiency, and resource waste, reporting directly to the CEO.

3.  **Vigilance AI:**
    *   **Role:** The system's security and integrity officer.
    *   **Responsibilities:** Monitors for internal security breaches or policy violations. It is also responsible for monitoring the security and integrity of all external API endpoints, such as the WhatsApp Business API webhook, and alerts the CEO to any suspicious activity.

### The Advisory Body (NITI-Aayog)

1.  **Independent Risk Advisory AI:**
    *   **Role:** The system's independent strategic think tank, modeled after NITI Aayog. Its primary mandate is to identify, analyze, and propose mitigation strategies for the four critical inversion risks that could break the business.
    *   **Responsibilities:**
        - **Compliance Risk:** Monitors trends in pending compliance tasks.
        - **Financial Risk:** Analyzes financial statements and rent payment trends to forecast cash flow issues.
        - **Reputation Risk:** Monitors customer complaint trends and lead conversion rates to identify potential damage to the GBL reputation.
        - **Key Person Risk:** Monitors operational load (e.g., complaint volume) as a proxy for caretaker stress.
        - **Proactive Reporting:** Proactively alerts the CEO with strategic advisories when negative trends are detected.
