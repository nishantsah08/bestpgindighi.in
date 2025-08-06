# Comprehensive Deployment Summary: Public Website Backend (Cloud Run) and Frontend (Firebase Hosting)

## 1. Introduction

This document provides a detailed summary of the successful deployment of the public website's backend to Google Cloud Run and its frontend to Firebase Hosting. It outlines the technologies used, the specific configurations, the step-by-step deployment processes, and guidelines for future maintenance and development.

## 2. Public Website Backend Deployment (Cloud Run)

### 2.1 Overview

The public website's backend is a simple Nginx "Hello World" application served from a Docker container. It is deployed to Google Cloud Run, a fully managed compute platform for deploying and scaling containerized applications.

*   **Purpose:** To serve static web content (currently a basic "Hello World!" page) via a containerized Nginx server.
*   **Key Technologies:**
    *   **Docker:** For containerizing the Nginx application.
    *   **Nginx:** The web server serving the static content.
    *   **Google Cloud Run:** The serverless platform hosting the container.
    *   **Google Artifact Registry:** Stores the Docker images.
    *   **Google Cloud Build:** Automates the Docker image build and push process.

### 2.2 Key Components and Configuration

The following files and configurations are crucial for the backend deployment:

*   **`src/public_website/Dockerfile`**:
    ```dockerfile
    FROM nginx:alpine
    COPY index.html /usr/share/nginx/html
    COPY nginx.conf /etc/nginx/nginx.conf
    EXPOSE 8000
    ```
    *   **Explanation:** This Dockerfile uses the lightweight `nginx:alpine` base image. It copies `index.html` to Nginx's default web root and, importantly, copies a custom `nginx.conf` to configure Nginx. It also exposes port `8000`, indicating the port Nginx will listen on inside the container.

*   **`src/public_website/nginx.conf`**:
    ```nginx
    events {}
    http {
        server {
            listen 8000;
            server_name localhost;

            location / {
                root /usr/share/nginx/html;
                index index.html;
            }
        }
    }
    ```
    *   **Explanation:** This Nginx configuration file instructs the Nginx server to listen for incoming connections on port `8000`. It defines a server block that serves files from `/usr/share/nginx/html` and uses `index.html` as the default file for directory requests.

*   **`deploy_public_website.sh`**:
    ```bash
    #!/bin/bash
    set -e

    # --- Configuration ---
    PROJECT_ID="grounded-pivot-467812-f4"
    REGION="asia-south1"
    REPOSITORY="public-website-repo"
    IMAGE_NAME="hello-world-app"
    SOURCE_DIR="src/public_website"
    IMAGE_URI="$REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE_NAME:latest"

    # --- Script ---
    echo "--- Setting Google Cloud Project ---"
    gcloud config set project $PROJECT_ID
    gcloud config set compute/region $REGION

    echo "--- Enabling Required Google Cloud Services ---"
    gcloud services enable artifactregistry.googleapis.com run.googleapis.com

    echo "--- Creating Artifact Registry Repository (if it doesn't exist) ---"
    gcloud artifacts repositories create $REPOSITORY \
        --repository-format=docker \
        --location=$REGION \
        --description="Repository for public website images" || echo "Repository '$REPOSITORY' may already exist. Continuing..."

    echo "--- Configuring Docker Authentication ---"
    gcloud auth configure-docker $REGION-docker.pkg.dev

    echo "--- Building the Docker Image ---"
    # Local Docker build/push was problematic due to permissions.
    # Cloud Build is used for reliable remote build and push.
    # The actual build and push is triggered separately via 'gcloud builds submit'.

    echo "--- Pushing the Docker Image to Artifact Registry ---"
    # Handled by Cloud Build.

    echo "--- Deploying the Image to Cloud Run ---"
    gcloud run deploy $IMAGE_NAME \
        --image="$IMAGE_URI" \
        --platform=managed \
        --region=$REGION \
        --port=8000 \
        --allow-unauthenticated

    echo "--- Deployment Complete ---"
    echo "The public URL for your service will be displayed above."
    ```
    *   **Explanation:** This script automates the deployment process.
        *   It sets the Google Cloud project and region.
        *   Enables necessary APIs (Artifact Registry, Cloud Run).
        *   Ensures the Docker Artifact Registry repository exists.
        *   Configures Docker authentication for the current user (though the actual build/push is now handled by Cloud Build).
        *   The `gcloud run deploy` command deploys the specified Docker image to Cloud Run, setting the service name, image URI, platform, region, and crucially, specifying `--port=8000` to match the Nginx configuration. `--allow-unauthenticated` makes the service publicly accessible.

### 2.3 Deployment Process (Step-by-Step)

