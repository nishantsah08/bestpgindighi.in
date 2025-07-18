# 01 - System Architecture

This document outlines the high-level architecture of the autonomous PG management system.

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
        DEPT_A(🏢 Dept A: Billing)
        DEPT_B(🏢 Dept B: Maintenance)
        DEPT_C(🏢 Dept C: Onboarding)
    end

    %% Core Communication Bus
    MCP((🌐 Model Context Protocol <br> Central Bus))

    %% Flows
    CEO -- "Strategic Direction" --> CAB_SEC
    CEO -- "Receives Reports & Advice" --- STRAT
    CEO -- "Receives Audit Reports" --- AUDIT
    CEO -- "Receives Security Alerts" --- VIGIL

    PARLIAMENT -- "Publishes Policies" --> MCP

    CAB_SEC -- "Reads Policies" --> MCP
    CAB_SEC -- "Issues Commands" --> DEPT_A
    CAB_SEC -- "Issues Commands" --> DEPT_B
    CAB_SEC -- "Issues Commands" --> DEPT_C

    DEPT_A -- "Executes Tasks" --> MCP
    DEPT_B -- "Executes Tasks" --> MCP
    DEPT_C -- "Executes Tasks" --> MCP

    DEPT_A -- "Refers Edge Cases" --> JUD
    DEPT_B -- "Refers Edge Cases" --> JUD
    DEPT_C -- "Refers Edge Cases" --> JUD

    STRAT -- "Analyzes System Data" ..-> MCP
    AUDIT -- "Audits Departments" ..-> DEPT_A
    AUDIT -- "Audits Departments" ..-> DEPT_B
    AUDIT -- "Audits Departments" ..-> DEPT_C
    VIGIL -- "Monitors Entire System" ..-> MCP
```

### Key Interaction Flows

1.  **Command & Control:** The CEO provides strategic direction to the Cabinet Secretary AI, which in turn reads policies from the MCP and directs the various Executive Departments.
2.  **Policy & Execution:** The Parliament publishes policies to the MCP. The Departments read these policies and execute their tasks accordingly.
3.  **Oversight & Reporting:** The independent Auditor and Vigilance AIs monitor the system and report directly to the CEO, ensuring unbiased oversight.
4.  **Exception Handling:** When a Department encounters an error it cannot solve, it refers the issue to the independent Judiciary AI for a binding resolution.