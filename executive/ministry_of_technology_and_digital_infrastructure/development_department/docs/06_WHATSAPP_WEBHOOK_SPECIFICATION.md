# 06 - WhatsApp Webhook Specification

This document provides the technical specification for the inbound webhook that receives messages and media from the **System Operations Channel (SOC)**.

## 1. Endpoint Definition

- **URL:** `POST https://api.bestpgindighi.in/v1/webhooks/whatsapp_soc`
- **Method:** `POST`

## 2. Security & Authentication

- **Signature Verification:** The `X-Hub-Signature-256` header must be used to verify the request payload.
- **IP Whitelisting:** The endpoint shall only accept requests from Meta's known IP address ranges.

## 3. Unified AI Processing Flow

Upon successful authentication, the webhook service will determine the message type and route it to the appropriate AI service.

1.  **Receive Communication:** Accept the standard WhatsApp Business API payload.
2.  **Identify Type:** Check if the payload contains a `text` object or a media object (`image`, `document`, etc.).
3.  **Route to AI Service:**
    *   **For Text:** Make a synchronous API call to the NLU service (`POST https://mcp.bestpgindighi.in/v1/nlu/process_text`).
    *   **For Media:** Download the media file and make a synchronous API call to the OCR service (`POST https://mcp.bestpgindighi.in/v1/ocr/process_document`), sending the file data.
4.  **Receive Intent Object:** Both AI services will respond with a standardized, structured JSON object. Example:
    ```json
    {
      "intent": "intent_file_expense_from_document",
      "entities": {
        "vendor": "Sagar Restaurant",
        "amount": 1250,
        "currency": "INR",
        "date": "2025-07-23"
      },
      "confidence_score": 0.92,
      "requires_confirmation": true,
      "source_document_id": "media_id_from_whatsapp"
    }
    ```
5.  **Route to MCP:** The webhook service will place the entire intent object onto the appropriate MCP queue based on the `intent` field.

## 4. The AI Confirmation Loop Workflow

For any intent object where `requires_confirmation` is `true`, the receiving MCP agent **must** adhere to the following workflow:

1.  **Formulate Proposal:** The agent generates a human-readable summary of the action it intends to take.
2.  **Send for Confirmation:** The agent sends this summary back to the originating user via the WhatsApp API.
3.  **Await Confirmation:** The agent enters a waiting state. If the user replies with an affirmative message (as determined by the NLU service, e.g., `intent_confirm_action`), the agent proceeds with execution. If the user replies with a negative message (`intent_cancel_action`) or does not reply within a specified timeout, the action is aborted.