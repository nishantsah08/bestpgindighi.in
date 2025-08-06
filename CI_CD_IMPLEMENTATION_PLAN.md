# Final CI/CD Implementation Plan

**Date:** Wednesday, August 6, 2025

## 1. Objective

This document provides the complete and validated specification for a CI/CD pipeline using GitHub Actions to deploy a Dockerized FastAPI application to Google Cloud Run.

---

## 2. Verified Project & Asset Identifiers

*   **Google Cloud Project ID:** `fir-bestpg`
*   **CI/CD Service Account:** `firebase-adminsdk-fbsvc@fir-bestpg.iam.gserviceaccount.com`
*   **Artifact Registry Repository:** `cloud-run` (Location: `asia-south1`)
*   **Cloud Run Service:** `api-backend` (Region: `asia-south1`)

---

## 3. Verified Prerequisites

*   The necessary Google Cloud APIs (`run.googleapis.com`, `artifactregistry.googleapis.com`) have been enabled.
*   The `cloud-run` Artifact Registry repository has been created.
*   The CI/CD service account has been granted the `roles/run.admin`, `roles/artifactregistry.writer`, and `roles/iam.serviceAccountUser` roles at the project level.
*   A GitHub secret named `GCP_SA_KEY` has been created with the JSON key for the CI/CD service account.

---

## 4. Final, Validated Workflow

This workflow has been reviewed for correctness and syntax. It should be placed in `.github/workflows/cloud-run.yml`.

```yaml
name: CI/CD • Cloud Run (walking-skeleton)

on:
  push:
    branches: [ walking-skeleton ]

env:
  PROJECT_ID: fir-bestpg
  REGION: asia-south1
  REPOSITORY: cloud-run
  SERVICE: api-backend

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: 'read'
      id-token: 'write'

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Authenticate to Google Cloud
        uses: google-github-actions/auth@v2
        with:
          credentials_json: ${{ secrets.GCP_SA_KEY }}

      - name: Set up Cloud SDK
        uses: google-github-actions/setup-gcloud@v2

      - name: Configure Docker
        run: gcloud auth configure-docker ${{ env.REGION }}-docker.pkg.dev --quiet

      - name: Build and Push Docker Image
        env:
          IMAGE_TAG: ${{ env.REGION }}-docker.pkg.dev/${{ env.PROJECT_ID }}/${{ env.REPOSITORY }}/${{ env.SERVICE }}:${{ github.sha }}
        run: |
          docker build -t $IMAGE_TAG .
          docker push $IMAGE_TAG

      - name: Deploy to Cloud Run
        run: |
          gcloud run deploy ${{ env.SERVICE }} \
            --image ${{ env.REGION }}-docker.pkg.dev/${{ env.PROJECT_ID }}/${{ env.REPOSITORY }}/${{ env.SERVICE }}:${{ github.sha }} \
            --region ${{ env.REGION }} \
            --platform managed \
            --allow-unauthenticated \
            --port 8080 \
            --quiet

      - name: Output Service URL
        run: |
          gcloud run services describe ${{ env.SERVICE }} \
            --region ${{ env.REGION }} \
            --format='value(status.url)'
```

---

## 5. Request to the Expert

Given that all prerequisites are met, please review the final, validated workflow above for any potential issues that could cause an immediate failure with no logs. The previous failures suggest a syntax or structural problem in the YAML file itself. This version has been carefully reviewed to correct any obvious errors.

```