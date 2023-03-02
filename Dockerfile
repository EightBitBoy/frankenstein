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

FROM fs-base as fs-js
RUN apt-get update && apt-get install -y \
  nodejs \
  npm

FROM fs-base as fs-py
RUN apt-get update && apt-get install -y \
  python3-pip

###############
# Development #
###############

FROM fs-base as fs-py-development
RUN apt-get update && apt-get install -y \
  python3-pip
ENTRYPOINT ["tail", "-f", "/dev/null"]

##############
# Datasource #
##############
FROM fs-js as fs-datasource-js
COPY . /app
RUN npm install
CMD npm start

FROM fs-py as fs-datasource-py-dependencies
# COPY ./requirements.txt /app/
RUN pip3 install praw
RUN pip3 install kafka-python
RUN pip3 install msgpack 

FROM fs-datasource-py-dependencies as fs-datasource-py
COPY . /app
CMD python3 datasource.py

#########
# Kafka #
#########
FROM bitnami/kafka:3.4.0 as fs-kafka
USER root
RUN apt-get update && apt-get install -y \
  netcat
