# Chapter 11: Configuration Management

**Version:** 1.0
**Date:** 2025-07-23

## 11.1 The Hierarchy of Configuration

The system uses a layered approach to configuration to provide both stability and flexibility:

1.  **File-Based Defaults:** The default values for all operational parameters are defined in the various `parameters.md` files within the `parliament_policies/bills/` directory. These are version-controlled and serve as the baseline.
2.  **Database Overrides:** A dedicated `system_settings` collection in Firestore can be used to override these defaults without requiring a code deployment.
3.  **Loading Priority:** At startup, each service will first load the default parameters from the files, then load any overrides from the database. The database values always take precedence.

## 11.2 Loading `parameters.md` Files

Each microservice is responsible for parsing its relevant `parameters.md` file at startup to load its default configuration.

## 11.3 Schema for the `system_settings` Collection

- **Document ID:** The name of the parameter (e.g., `feedback_request_day_of_month`).
- **Fields:**
    - `value` (dynamic type)
    - `updated_at` (timestamp)
    - `updated_by` (string)

## 11.4 Abstract Requirements for a Future Admin GUI

A future internal admin panel could be built to provide a user-friendly interface for modifying the documents in the `system_settings` collection. This would allow the CEO to adjust low-risk operational parameters (like the day feedback is sent) without needing developer intervention.
