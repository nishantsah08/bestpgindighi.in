# 04 - Folder Structure

This document outlines the logical structure of the project repository.

```
bestpgindighi-ai/
│
├── .github/                  # CI/CD workflows and automation.
│
├── 📜 constitution/          # The "Why": Core mission, values, and goals.
│   └── 00_CONSTITUTION.md
│
├── 🏛️ parliament_policies/    # The "What": Enforceable business policies.
│   ├── bills/                # Draft policies (proposals).
│   ├── acts/                 # Ratified, live policies.
│   └── 03_DEVELOPMENT_WORKFLOW.md # The legislative process document.
│
├── 🚀 executive/             # The "How": AI agents that run the business.
│   ├── ministry_of_finance/      # The "Finance" Ministry.
│   │   └── README.md
│   ├── growth_and_commerce/      # The "Hunter" Ministry (Sales-led).
│   │   └── README.md
│   ├── property_and_tenant_welfare/ # The "Farmer" Ministry (Caretaker-led).
│   │   └── README.md
│   ├── 02_AI_AGENT_ROLES.md    # Describes the roles of the AI "civil service".
│   └── README.md             # Explains the two-ministry structure.
│
├── ⚖️ judiciary/             # Independent error and dispute resolution AI.
│
├── 👀 independent_bodies/    # Independent oversight AIs (Auditor, Vigilance).
│
├── 🧠 advisory/              # Strategic planning and analysis AI.
│
├── 🌐 mcp/                   # Shared Model Context Protocol servers.
│
├── 📚 docs/                   # System documentation (this folder).
│   ├── 00_SYSTEM_OVERVIEW.md
│   ├── 01_SYSTEM_ARCHITECTURE.md
│   ├── 04_FOLDER_STRUCTURE.md (this file)
│   └── 05_BUSINESS_OPERATIONS_MODEL.md
│
├── 🌐 website/               # Source code for the public-facing website.
│
├── 📱 mobile_apps/            # Source code for the native Android application suite.
│   ├── ceo_app/
│   ├── sales_app/
│   └── caretaker_app/
│
└── README.md                 # High-level project overview.
```