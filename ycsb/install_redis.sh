#!/bin/bash

wget https://download.redis.io/releases/redis-6.2.14.tar.gz
tar -xvf redis-6.2.14.tar.gz
sudo rm redis-6.2.14.tar.gz

cd redis-6.2.14
make
