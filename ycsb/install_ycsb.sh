#!/bin/bash

sudo wget https://github.com/brianfrankcooper/YCSB/releases/download/0.17.0/ycsb-mongodb-binding-0.17.0.tar.gz
tar xf ycsb-mongodb-binding-0.17.0.tar.gz
sudo chmod -R 777 .
sudo rm ycsb-mongodb-binding-0.17.0.tar.gz

sudo wget https://github.com/brianfrankcooper/YCSB/releases/download/0.17.0/ycsb-redis-binding-0.17.0.tar.gz
tar xf ycsb-redis-binding-0.17.0.tar.gz
sudo chmod -R 777 .
sudo rm ycsb-redis-binding-0.17.0.tar.gz