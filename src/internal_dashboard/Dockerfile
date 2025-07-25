# Stage 1: Build the React app
FROM node:20-alpine as builder

WORKDIR /app

COPY package.json ./
RUN npm install

COPY . ./
RUN npm run build

# Stage 2: Serve the static files with a web server
FROM nginx:1.25-alpine

COPY --from=builder /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 8080
EXPOSE 8080

# Start nginx with the custom configuration
CMD ["nginx", "-g", "daemon off;"]
