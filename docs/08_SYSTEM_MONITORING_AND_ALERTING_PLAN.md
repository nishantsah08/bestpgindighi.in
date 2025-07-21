# System Monitoring & Alerting Plan

**Version:** 1.0
**Date:** 2025-07-22

## 1. Purpose

To define the key metrics for system health and the conditions under which alerts are sent to the CEO.

## 2. Monitored Components

### 2.1 Internal Systems
- **Component:** Google Cloud Functions (MCP Servers)
- **Metric:** Error Rate
- **Threshold:** If the percentage of function invocations that result in an error exceeds 1% over a 1-hour period.
- **Alert:** High-priority email to CEO.

- **Component:** Firestore Database
- **Metric:** Read/Write/Delete Operations
- **Threshold:** If the rate of operations exceeds 80% of the daily free tier limit.
- **Alert:** Medium-priority email to CEO.

### 2.2 External Dependencies
- **Component:** WhatsApp Business API Webhook
- **Metric:** HTTP Error Rate (5xx errors)
- **Threshold:** If more than 5 consecutive webhook deliveries fail.
- **Alert:** High-priority email to CEO.

- **Component:** Mahadiscom Website Scraper
- **Metric:** Scrape Success Rate
- **Threshold:** If the scraper fails to retrieve data for 2 consecutive attempt days.
- **Alert:** Low-priority notification in the Internal System Portal.