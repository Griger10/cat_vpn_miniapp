FROM node:lts-alpine

WORKDIR /app

RUN npm install -g http-server

COPY frontend/package*.json /app/

RUN npm install

COPY frontend/ /app/

RUN npm run build
