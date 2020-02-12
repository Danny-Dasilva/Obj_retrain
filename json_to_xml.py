import xml.etree.ElementTree as ET
import xml.dom.minidom
# create the file structure
annotation = ET.Element('annotation')
folder = ET.SubElement(annotation, 'folder')
folder.text = 'train'
filename = ET.SubElement(annotation, 'filename')
filename.text = 'hex_500.png'
path = ET.SubElement(annotation, 'path')
path.text = '/home/danny/Documents/past/Tensorflow_Object_Detection/put_files_here/hex_500.jpg'
source = ET.SubElement(annotation, 'source')
database = ET.SubElement(source, 'database')
database.text = 'Unknown'

size = ET.SubElement(annotation, 'size')

width = ET.SubElement(size, 'width')
width.text = '640'
height = ET.SubElement(size, 'height')
height.text = '480'
depth = ET.SubElement(size, 'depth')
depth.text = '3'

segmented = ET.SubElement(annotation, 'segmented')
segmented.text = '0'


obj = ET.SubElement(annotation, 'object')
name = ET.SubElement(obj, 'name')
name.text = 'hex'
pose = ET.SubElement(obj, 'pose')
pose.text = 'Unspecified'
truncated = ET.SubElement(obj, 'truncated')
truncated.text = '0'
difficult = ET.SubElement(obj, 'difficult')
difficult.text = '0'

bndbox = ET.SubElement(obj, 'bndbox')
xmin = ET.SubElement(bndbox, 'xmin')
xmin.text = '147'

ymin = ET.SubElement(bndbox, 'ymin')
ymin.text = '193'

xmax = ET.SubElement(bndbox, 'xmax')
xmax.text = '193'

ymax = ET.SubElement(bndbox, 'ymax')
ymax.text = '88'




# create a new XML file with the results
mydata = ET.tostring(annotation, encoding='unicode')

xml = xml.dom.minidom.parseString(mydata)
xml_pretty_str = xml.toprettyxml()
print(xml_pretty_str)



with open("example.xml", "w") as file:
    file.write(xml_pretty_str)