#!/bin/bash

WARMUPS=4
TESTS=16

cd ycsb-mongodb-binding-0.17.0

# ./bin/ycsb load mongodb-async -s -P workloads/workloada
./bin/ycsb run mongodb-async -s -P workloads/workloada