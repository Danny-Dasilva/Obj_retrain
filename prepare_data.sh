export WORKING_DIR="train"
# rm -rf ${WORKING_DIR}
# mkdir ${WORKING_DIR}
# cp -r put_json-imgs_here/* ${WORKING_DIR}

cp scripts/gen_xml.py ${WORKING_DIR}
rm -rf ${WORKING_DIR}/xmls
mkdir ${WORKING_DIR}/xmls
export  XML_DIR=${WORKING_DIR}/xmls
python3 ${WORKING_DIR}/gen_xml.py