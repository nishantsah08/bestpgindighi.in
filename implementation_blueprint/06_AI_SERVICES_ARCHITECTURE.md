# Chapter 6: AI Services Architecture

**Version:** 1.0
**Date:** 2025-07-23

## 6.1 The NLU/OCR Service

This is a single, unified microservice responsible for interpreting all inbound communications from the SOC.

### 6.1.1 Model Selection
- **OCR:** Google Cloud Vision API - Text Detection. Chosen for its high accuracy and ability to handle various image qualities and languages.
- **NLU:** A fine-tuned version of a pre-trained transformer model like `distilbert-base-uncased`. Chosen for its balance of performance and efficiency.

### 6.1.2 Diagram: Inbound Message Processing Flow

- **Visual Asset:** `![Inbound Message Processing Flow](./assets/visuals/06_message_flow.svg)`
- **Source Code (Mermaid):**
  ```mermaid
  graph TD
      A[WhatsApp Gateway Receives Message] --> B{Is message type text or media?};
      B -- Text --> C[Send to NLU Model];
      B -- Media --> D[Download Media];
      D --> E[Send to Cloud Vision API for OCR];
      E --> C;
      C --> F[Extract Intent & Entities];
      F --> G[Format Standardized Intent Object];
      G --> H[Return JSON to Gateway];
  ```

## 6.2 The Predictive Models Service

This service hosts the custom machine learning models for lead scoring and vacancy prediction.

### 6.2.1 Lead Scoring Model
- **Architecture:** A gradient boosting model (e.g., XGBoost) trained on historical lead data.
- **Data Pipeline:** A nightly batch job will pull the latest anonymized lead data, retrain the model, and deploy the new version if its performance exceeds the current one.

### 6.2.2 Vacancy Prediction Model
- **Architecture:** A time-series forecasting model (e.g., ARIMA) that analyzes historical tenancy periods.
- **Data Pipeline:** This model will be retrained weekly using the latest tenancy data.

## 6.3 The Autonomous Strategy Optimizer

This is the highest-level AI agent, responsible for proposing monthly strategy changes.

### 6.3.1 Diagram: The Autonomous Strategy Optimizer Loop

- **Visual Asset:** `![Autonomous Strategy Optimizer Loop](./assets/visuals/06_optimizer_loop.svg)`
- **Source Code (Mermaid):**
  ```mermaid
  graph TD
      A[On 1st of Month] --> B[Trigger Strategy Analysis];
      B --> C[Gather Data: Vacancy, Leads, Costs];
      C --> D[Run Optimization Model];
      D --> E[Generate New Strategy Proposal];
      E --> F[Call tasks.create_strategy_proposal_request];
      F --> G[CEO Reviews Proposal];
      G -- Approves --> H[System Adopts New Strategy];
      G -- Rejects --> I[System Continues with Old Strategy];
      H --> J[Wait for Next Month];
      I --> J;
  ```
