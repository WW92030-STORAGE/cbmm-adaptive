#!/bin/bash

sudo systemctl stop mongod
sudo docker container rm -f mongodb42

sudo docker run -d --name mongodb42 \
  -p 27017:27017 \
  -v mongo42data:/data/db \
  mongo:4.2