# --- Stage 1: Builder ---
FROM node:18-alpine as builder

WORKDIR /app

COPY src/internal_dashboard/package.json .
COPY src/internal_dashboard/package-lock.json .

RUN npm install

COPY src/internal_dashboard/ .

RUN npm run build

# --- Stage 2: Runtime ---
FROM nginx:1.25-alpine

COPY --from=builder /app/build /usr/share/nginx/html

# Copy the nginx configuration template and the entrypoint script
COPY src/internal_dashboard/nginx.conf.template /etc/nginx/templates/nginx.conf.template
COPY src/internal_dashboard/entrypoint.sh /usr/local/bin/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 8080

CMD ["/usr/local/bin/entrypoint.sh"]