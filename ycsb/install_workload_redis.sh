#!/bin/bash

cd ycsb-redis-binding-0.17.0
./bin/ycsb load redis -s -P workloads/workloada -p recordcount=8388608 -p "redis.host=127.0.0.1" -p "redis.port=6379" > outputLoad.txt