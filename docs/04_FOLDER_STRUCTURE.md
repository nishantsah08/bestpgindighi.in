# 04 - Folder Structure

This document outlines the logical structure of the project repository.

```
bestpgindighi-ai/
│
├── .github/                  # CI/CD workflows and automation.
│
├── 📜 constitution/          # The "Why": Core mission, values, and goals.
│   └── mission_statement.md
│
├── 🏛️ parliament/             # The "What": Enforceable business policies.
│   ├── policies/             # Tier 1 Foundational Policies (as YAML code).
│   │   ├── billing_policy.yaml
│   │   └── maintenance_policy.yaml
│   └── tests/                # The bludeprint validation tool's test suite.
│
├── 🚀 executive/             # The "How": AI agents that run the business.
│   ├── cabinet_secretary_ai/   # The central coordinating AI.
│   └── departments/          # Self-contained, deployable business units.
│       └── billing/
│           ├── secretary_ai/     # Source code for the department's AI.
│           ├── secretariat/      # Resources (apps, cloud config, etc).
│           ├── Dockerfile        # Isolated development environment.
│           └── DEPLOYMENT.md     # Department-specific deployment guide.
│
├── ⚖️ judiciary/             # Independent error and dispute resolution AI.
│   └── src/
│
├── 👀 independent_bodies/    # Independent oversight AIs.
│   ├── auditor_ai/
│   └── vigilance_ai/
│
├── 🧠 advisory/              # Strategic planning and analysis AI.
│   └── strategy_and_planning_ai/
│
├── 🌐 mcp/                   # Shared Model Context Protocol servers.
│   └── src/
│
├── 📚 docs/                   # System documentation (this folder).
│
└── README.md                 # High-level project overview.
```