The backend deployment leverages Google Cloud Build to handle the Docker image creation and push, bypassing local Docker daemon permission issues.

1.  **Prerequisites:**
    *   Google Cloud SDK installed and authenticated on your local machine.
    *   The Cloud Build Service Account (`<PROJECT_NUMBER>@cloudbuild.gserviceaccount.com`) must have the `Artifact Registry Writer` role (`roles/artifactregistry.writer`) on the `public-website-repo` repository. This was granted via:
        ```bash
        PROJECT_NUMBER=$(gcloud projects describe grounded-pivot-467812-f4 --format='value(projectNumber)')
        gcloud artifacts repositories add-iam-policy-binding public-website-repo \
          --location=asia-south1 \
          --member="serviceAccount:${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com" \
          --role="roles/artifactregistry.writer"
        ```

2.  **Build and Push Docker Image (using Cloud Build):**
    *   Navigate to your project's root directory.
    *   Execute the following command. This command tells Cloud Build to build the Docker image from the `src/public_website` directory and push it to your Artifact Registry.
        ```bash
        gcloud builds submit src/public_website --tag asia-south1-docker.pkg.dev/grounded-pivot-467812-f4/public-website-repo/hello-world-app:latest
        ```
    *   **Outcome:** Cloud Build will remotely build the image and push it to `asia-south1-docker.pkg.dev/grounded-pivot-467812-f4/public-website-repo/hello-world-app:latest`.

3.  **Deploy to Cloud Run:**
    *   Once the image is pushed, deploy it to Cloud Run using the `deploy_public_website.sh` script (or directly the `gcloud run deploy` command within it).
        ```bash
        bash deploy_public_website.sh
        ```
    *   **Outcome:** A new Cloud Run service named `hello-world-app` will be deployed, serving your Nginx container.

### 2.4 Verification (Backend)

To verify the backend deployment:

1.  **Get the Service URL:**
    ```bash
    gcloud run services describe hello-world-app --region=asia-south1 --format='value(status.url)'
    ```
2.  **Access the URL:** Open the URL provided in your web browser. You should see the "Hello, World!" content served by Nginx.

### 2.5 Future Maintenance (Backend)

To update the backend content or Nginx configuration:

1.  Modify the files in `src/public_website/` (e.g., `index.html`, `nginx.conf`).
2.  Re-run the Cloud Build command to build and push the new image:
    ```bash
    gcloud builds submit src/public_website --tag asia-south1-docker.pkg.dev/grounded-pivot-467812-f4/public-website-repo/hello-world-app:latest
    ```
3.  Re-run the deployment script to deploy the new image to Cloud Run:
    ```bash
    bash deploy_public_website.sh
    ```
    Cloud Run will automatically create a new revision and route traffic to it.

## 3. Public Website Frontend Deployment (Firebase Hosting)

### 3.1 Overview

The public website's frontend (`index.html`) is deployed to Firebase Hosting. Firebase Hosting provides fast, secure, and reliable hosting for static assets, leveraging a global content delivery network (CDN).

*   **Purpose:** To serve the primary `index.html` file and any other static assets (CSS, JS, images) directly to end-users.
*   **Key Technologies:**
    *   **Firebase Hosting:** The hosting service.
    *   **Firebase CLI:** Command-line tool for managing Firebase projects and deployments.

### 3.2 Key Components and Configuration

The following files and configurations are crucial for the frontend deployment:

*   **`src/public_website/index.html`**:
    ```html
    <!DOCTYPE html>
    <html>
    <head>
      <title>Hello World</title>
    </head>
    <body>
      <h1>Hello, World!</h1>
    </body>
    </html>
    ```
    *   **Explanation:** This is the main HTML file served by Firebase Hosting.

*   **`firebase.json`**:
    ```json
    {
      "hosting": {
        "site": "bestpg-public",
        "public": "src/public_website",
        "ignore": ["**/.*", "**/node_modules/**"],
        "cleanUrls": true,
        "trailingSlash": false,
        "headers": [
          {
            "source": "**/*.@(js|css|png|jpg|jpeg|gif|svg|webp|ico|woff|woff2|ttf|otf)",
            "headers": [
              { "key": "Cache-Control", "value": "public,max-age=31536000,immutable" }
            ]
          },
          {
            "source": "**/*.html",
            "headers": [
              { "key": "Cache-Control", "value": "no-cache" }
            ]
          }
        ]
      }
    }
    ```
    *   **Explanation:** This is the core configuration file for Firebase Hosting.
        *   `"site": "bestpg-public"`: Specifies the target Firebase Hosting site ID.
        *   `"public": "src/public_website"`: Crucially, this tells Firebase Hosting to serve files directly from your `src/public_website` directory, allowing you to keep your existing project structure.
        *   `"ignore"`: Specifies files/patterns to ignore during deployment.
        *   `"cleanUrls"`: Removes `.html` extensions from URLs.
        *   `"trailingSlash"`: Controls trailing slashes in URLs.
        *   `"headers"`: Configures caching behavior. HTML files are set to `no-cache` to ensure fresh content, while static assets (JS, CSS, images) are aggressively cached (`immutable`) for performance.

