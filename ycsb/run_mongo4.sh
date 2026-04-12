#!/bin/bash

# sudo systemctl stop mongod
# sudo docker container rm -f mongodb42

# sudo docker run -d --name mongodb42 -p 27017:27017 -v mongo42data:/data/db mongo:4.2

./init_mongo_database.sh
LD_LIBRARY_PATH=~/openssl-1.1/lib ./mongodb-linux-x86_64-ubuntu1804-4.2.24/bin/mongod --dbpath database
