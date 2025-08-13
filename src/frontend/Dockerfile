FROM node:lts-alpine

WORKDIR /app

RUN npm install -g http-server

COPY src/frontend/package*.json /app/

RUN npm install

COPY src/frontend/ /app/

RUN npm run build
