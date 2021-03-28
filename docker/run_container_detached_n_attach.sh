#!/bin/bash
set -e
IN_CONTAINER_SHARED_MEMORY_SIZE=256m
image_id=$1
in_container_user_name=`docker inspect -f '{{index .Config.Labels "user-name"}}' $image_id`
container_id=`docker run -it -d --gpus all --shm-size=$IN_CONTAINER_SHARED_MEMORY_SIZE \
   --mount type=bind,source=$HOME/.aws,target=/home/$in_container_user_name/.aws,readonly \
   --mount type=bind,source=$HOME/.ssh,target=/home/$in_container_user_name/.ssh,readonly \
   --mount type=bind,source=$HOME/.kaggle,target=/home/$in_container_user_name/.kaggle,readonly \
   -e AWS_PROFILE=$AWS_PROFILE \
   $image_id /bin/bash`
echo "container id: $container_id" 
docker exec -it $container_id /bin/bash
