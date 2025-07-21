# 01 - System Architecture

This document outlines the high-level architecture of the autonomous management system. The system is owned by **"SVH Enterprise"** and this specific implementation is for the **"Best PG in Dighi"** brand.

## Core Communication: Model Context Protocol (MCP)

All components within the system communicate via the Model Context Protocol (MCP). The MCP acts as a central, intelligent communication bus, ensuring that all interactions are standardized, contextual, and auditable.

## Architecture Diagram

```mermaid
graph TD
    subgraph "Strategic & Legislative"
        CEO(👤 CEO/Owner)
        PARLIAMENT(🏛️ Parliament <br> Defines Policies)
    end

    subgraph "Advisory & Oversight (Independent)"
        STRAT(🧠 Strategy & Planning AI)
        AUDIT(🔍 Auditor AI)
        VIGIL(🛡️ Vigilance AI)
        JUD(⚖️ Judiciary AI)
    end

    subgraph "Executive Branch"
        CAB_SEC(🤖 Cabinet Secretary AI)
        FIN_MIN(💰 Ministry of Finance)
        DEPT_A(🏢 Dept A: Billing)
        DEPT_B(🏢 Dept B: Maintenance)
        DEPT_C(🏢 Dept C: Onboarding)
    end

    subgraph "External Interfaces & Applications"
        PublicWebsite[🌐 Public Website]
        SystemPortal[🔒 Internal System Portal]
        MobileSuite[📱 Native Mobile Suite <br> CEO, Sales, Caretaker Apps]
    end

    %% Core Communication Bus
    MCP((🌐 Model Context Protocol <br> Central Bus))

    %% Flows
    CEO -- "Strategic Direction" --> CAB_SEC
    CEO -- "Manages via" --> SystemPortal
    CEO -- "Manages via" --> MobileSuite

    PARLIAMENT -- "Publishes Policies" --> MCP

    PublicWebsite -- "Generates Leads" --> DEPT_C

    SystemPortal -- "Interacts with" --> MCP
    MobileSuite -- "Interacts with" --> MCP

    CAB_SEC -- "Reads Policies" --> MCP
    CAB_SEC -- "Issues Commands" --> DEPT_A
    CAB_SEC -- "Issues Commands" --> DEPT_B
    CAB_SEC -- "Issues Commands" --> DEPT_C
    CAB_SEC -- "Issues Commands" --> FIN_MIN

    FIN_MIN -- "Executes Financial Tasks" --> MCP
    DEPT_A -- "Executes Tasks" --> MCP
    DEPT_B -- "Executes Tasks" --> MCP
    DEPT_C -- "Executes Tasks" --> MCP

    FIN_MIN -- "Refers Edge Cases" --> JUD
    DEPT_A -- "Refers Edge Cases" --> JUD
    DEPT_B -- "Refers Edge Cases" --> JUD
    DEPT_C -- "Refers Edge Cases" --> JUD

    STRAT -- "Analyzes System Data" ..-> MCP
    AUDIT -- "Audits Departments" ..-> DEPT_A
    AUDIT -- "Audits Departments" ..-> DEPT_B
    AUDIT -- "Audits Departments" ..-> DEPT_C
    AUDIT -- "Audits Ministry" ..-> FIN_MIN
    VIGIL -- "Monitors Entire System" ..-> MCP
```

### Core Data Models

The system is built around a set of core data models that represent key business entities.

1.  **Tenants:** Represents all prospective, current, and past tenants. This model holds all customer-related information, including contact details, billing history, and communication logs.
2.  **Vendors:** Represents all third-party service providers (e.g., electricians, plumbers, suppliers). This model stores vendor contact information, service history, and financial records like invoices and quotes.
3.  **General Ledger:** The central, immutable record of all financial transactions (revenue and expenses) within the system.

### Key Interaction Flows

1.  **Financial Management:** The **Ministry of Finance**, via its **Financial AI Agent**, handles all expense and revenue recording. It receives data from the outside world via the official **WhatsApp Business API** and then processes it internally using the Model Context Protocol (MCP).
2.  **Lead Generation:** The **Public Website** serves as the primary channel for attracting new leads. Information from prospective tenants is captured and fed directly to the Onboarding Department (Dept C).
3.  **Command & Control:** The CEO provides strategic direction and manages the system via the **Internal System Portal** and the **Native Mobile Suite**. These interfaces act as the primary human-computer interaction points for system management. The detailed blueprint for the portal is defined in `04_INTERNAL_SYSTEM_PORTAL_BLUEPRINT.md`.
4.  **Policy & Execution:** The Parliament publishes policies to the MCP. The Departments read these policies and execute their tasks accordingly.
5.  **Oversight & Reporting:** The independent Auditor and Vigilance AIs monitor the system and report directly to the CEO, ensuring unbiased oversight. The Auditor AI has a specific mandate to audit the new Ministry of Finance.
6.  **Exception Handling:** When a Department encounters an error it cannot solve, it refers the issue to the independent Judiciary AI for a binding resolution.
7.  **Vendor Management:** The CEO manages all vendor relationships, including adding new vendors and logging interactions, primarily through the **CEO Mobile App** and the **Internal System Portal**.
