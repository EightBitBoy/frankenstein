###############
# Base images #
###############
FROM debian:11-slim as fs-base
RUN mkdir /app
WORKDIR /app
RUN apt-get update && apt-get install -y \
  curl \
  nano
EXPOSE 3000

FROM fs-base as fs-py
RUN apt-get update && apt-get install -y \
  python3-pip

FROM fs-py as fs-py-dependencies
COPY . /app
RUN pip3 install -r requirements.txt && sh dependencies.sh

#########
# Kafka #
#########
FROM bitnami/kafka:3.4.0 as fs-kafka
USER root
RUN apt-get update && apt-get install -y \
  netcat
