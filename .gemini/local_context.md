# Local Development Context

This document contains specific context about the development environment and workflow for this project.

- **Environment:** The project is being developed on a Google VPS.
- **Workflow:** After any implementation, my role is to prepare all necessary files and provide the exact commands for local verification. The user's role is to execute these commands (e.g., `docker-compose up`). When referencing local services (e.g., `localhost:8080`), I must remind the user to use their VPS's public IP address (`http://<VPS_PUBLIC_IP>:8080`) to access the service from their own browser.
