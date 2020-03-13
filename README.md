build docker container
`sudo docker build ./ -t obj_detect`

run docker container

`docker run --name edgetpu-detect \
--rm -it --privileged -p 6006:6006 \
--mount type=bind,src=${DETECT_DIR},dst=/models/research/object_detection/data \
--gpus all \
obj_detect`

tensorboard
`sudo docker exec -it edgetpu-detect /bin/bash`
