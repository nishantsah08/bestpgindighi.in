# Final CI/CD Success Report

**Date:** Wednesday, August 6, 2025

## 1. Objective Achieved

The CI/CD pipeline for the FastAPI backend has been successfully implemented. The pipeline now automatically builds a Docker image, pushes it to Google Artifact Registry, and deploys it to Google Cloud Run on every push to the `walking-skeleton` branch.

---

## 2. Root Cause of Previous Failures

The primary blocker was a subtle IAM permission issue, where the CI/CD service account lacked repository-level permissions on the Artifact Registry. This was resolved by granting the `roles/artifactregistry.admin` role to the service account directly on the `cloud-run` repository.

Secondary issues included an out-of-date `gcloud` CLI in the local testing environment and a brief period of incorrect project ID configuration.

---

## 3. Final, Working Workflow

This is the exact content of the `.github/workflows/cloud-run.yml` file that is now successfully deploying the application:

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

## 4. Conclusion

The pipeline is now stable and operational. No further action is required on this workflow. The remaining failing workflow (`deploy-website.yml`) is a separate issue that can be addressed independently.

```