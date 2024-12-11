FROM node:lts-slim AS builder

WORKDIR /app

COPY ./frontend/package.json .

RUN npm install
