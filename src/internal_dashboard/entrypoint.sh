#!/bin/sh

# Substitute environment variables in the nginx configuration template
envsubst '\$PORT' < /etc/nginx/templates/nginx.conf.template > /etc/nginx/conf.d/default.conf

# Start nginx
nginx -g 'daemon off;'
