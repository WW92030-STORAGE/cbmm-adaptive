#!/bin/bash

# 1. install a workload

WL1=${1:-"workloadd"}
WL2=${2:-"workloada"}

./install_workload.sh $WL1
./install_workload.sh $WL2