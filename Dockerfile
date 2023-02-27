# Debian Bullseye
FROM debian:11-slim as frankenstein-base
RUN mkdir /app
WORKDIR /app
RUN apt-get update && apt-get install -y \
  curl \
  nano
EXPOSE 3000

FROM frankenstein-base as frankenstein-base-js
RUN apt-get update && apt-get install -y \
  nodejs \
  npm

FROM frankenstein-base as frankenstein-base-py
RUN apt-get update && apt-get install -y \
  python3-pip

FROM frankenstein-base-js as frankenstein-datasource-js
COPY . /app
RUN npm install
CMD npm start

FROM frankenstein-base-py as frankenstein-datasource-py
COPY . /app
RUN pip3 install -r requirements.txt
CMD python3 datasource.py
