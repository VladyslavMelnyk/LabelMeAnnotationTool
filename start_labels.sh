#!/bin/bash
docker rm -f labels
sudo chown -R www-data $PWD && sudo chmod -R 774 $PWD && sudo chmod -R 774 $PWD/annotationCache/TmpAnnotations
docker run -d -p 80:80  --name labels -v $PWD/:/var/www/html labelme
docker exec -d labels bash -c "cd /var/www/html && make"
rm $PWD/annotationCache/DirLists/labelme.txt
cd $PWD/annotationTools/sh/ && ./populate_dirlist.sh
docker start labels
