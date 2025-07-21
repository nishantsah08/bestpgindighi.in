# 04 - Internal System Portal Blueprint

This document outlines the structural blueprint and feature set for the CEO's Internal System Portal.

**Authentication:** Secure login via the CEO's designated Google Account.

---

### 1. Main Dashboard (Landing Page)

- **Purpose:** To provide a single-glance overview of the entire business's health and status.
- **Components:**
    - **Key Performance Indicators (KPIs) Bar:** Occupancy, Revenue MTD, Expenses MTD, Net Profit MTD, Open Maintenance Tickets, New Leads (7 days).
    - **Recent Activity Feed:** A live-updating list of important system events.
    - **Action Required Queue:** A list of items that require the CEO's direct attention.

---

### 2. Main Navigation Menu (Sidebar)

- Dashboard
- Cabinet Secretary (Query Interface)
- Ministry of Finance
- Ministry of Growth & Commerce (Sales)
- Ministry of Property & Tenant Welfare (Caretaker)
- Ministry of Technology & Digital Infrastructure
- Vendor Directory
- Settings

---

### 3. Section Details

#### 3.1 Cabinet Secretary (Query Interface)
- **Purpose:** A powerful, LLM-driven interface for the CEO to ask complex questions that span across internal system data and the open internet.
- **Interface:** A single, prominent text input box for natural language queries.

#### 3.2 Ministry of Finance
- **Purpose:** The deep-dive section for all financial data and control.
- **Sub-Pages:** Financial Statements (P&L, Balance Sheet, Cash Flow), General Ledger (with Transaction Correction feature), and Inventory Management.

#### 3.3 Ministry of Growth & Commerce (Sales)
- **Purpose:** To monitor the performance of the sales and marketing functions.
- **Components:** Lead Funnel Visual, Tenant Onboarding Status, Revenue Analytics, and the **GBL Review Link Generator** tool.

#### 3.4 Ministry of Property & Tenant Welfare (Caretaker)
- **Purpose:** To monitor the operational health of the physical properties.
- **Components:** Maintenance Ticket Dashboard, Tenant Satisfaction Metrics, and Property Inspection Reports.

#### 3.5 Ministry of Technology & Digital Infrastructure
- **Purpose:** To provide a high-level overview of the health and status of the digital infrastructure.
- **Components:** System Status Dashboard, Deployment Logs, and a high-level Error Monitoring summary.

#### 3.6 Vendor Directory
- **Purpose:** The web-based interface for managing all vendor information.
- **Features:** A searchable list of vendors, with profile pages containing full financial transaction history, interaction logs, and uploaded files.

#### 3.7 Settings
- **Purpose:** A section for system-level configurations.
- **Components:** User Management, Notification Preferences, and configuration for financial categories.