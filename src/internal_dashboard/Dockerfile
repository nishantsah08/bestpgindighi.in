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

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]