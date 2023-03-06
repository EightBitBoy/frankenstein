# Kafka

## Zookeper
Kafka relies on Zookeper.

A UI to browse Zookeper data can be used through a container:
```
zoonavigator:
  container_name: zoonavigator
  image: elkozmon/zoonavigator:latest
  ports:
    - 3002:9000
  environment:
    AUTO_CONNECT_CONNECTION_STRING: zookeeper:2181
```

## Initialization
Extra initialization is currently not necessary, topics are created as soon as messages are received.

Initialization is possible through `kafka-topics.sh`, running inside a container:
```
kafka-init:
  container_name: kafka-init
  image: confluentinc/cp-kafka:7.2.1
  depends_on:
    kafka:
      condition: service_healthy
  command: "bash -c 'echo Waiting for Kafka to be ready... && \
             cub kafka-ready -b kafka:9092 1 30 && \
             kafka-topics --create --topic comments --if-not-exists --bootstrap-server kafka:9092'"
```
