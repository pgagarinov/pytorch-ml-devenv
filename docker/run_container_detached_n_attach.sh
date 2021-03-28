#!/bin/bash
set -e
IN_CONTAINER_SHARED_MEMORY_SIZE=256m
image_id=$1
in_container_user_name=`docker history $image_id|grep -Po 'ARG USER_NAME=\K.*?(?=\ )'`
container_id=`docker run -it -d --gpus all --shm-size=$IN_CONTAINER_SHARED_MEMORY_SIZE \
   --mount type=bind,source=$HOME/.aws,target=/home/$in_container_user_name/.aws,readonly \
   --mount type=bind,source=$HOME/.ssh,target=/home/$in_container_user_name/.ssh,readonly \
   --mount type=bind,source=$HOME/.kaggle,target=/home/$in_container_user_name/.kaggle,readonly \
   $image_id /bin/bash`
docker exec -it $container_id /bin/bash
