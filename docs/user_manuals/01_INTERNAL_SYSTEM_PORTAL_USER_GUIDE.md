# Internal System Portal - User Guide

**For:** CEO, Power Users

### Philosophy: Total Information, Total Control

This web-based portal is the central nervous system of the entire operation, structured like a government to provide both high-level oversight and deep, departmental control. It is designed for use on a desktop computer.

---

### Main Navigation & Structure

The portal is organized around a main navigation bar on the left, providing access to each major governmental function:

*   `📈 Dashboard`
*   `🗣️ Cabinet Secretary`
*   `💰 Ministry of Finance`
*   `🏡 Property & Tenant Welfare`
*   `📈 Growth & Commerce`
*   `⚙️ Ministry of Technology`

---

### 1. The Dashboard

This is your primary, cross-ministry "Situation Room." It is a tabbed interface designed to show what needs attention and how the business is performing.

*   **Date Range Filter:** All data on the dashboard can be filtered by a master date range (e.g., "This Month").
*   **Action Items Tab:** The default view, focusing on immediate tasks. It contains:
    *   A **Pending Issues** widget with a total count and breakdown by category (Judiciary, Maintenance).
    *   A **Rent Status** widget showing collected vs. pending rent for the period.
    *   An **Issues Docket** listing all actionable items requiring your review.
*   **Performance Trends Tab:** This view shows key performance indicators (KPIs) with visual trend line charts:
    *   Widgets for Revenue, Occupancy Rate, Lead Conversion, etc., all showing trends over the selected period.

---

### 2. The Cabinet Secretary

Your direct line to the system's AI analyst. Use this chat-like interface to ask complex, natural language questions about your business data (e.g., "Compare electricity costs for Q1 vs Q2").

---

### 3. Ministry Pages (Departmental Headquarters)

Each ministry page is a dedicated dashboard for that specific business function, often with its own tabs for different departments.

*   **Ministry of Finance:** Manage all financial operations.
    *   **Sub-Pages:** Financial Statements (P&L, Balance Sheet, Cash Flow), General Ledger (with Transaction Correction feature), and Asset Inventory.
    *   **Automated Inventory:** When a capital asset (e.g., a fan, a mattress) is purchased via the AI-powered expense workflow, it is automatically added to the Asset Inventory upon your confirmation. This portal view allows you to see the real-time status of all assets.
*   **Property & Tenant Welfare:** The hub for the Tenant CRM and the Property/Bed inventory management system.
*   **Growth & Commerce:** Contains the detailed Sales Pipeline, lead management tools, and marketing reports.

---

### 4. Ministry of Technology

The engine room for configuring the system itself.

*   **The Parliament (Tab):** A powerful GUI for editing live business policies. The system reads the project's `.yaml` policy files and generates user-friendly forms to let you change the rules of the business without touching code.
*   **System Configuration (Tab):** The secure area for managing system-wide technical settings, most importantly the **API Keys and Integration Secrets** for third-party services like WhatsApp or payment gateways.

---

### 5. Personal Settings (User Profile Menu)

Settings that are specific to your user account are located in the User Profile Menu, accessed by clicking your name in the **top-right corner** of the portal.

*   **Edit Profile:** Change your display name and contact information.
*   **Change Password:** Manage your login credentials.
*   **Theme:** Select a light or dark theme for the portal interface.
*   **Logout:** Sign out of the application.

---

### 6. Initial System Setup & Data Population

When the system is first deployed, it will be empty. Follow this two-step process to populate it with your core business data.

#### Step 1: Manual Setup of Core Data

First, you must manually set up the foundational data using the portal:

1.  **Define Properties:** Navigate to `🏡 Property & Tenant Welfare -> Asset Management`. Add your properties, and then the rooms and beds within them, setting the rent price for each bed.
2.  **Create Staff Accounts:** Create user accounts for your staff members and assign their roles.

#### Step 2: AI-Powered Import of Existing Tenants

To import your existing tenant data, you will use a conversational AI workflow powered by the Cabinet Secretary.

1.  **Upload Raw Data:** Navigate to `🏡 Property & Tenant Welfare -> Data Import`. Upload your existing tenant spreadsheet or file in whatever format you have it (Excel, CSV, text).
2.  **Conversational Mapping:** The Cabinet Secretary AI will start a chat session. It will analyze your file and guide you through mapping your columns (e.g., "Name," "Room No.") to the system's required fields.
3.  **AI-Assisted Cleaning:** The AI will automatically handle tasks like splitting a "101A" room value into Room: "101" and Bed: "A", asking you for confirmation.
4.  **Guided Import:** Once you confirm the mapping, the AI will process the file, validate each row against the properties you set up in Step 1, and import all valid tenants. It will provide a summary of the import and a list of any rows that failed for your review.
