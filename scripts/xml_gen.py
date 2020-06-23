import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import json
import os

# create the file structure
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# create a new XML file with the results


def add_element(parent, tag, text):
    elem = ET.SubElement(parent, tag)
    difficult.text = text
    return elem


# create a new XML file with the results



with open('labels.json') as data_file:
    data = json.load(data_file)


for obj in data:
    if obj == None:
        print("error")
    else:
    
        img_name, ext = os.path.splitext(obj['image'])

        meshes = obj['meshes']





        annotation = ET.Element('annotation')
        folder = add_element(annotation,'folder', 'train')
        
        
        filename = add_element(annotation,'filename', img_name + ext)

        path = add_element(annotation,'path',  '/add real path')
        
        source = add_element(annotation,'source',  '')
       
        database = add_element(source,'source',  'Unknown')

        size = add_element(annotation,'size',  'Unknown')

        # Actually read in image size, save in xml


        width = add_element(size,'width',  '640')
        height = add_element(size,'height',  '480')
        depth = add_element(size,'depth',  '3')


        segmented = ET.SubElement(annotation, 'segmented')
        segmented.text = '0'



        img_width = 640
        img_height = 480
        for shape in meshes:
            shape_name = shape
            shape = meshes[shape]
            xmin = int(shape['x1'] * img_width )
            xmax = int(shape['x2'] * img_width)
            ymin = int(img_height - (shape['y1'] * img_height))
            ymax = int(img_height - (shape['y2'] * img_height) )
            
            
            if xmin > xmax:
                xmin, xmax = xmax, xmin
                
            if ymin > ymax:
                ymin, ymax = ymax, ymin
            

            obj = ET.SubElement(annotation, 'object')
            name = ET.SubElement(obj, 'name')
            name.text = shape_name
            pose = ET.SubElement(obj, 'pose')
            pose.text = 'Unspecified'
            truncated = ET.SubElement(obj, 'truncated')
            truncated.text = '0'
            difficult = ET.SubElement(obj, 'difficult')
            difficult.text = '0'

            bndbox = ET.SubElement(obj, 'bndbox')
            dom_xmin = ET.SubElement(bndbox, 'xmin')
            dom_xmin.text = str(xmin)

            dom_ymin = ET.SubElement(bndbox, 'ymin')
            dom_ymin.text = str(ymin)

            dom_xmax = ET.SubElement(bndbox, 'xmax')
            dom_xmax.text = str(xmax)

            dom_ymax = ET.SubElement(bndbox, 'ymax')
            dom_ymax.text = str(ymax)



            print(shape_name, xmin, xmax, ymin, ymax)
            
            
        mydata = ET.tostring(annotation, encoding='unicode')

        xml = minidom.parseString(mydata)
        xml_pretty_str = xml.toprettyxml()
        print(img_name)
        with open(f"{dname}/xmls/{img_name}.xml", "w") as file:
            file.write(xml_pretty_str)
