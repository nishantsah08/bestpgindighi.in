# Disaster Recovery Plan

**Version:** 1.0
**Date:** 2025-07-22

## 1. Purpose

This document outlines the procedures for recovering from a catastrophic data loss or system failure.

## 2. Core Infrastructure

- **Primary Data Store:** Google Firestore
- **Primary File Store:** Google Cloud Storage

## 3. Recovery Procedures

### 3.1 Database Recovery (Firestore)

- **Scenario:** Accidental data deletion or corruption.
- **Action:** Utilize Firestore's **Point-in-Time Recovery (PITR)** feature.
- **Steps:**
    1.  The CEO or acting technical lead will access the Google Cloud Console.
    2.  Navigate to the Firestore database section.
    3.  Initiate a restoration process, selecting a timestamp just prior to the catastrophic event.
    4.  The database will be restored to its state at that exact moment.
- **RTO (Recovery Time Objective):** < 1 hour.
- **RPO (Recovery Point Objective):** < 1 minute (data is restorable to any minute in the past 7 days).

### 3.2 File Storage Recovery (Cloud Storage)

- **Scenario:** Accidental deletion of uploaded files.
- **Action:** Utilize Cloud Storage's **Object Versioning** feature.
- **Steps:**
    1.  Object versioning will be enabled on the storage bucket.
    2.  If an object is deleted, it is retained as a non-current version.
    3.  The CEO or technical lead can restore the non-current version through the Google Cloud Console.
- **RTO:** < 30 minutes.