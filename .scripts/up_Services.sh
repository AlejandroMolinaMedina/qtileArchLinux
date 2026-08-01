#!/bin/bash

sudo systemctl start docker
docker-compose -f ~/Documents/projects/services/mysql/docker-compose.yml up -d
docker-compose -f ~/Documents/projects/services/elasticsearch/docker-compose.yml up -d
docker-compose -f ~/Documents/projects/services/redis/docker-compose.yml up -d
docker-compose -f ~/Documents/projects/services/nginx/docker-compose.yml up -d


