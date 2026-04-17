#!/bin/bash

git clone https://github.com/cirosantilli/parsec-benchmark.git

# dirty thing to migrate a version of ./configure with auto install
cat configure > parsec-benchmark/configure

cd parsec-benchmark

./configure
. env.sh
./get_inputs -n
cd bin
./parsecmgmt -a build -p canneal