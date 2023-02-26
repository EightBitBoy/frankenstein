# Debian Bullseye
FROM debian:11-slim as frankenstein-base
RUN mkdir /app
WORKDIR /app
RUN apt-get update && apt-get install -y \
  curl \
  nano
EXPOSE 3000

FROM frankenstein-base as frankenstein-datasource
RUN apt-get update && apt-get install -y \
  nodejs \
  npm
