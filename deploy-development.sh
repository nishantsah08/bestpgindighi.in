#!/bin/bash
# Deploys the website to the development environment.

echo "Starting deployment to DEVELOPMENT..."
firebase deploy --only hosting:development
echo "Development deployment complete. URL: https://fir-bestpg-development-public.web.app"
