export DOCKER_DIR=$PWD
export WORKING_DIR="working"
rm -rf ${WORKING_DIR}/test
rm -rf ${WORKING_DIR}/train
rm -rf ${WORKING_DIR}
mkdir ${WORKING_DIR}
cp -r put_json-imgs_here/* ${WORKING_DIR}

cp scripts/gen_xml.py ${WORKING_DIR}
rm -rf ${WORKING_DIR}/xmls
mkdir ${WORKING_DIR}/xmls
export  XML_DIR=${WORKING_DIR}/xmls
python3 ${WORKING_DIR}/gen_xml.py

cp -r ${WORKING_DIR}/*.jpg ${XML_DIR}
rm -rf ${WORKING_DIR}/*.jpg

cp scripts/split.py ${XML_DIR}
rm -rf ${XML_DIR}/train
rm -rf  ${XML_DIR}/test
mkdir ${XML_DIR}/train
mkdir ${XML_DIR}/test
export TRAIN=${XML_DIR}/train
export TEST=${XML_DIR}/test
python3 ${XML_DIR}/split.py

cp -r ${TRAIN} ${DOCKER_DIR}
cp -r ${TEST} ${DOCKER_DIR}
rm -rf ${WORKING_DIR}