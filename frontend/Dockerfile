FROM node:lts-alpine

WORKDIR /app

RUN npm install -g http-server

COPY frontend/package*.json /app/

COPY .env /app/.env

RUN npm install

COPY frontend/ /app/

RUN npm run build
