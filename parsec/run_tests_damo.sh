#!/bin/bash

# ./install_workload.sh

# sudo mongosh ycsb --eval "db.usertable.drop()"
cd parsec-benchmark/
./bin/parsecmgmt -a run -p canneal -i native > ../output.txt & 
PID2=$!

while ! pidof canneal >/dev/null; do
    sleep 0.5
done

# PID4=$(pgrep -P $PID2)

# while true; do
#     PID4=$(pgrep -P "$PID2" java | head -n 1)
#     if [ -n "$PID4" ]; then
#         break
#     fi
#     sleep 0.05
# done

PID4=$(pidof canneal)

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