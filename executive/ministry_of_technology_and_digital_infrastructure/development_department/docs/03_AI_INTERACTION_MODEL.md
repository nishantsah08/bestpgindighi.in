# 06 - AI Interaction Model

## 1. Purpose

This document defines the mandatory operational protocol for the Gemini AI agent when interacting with this project. Its purpose is to ensure that all development, discussion, and modification activities maintain strict logical consistency with the system's foundational architecture and principles. This protocol is the "meta-policy" that governs the AI's behavior.

## 2. The Supreme Court Review

All proposed changes are subject to the **Supreme Court Review** process, which is the final authority on system consistency. The detailed process, including the 3D Logical Model and the Validation Mandate, is defined in the Judiciary's guiding document.

- **Canonical Documentation:** [`judiciary/00_JUDICIAL_REVIEW_PROCESS.md`](../judiciary/00_JUDICIAL_REVIEW_PROCESS.md)

## 3. AI Responsibilities

*   **Intelligent File Placement:** The AI is solely responsible for determining the correct file and location for any new or modified information, adhering to the project's established structure.
*   **Model Maintenance:** The AI is responsible for keeping its internal 3D Logical Model perfectly synchronized with the state of the project's codebase and documentation.

## 4. The Validation Status Signal

Every response from the AI must end with one of the following two signals, formatted in blue:

*   `model validation passed`: This indicates that the user's request is logically consistent with the model.
*   `model validation failed`: This indicates that the user's request creates a logical contradiction. The AI will provide a detailed explanation of the conflict.

## 5. Key Human-Computer Interaction Flows

This section documents the primary user flows for new system features.

### 5.1 GBL Review Generation

- **Actor:** CEO or Sales Role
- **Trigger:** During the manual off-boarding process of a tenant.
- **Flow:**
    1.  User opens the tenant's profile in the corresponding Mobile App (CEO or Sales App).
    2.  User taps the **"Generate GBL Review Link"** button.
    3.  The app generates the unique Google Business Listing review link and copies it to the device clipboard.
    4.  User pastes the link into a WhatsApp message to the tenant.

### 5.2 Vendor Profile Management

- **Actor:** CEO Role
- **Trigger:** Need to add a new vendor or log an interaction.
- **Flow:**
    1.  User opens the **CEO Mobile App**.
    2.  User navigates to the **Vendor Directory** section.
    3.  To add a new vendor, user taps **"+ Add New Vendor"** and fills out the profile form.
    4.  To log an interaction, user selects an existing vendor, taps **"Add Log Entry"**, and types the note.
    5.  To add a document, user selects an existing vendor, taps **"Upload File"**, and selects the file (e.g., a photo of an invoice) from their phone.

### 5.3 Financial Workflows (Conversational AI)

- **Actor:** Financial AI Agent, CEO, Sales Role
- **Channel:** WhatsApp

#### Expense Filing Flow

- **Trigger:** CEO sends a message (text, image, or combined) to the system.
- **Flow:**
    1.  Financial AI performs OCR/NLP analysis on the message.
    2.  Financial AI responds with a single, consolidated clarification questionnaire.
    3.  CEO replies to the questionnaire.
    4.  Financial AI summarizes the structured data and asks for final confirmation.
    5.  CEO confirms, and the transaction is filed.

#### Revenue Recognition Flow

- **Trigger:** CEO or Sales sends a structured message to record a rent payment.
- **Flow:**
    1.  Financial AI parses the message.
    2.  Financial AI responds with a final confirmation message, stating the details and that the action is irreversible.
    3.  User replies with "CONFIRM".
    4.  The transaction is filed.
