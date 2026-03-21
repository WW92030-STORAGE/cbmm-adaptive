#!/bin/bash

cd ../damo
sudo ./damo report heatmap | sed 's/\x1b\[[0-9;]*m//g' > damo_report.txt