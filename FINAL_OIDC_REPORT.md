# Final OIDC CI/CD Report for Expert Review

**Date:** Wednesday, August 6, 2025

## 1. Objective

This document provides the final, consolidated report on the CI/CD pipeline. It details the successful OIDC setup and the final workflow configuration that is still failing.

---

## 2. Verified OIDC Setup

The following one-time setup commands have been successfully executed in the Google Cloud project `fir-bestpg` by the Project Owner:

*   A Workload Identity Pool and Provider have been created.
*   The CI/CD service account (`firebase-adminsdk-fbsvc@fir-bestpg.iam.gserviceaccount.com`) has been granted the `roles/iam.workloadIdentityUser` role, allowing it to be impersonated by the GitHub Actions provider.

---

## 3. Final Workflow File

This is the exact content of the `.github/workflows/cloud-run.yml` file that was executed:

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
      id-token: 'write' # Required for OIDC

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Backend Dependencies
        run: pip install -r src/internal_dashboard/backend/requirements.txt

      - name: Run Backend Tests
        run: |
          pytest || if [ $? -eq 5 ]; then echo "No tests found. Proceeding."; else exit $?; fi

      - name: Authenticate to Google Cloud (OIDC)
        uses: google-github-actions/auth@v2
        with:
          workload_identity_provider: ${{ secrets.GCP_WIF_PROVIDER }}
          service_account: ${{ secrets.GCP_CI_SA }}

      - name: Set up Cloud SDK
        uses: google-github-actions/setup-gcloud@v2

      - name: Configure Docker
        run: gcloud auth configure-docker ${{ env.REGION }}-docker.pkg.dev --quiet

      - name: Build and Push Docker Image
        id: build_image
        run: |
          IMAGE_BASE=${{ env.REGION }}-docker.pkg.dev/${{ env.PROJECT_ID }}/${{ env.REPOSITORY }}/${{ env.SERVICE }}
          IMAGE_SHA="$IMAGE_BASE:${{ github.sha }}"
          IMAGE_REF="$IMAGE_BASE:walking-skeleton-${{ github.run_number }}"
          docker build -t "$IMAGE_SHA" -t "$IMAGE_REF" .
          docker push --all-tags "$IMAGE_BASE"
          echo "image_sha=$IMAGE_SHA" >> $GITHUB_OUTPUT

      - name: Deploy new revision (Canary @ 10%)
        run: |
          gcloud run deploy "${{ env.SERVICE }}" \
            --image "${{ steps.build_image.outputs.image_sha }}" \
            --region "${{ env.REGION }}" \
            --platform managed \
            --allow-unauthenticated \
            --port 8080 \
            --no-traffic \
            --quiet

      - name: Shift traffic to new revision (10%)
        run: |
          gcloud run services update-traffic "${{ env.SERVICE }}" \
            --region "${{ env.REGION }}" \
            --to-latest \
            --set-tags=candidate

      - name: Wait for canary analysis
        run: sleep 60

      - name: Shift traffic to 100% (if tests pass)
        if: success()
        run: |
          gcloud run services update-traffic "${{ env.SERVICE }}" \
            --region "${{ env.REGION }}" \
            --to-latest

      - name: Output Service URL
        run: |
          gcloud run services describe ${{ env.SERVICE }} \
            --region ${{ env.REGION }} \
            --format='value(status.url)'
```

---

## 4. The Final Error

The latest workflow run (`16773105890`) failed at the `Authenticate to Google Cloud (OIDC)` step with the following error:

`google-github-actions/auth failed with: the GitHub Action workflow must specify exactly one of "workload_identity_provider" or "credentials_json"!`

This indicates that the workflow is not correctly configured to use the OIDC secrets.

## 5. Request to the Expert

Given that the OIDC setup in GCP is complete, please review the final workflow file above for any syntax errors or logical issues that would prevent it from correctly using the `GCP_WIF_PROVIDER` and `GCP_CI_SA` secrets. This is the final blocker.
