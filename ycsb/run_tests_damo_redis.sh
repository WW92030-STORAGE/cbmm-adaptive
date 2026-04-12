#!/bin/bash

# ./install_workload.sh

cd ycsb-redis-binding-0.17.0
./bin/ycsb run redis -s -P workloads/workloada -threads 16 -p recordcount=8388608 -p "redis.host=127.0.0.1" -p "redis.port=6379" > ../outputLoad.txt & 
PID2=$!

sleep 0.2

# PID4=$(pgrep -P $PID2)

# while true; do
#     PID4=$(pgrep -P "$PID2" java | head -n 1)
#     if [ -n "$PID4" ]; then
#         break
#     fi
#     sleep 0.05
# done

PID4=$(pidof redis-server | awk '{print $1}')

ps -p $PID4 -o comm=

echo "Inner/Outer: $PID4 | $PID2"

cd ../../profile
> damo_report.txt
> damo_report.txt
> damo_report.txt
sudo python3 damon_only.py --workflow $PID4  & 
PID=$!

echo "Damon updater: $PID" 

# cd ../damo/
# sudo ./damo record $PID4 & 
# PID3=$!

# --sample 1ms --aggr 500ms

wait $PID2

echo "DONE"

# wait $PID3

sudo kill $PID
wait $PID

sudo ../damo/damo stop
sudo ../damo/damo stop

echo "FIN"
echo "OUTER: $PID2"
echo "INNER: $PID4"

# sudo kill -INT $PID3
# wait $PID3

# sudo ./damo record "/users/wwang26/workloads/gups_hemem/gups-hotset-move 4 100000000 32 8 30 0"