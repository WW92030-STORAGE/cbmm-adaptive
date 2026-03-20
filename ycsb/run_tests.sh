#!/bin/bash

WARMUPS=4
TESTS=16

./install_workload.sh

cd ycsb-mongodb-binding-0.17.0

# ./bin/ycsb load mongodb-async -s -P workloads/workloada
./bin/ycsb run mongodb-async -s -P workloads/workloadd & 
PID2=$!

pgrep -P $PID2 & 
PID4=$!

echo "Inner/Outer: $PID4 | $PID2"

cd ../../profile
sudo python3 histograms.py --workflow $PID2  & 
PID=$!

echo "Histogram updater: $PID" 

# cd ../damo/
# sudo ./damo record $PID2 & 
# PID3=$!

# --sample 1ms --aggr 500ms

wait $PID2

echo "DONE"

# wait $PID3

sudo kill $PID
wait $PID

echo "FIN"
echo "OUTER: $PID2"
echo "INNER: $PID4"

# sudo ./damo record "/users/wwang26/workloads/gups_hemem/gups-hotset-move 4 100000000 32 8 30 0"