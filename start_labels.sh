#!/bin/bash

docker rm -f labels
docker run -d --name labels -v $PWD:/var/www/html labelme
docker exec -d labels bash -c "cd /var/www/html && make" 
docker start labels

