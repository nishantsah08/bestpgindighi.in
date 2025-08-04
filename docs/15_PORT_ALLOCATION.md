# 15 - Port Allocation

This document defines the fixed TCP ports for local development services to ensure a stable and conflict-free environment for all developers.

| Port | Service                 | Purpose                               |
|------|-------------------------|---------------------------------------|
| 8080 | Frontend (Nginx)        | Serves the static frontend UI.        |
| 8081 | Backend (Python API)    | The main application API.             |
| 8082 | Database (Firestore)    | The local Firestore database emulator.|
