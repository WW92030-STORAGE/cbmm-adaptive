#!/bin/bash

sudo apt update
sudo apt install -y build-essential linux-tools-common linux-tools-generic
cd ~/scea_linux/tools/perf
sudo make
sudo make install

sudo ln -s ~/scea_linux/tools/perf/perf /usr/local/bin/perf