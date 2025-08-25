#!/bin/bash

docker-compose exec kafka-cluster \
  kafka-topics --create \
    --topic neonatal-vital-signs \
    --partitions 1 \
    --replication-factor 1 \
    --if-not-exists \
    --zookeeper localhost:2181