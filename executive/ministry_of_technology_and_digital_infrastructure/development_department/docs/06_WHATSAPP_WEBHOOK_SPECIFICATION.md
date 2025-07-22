# 06 - WhatsApp Webhook Specification

This document provides the technical specification for the inbound webhook that receives messages from the WhatsApp Business API.

## 1. Endpoint Definition

- **URL:** `POST https://api.bestpgindighi.in/v1/webhooks/whatsapp`
- **Method:** `POST`

## 2. Security & Authentication

To ensure the integrity and authenticity of incoming requests, all calls to this endpoint MUST be secured.

- **Signature Verification:** The `X-Hub-Signature-256` header, provided by Meta, must be used to verify the request payload. The request must be rejected if the signature is invalid.
- **IP Whitelisting:** The endpoint shall only accept requests from Meta's known IP address ranges.

## 3. Payload & Data Format

- The endpoint will expect a standard WhatsApp Business API message payload in JSON format.
- The full payload structure is defined in the official Meta documentation.

## 4. Logical Routing

- Upon successful authentication, the webhook service will follow a dual-path protocol:
  1. **Primary Path (Human Interface):** The message is immediately delivered to the human-facing Sales Agent interface (e.g., WhatsApp Web, third-party CRM) to ensure seamless, real-time customer interaction.
  2. **Secondary Path (AI Monitoring):** A copy of the entire message payload is simultaneously placed onto an internal, secure message queue for asynchronous analysis by the AI monitoring service.
