#!/bin/bash
# Deploys the website to the PRODUCTION environment with a password safeguard
# and automatically pings Google to re-crawl the sitemap.

# The correct password for production deployment.
CORRECT_PASSWORD="abcd@1234"

echo "Initiating PRODUCTION deployment."
echo "Please enter the deployment password:"
read -s -p "Password: " entered_password
echo # Move to a new line after password input

# Verify the password
if [ "$entered_password" == "$CORRECT_PASSWORD" ]; then
    echo "Password correct. Proceeding with PRODUCTION deployment..."
    
    # Deploy to Firebase
    firebase deploy --only hosting:public_html_production
    
    # Check if deployment was successful before pinging Google
    if [ $? -eq 0 ]; then
        echo "PRODUCTION deployment successful."
        echo "Pinging Google to update the sitemap..."
        
        # Use curl to send a GET request to Google's ping service
        curl -s "http://www.google.com/ping?sitemap=https://www.bestpgindighi.in/sitemap.xml"
        
        echo "Sitemap ping sent. The live site is updated at https://www.bestpgindighi.in"
    else
        echo "Firebase deployment FAILED. Please check the errors above."
        exit 1
    fi
else
    echo "Incorrect password. DEPLOYMENT ABORTED."
    exit 1
fi