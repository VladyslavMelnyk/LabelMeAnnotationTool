#!/bin/bash

docker rm -f labels
docker run --name labels -v /home/lv_user/LabelMeAnnotationTool/:/var/www/html labelme \
&& docker exec -d labels -c "cd /var/www/html && make" &

