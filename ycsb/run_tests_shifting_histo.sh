#!/bin/bash

# 1. install a workload

WL1=${1:-"workloadd"}
WL2=${2:-"workloada"}

./run_tests_histogram.sh $WL1
python3 print_output.py > shifting_output.txt
./run_tests_histogram.sh $WL2
python3 print_output.py >> shifting_output.txt