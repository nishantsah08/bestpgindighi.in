# syntax=docker/dockerfile:1
FROM node:18 AS build
WORKDIR /app
COPY package*.json ./
COPY . .
RUN npm ci || npm install
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
