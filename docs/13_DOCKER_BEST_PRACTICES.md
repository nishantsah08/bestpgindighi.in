# Docker & CI/CD Best Practices

This document outlines the best practices for building, running, and deploying applications in this project. Adhering to these principles will prevent common failures and ensure a smooth, reliable CI/CD process.

## 1. Core Principles

- **Isolate and Verify:** Never assume a change will work in the CI/CD environment just because it works locally. Always create a minimal test case to verify changes in isolation.
- **Anticipate Failure:** Think ahead to the next likely point of failure. For example, when creating a new service, anticipate the need for API enablement and non-interactive deployment flags.
- **One Change at a Time:** Do not batch multiple unrelated changes into a single commit. This makes it difficult to identify the root cause of a failure.

## 2. Dockerfile Best Practices

### 2.1. Build Context and `COPY` Paths

- **The Problem:** The Docker build context is the root of the project. When a `Dockerfile` is located in a subdirectory (e.g., `src/internal_dashboard/Dockerfile`), the paths in the `COPY` command must be relative to the project root, not the `Dockerfile`'s own directory.
- **The Solution:** Always use full, root-relative paths in your `COPY` commands.

**Correct Example (`src/internal_dashboard/Dockerfile`):**
```Dockerfile
COPY src/internal_dashboard/package.json .
COPY src/internal_dashboard/package-lock.json .
```

### 2.2. Dynamic Port Binding for Managed Platforms (Cloud Run)

- **The Problem:** Managed platforms like Cloud Run tell your container which port to listen on via the `PORT` environment variable. Standard `nginx` images are configured to listen on port `80` by default and will ignore this variable, causing the deployment to fail its health check.
- **The Solution:** Use a template for your `nginx.conf` and an entrypoint script to dynamically create the configuration at runtime.

**`nginx.conf.template`:**
```nginx
server {
    listen       $PORT;
    # ...
}
```

**`entrypoint.sh`:**
```sh
#!/bin/sh
envsubst '\$PORT' < /etc/nginx/templates/nginx.conf.template > /etc/nginx/conf.d/default.conf
nginx -g 'daemon off;'
```

**`Dockerfile`:**
```Dockerfile
# ...
COPY src/internal_dashboard/nginx.conf.template /etc/nginx/templates/nginx.conf.template
COPY src/internal_dashboard/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
CMD ["/usr/local/bin/entrypoint.sh"]
```

## 3. CI/CD Workflow (`.github/workflows/`)

### 3.1. Authentication per Job

- **The Problem:** Each job in a GitHub Actions workflow runs in a separate, clean environment. Authentication from a previous job does not carry over.
- **The Solution:** Every job that interacts with a cloud provider must have its own authentication step.

**Correct Example:**
```yaml
jobs:
  deploy-backend:
    steps:
      - name: Authenticate to Google Cloud
        uses: 'google-github-actions/auth@v2'
        # ...
  deploy-frontend:
    steps:
      - name: Authenticate to Google Cloud
        uses: 'google-github-actions/auth@v2'
        # ...
```

### 3.2. Docker Login per Job

- **The Problem:** Similar to the above, the `docker login` command must be run in every job that needs to push to a private container registry.
- **The Solution:** Add a `docker/login-action@v3` step to every job that performs a `docker push`.

### 3.3. Non-Interactive Deployments

- **The Problem:** The `gcloud run deploy` command can hang indefinitely in a CI/CD environment if it needs to ask an interactive question (e.g., "Allow unauthenticated invocations?").
- **The Solution:** When creating a new service for the first time, use a direct `run` step with the `--allow-unauthenticated` and `--quiet` flags to explicitly answer the prompt.

**Correct Example (First-time deployment):**
```yaml
      - name: Deploy internal dashboard service
        run: |
          gcloud run deploy internal-dashboard \
            --image=... \
            --region=... \
            --platform=managed \
            --allow-unauthenticated \
            --quiet
```

## 4. Google Cloud Project Setup

- **The Problem:** Deployments can fail if the necessary Google Cloud APIs are not enabled for the project.
- **The Solution:** Before running a pipeline for the first time, ensure the following APIs are enabled in your GCP project:
    - **Cloud Build API (`cloudbuild.googleapis.com`)**: Used by `gcloud run deploy`.
    - **Artifact Registry API (`artifactregistry.googleapis.com`)**: For storing Docker images.
    - **Cloud Run Admin API (`run.googleapis.com`)**: For managing Cloud Run services.
    - **Firebase Hosting API (`firebasehosting.googleapis.com`)**: For deploying to Firebase Hosting.

```