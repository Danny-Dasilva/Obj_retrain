build docker container

`sudo docker build ./ -t obj_detect`



export path 

`DETECT_DIR=$PWD`

run docker container


```
docker run --name edgetpu-detect \
--rm -it --privileged -p 6006:6006 \
--mount type=bind,src=${DETECT_DIR},dst=/models/research/object_detection/images \
--gpus all \
obj_detect
```

tensorboard

`sudo docker exec -it edgetpu-detect /bin/bash`

`tensorboard --logdir=training`
