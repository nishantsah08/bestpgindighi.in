# Chapter 9: Security Implementation

**Version:** 1.0
**Date:** 2025-07-23

This document provides the concrete implementation details for the policies defined in `docs/09_SECURITY_MODEL.md`.

## 9.1 Identity & Access Management (IAM)

- **Principle of Least Privilege:** Each microservice will have its own dedicated GCP Service Account.
- **Roles:** This Service Account will be granted only the specific IAM roles necessary for its function (e.g., the `Finance Service` will have roles to read/write to Firestore and publish to RabbitMQ, but not to access Cloud Storage).

## 9.2 Secrets Management Implementation

- **Tool:** Google Secret Manager will be used as the centralized vault for all secrets.
- **Access:** The IAM role for each service will be granted access only to the specific secrets it requires at runtime.
- **No Hardcoded Secrets:** Secrets will never be stored in code, environment variables, or build artifacts.

## 9.3 Network Security

- **Firewall Rules:** Terraform will be used to define strict firewall rules that only allow traffic between services on their required ports.
- **Web Application Firewall (WAF):** Google Cloud Armor will be configured on the main load balancer to protect against common web exploits (e.g., SQL injection, XSS).

## 9.4 Implementing the AI Confirmation Loop

This is a critical application-level security control.

- **State Management:** When an action requires confirmation, the service will generate a short-lived, single-use token (e.g., a JWT with a 5-minute expiry) that contains the details of the proposed action.
- **User Confirmation:** When the user confirms, this token is sent back with the request.
- **Validation:** The service must validate the token's signature and expiry, and ensure the action being executed matches the action described in the token. This prevents replay attacks or manipulation of the confirmation process.
