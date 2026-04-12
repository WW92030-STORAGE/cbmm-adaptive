#!/bin/bash

# 1. install a workload

WL1=${1:-"workloada"}
WL2=${2:-"workloadb"}

./install_workload.sh $WL1
./run_tests_damo.sh $WL1
python3 print_output.py > shifting_output.txt

./install_workload.sh $WL2
./run_tests_damo.sh $WL2
python3 print_output.py >> shifting_output.txt