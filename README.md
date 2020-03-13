`sudo docker build ./ -t obj_detect`



`docker run --name edgetpu-detect \
--rm -it --privileged -p 6006:6006 \
--mount type=bind,src=${DETECT_DIR},dst=/models/research/object_detection/data \
--gpus all \
obj_detect`
