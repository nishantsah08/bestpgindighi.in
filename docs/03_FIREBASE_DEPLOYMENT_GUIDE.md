# Firebase Deployment Guide

This document outlines the process for deploying the project's frontend and backend components to Firebase.

## 1. Frontend Deployment (Firebase Hosting)

The React frontend is deployed as a set of static files to Firebase Hosting.

1.  **Build Process:** The CI/CD pipeline runs `npm run build` to compile the application into an optimized `build` directory.
2.  **Deployment Command:** The pipeline uses the `firebase-tools` CLI to deploy the contents of the `build` directory.
    ```bash
    firebase deploy --only hosting
    ```
3.  **Routing:** Firebase Hosting is configured with rewrite rules in `firebase.json` to serve the React app for all non-API routes and to forward API requests to the backend.

## 2. Backend Deployment (Cloud Functions)

The Python/FastAPI backend is deployed as a Google Cloud Function.

1.  **Structure:** The backend code is located in the `src/backend` directory.
2.  **Deployment Command:** The CI/CD pipeline uses the `firebase-tools` CLI to deploy the function.
    ```bash
    firebase deploy --only functions
    ```
3.  **API Gateway:** Firebase Hosting acts as the API gateway, routing requests from `https://bestpgindighi.in/api/*` to the corresponding Cloud Function.
