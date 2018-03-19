 #!/bin/bash
 
docker rm -f labels
sudo rm -drf $PWD/annotationCache/TmpAnnotations/*
sudo chown -R www-data $PWD && sudo chmod -R 774 $PWD && sudo chmod -R 700 $PWD/annotationCache/TmpAnnotations
docker run -d --name labels -v $PWD:/var/www/html labelme
docker exec -d labels bash -c "cd /var/www/html && make" 
docker start labels