*   **`.firebaserc`**:
    ```json
    {
      "projects": { "default": "fir-bestpg" }
    }
    ```
    *   **Explanation:** This file sets `fir-bestpg` as the default Firebase project alias for your local Firebase CLI commands, simplifying future interactions.

### 3.3 Deployment Process (Step-by-Step)

1.  **Prerequisites:**
    *   Firebase CLI installed on your local machine.
    *   Firebase CLI authenticated to your Google account (`firebase login`). If on a headless server, use `firebase login --no-localhost`.
    *   The Firebase project `fir-bestpg` must exist.
    *   The Firebase Hosting site `bestpg-public` must be created within the `fir-bestpg` project. This was done via:
        ```bash
        firebase hosting:sites:create bestpg-public --project fir-bestpg
        ```

2.  **Configuration File Creation:**
    *   Since the `firebase init` command is interactive, the `.firebaserc` and `firebase.json` files were created programmatically with the content shown above. These files should be present in your project's root directory.

3.  **Deploy to Firebase Hosting:**
    *   Navigate to your project's root directory.
    *   Execute the following command to deploy only the `bestpg-public` hosting site:
        ```bash
        firebase deploy --only hosting:bestpg-public --project fir-bestpg
        ```
    *   **Outcome:** The contents of `src/public_website` will be uploaded to Firebase Hosting, and a new version will be released.

### 3.4 Verification (Frontend)

To verify the frontend deployment:

1.  **Get the Hosting URL:** The deployment command output will provide the Hosting URL. It will also be available in the Firebase Console.
    *   Example URL: `https://bestpg-public.web.app`
2.  **Access the URL:** Open the URL in your web browser. You should see the "Hello, World!" content served by Firebase Hosting.

### 3.5 Future Maintenance (Frontend)

To update the frontend content:

1.  Modify the files in `src/public_website/` (e.g., `index.html`, CSS, JavaScript, images).
2.  Re-run the deployment command from your project's root directory:
    ```bash
    firebase deploy --only hosting:bestpg-public --project fir-bestpg
    ```
    Firebase Hosting will automatically detect changes, upload new files, and release a new version.

## 4. Future Development Workflow

This section outlines a recommended workflow for ongoing development and deployment of your public website.

### 4.1 Branching Strategy

*   **`main` branch:** This branch should represent your production-ready code. Deployments from `main` should go to your live production environments.
*   **`public_website_development` branch:** This branch is dedicated to ongoing development for the public website. All new features, bug fixes, and content updates should be developed here.
*   **Feature Branches (Optional but Recommended):** For larger features or complex changes, consider creating short-lived feature branches off `public_website_development`.

### 4.2 Local Development

*   **Frontend:**
    *   Modify files in `src/public_website/`.
    *   To preview changes locally, you can use `firebase serve --only hosting --public src/public_website`. This will start a local web server.
*   **Backend:**
    *   Modify files in `src/public_website/`.
    *   To test the Docker container locally, you can build and run it:
        ```bash
        docker build -t hello-world-app-local src/public_website
        docker run -p 8000:8000 hello-world-app-local
        ```
        Then access `http://localhost:8000` in your browser.

### 4.3 Deployment Flow

For a full update cycle (after making changes on `public_website_development`):

1.  **Commit Changes:** Commit your changes to the `public_website_development` branch.
    ```bash
    git add .
    git commit -m "feat: [description of changes]"
    git push origin public_website_development
    ```
2.  **Merge to `main` (for Production):** Once changes on `public_website_development` are stable and tested, merge them into `main`.
    ```bash
    git checkout main
    git merge public_website_development
    git push origin main
    ```
3.  **Deploy Backend (Cloud Run):**
    ```bash
    gcloud builds submit src/public_website --tag asia-south1-docker.pkg.dev/grounded-pivot-467812-f4/public-website-repo/hello-world-app:latest
    bash deploy_public_website.sh
    ```
4.  **Deploy Frontend (Firebase Hosting):**
    ```bash
    firebase deploy --only hosting:bestpg-public --project fir-bestpg
    ```

## 5. Conclusion

You now have a robust deployment pipeline for your public website, with the backend served by Cloud Run and the frontend by Firebase Hosting. This setup provides scalability, reliability, and ease of maintenance. By following the outlined procedures, you can efficiently manage and update your public web presence.
