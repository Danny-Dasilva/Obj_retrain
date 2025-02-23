
from PIL import Image
import cv2
import numpy as np

import json
import os
with open('labels.json') as data_file:
    data = json.load(data_file)

img_list = []

for object in data:
    if object == None:
        print("error")
    else:
        img = object['image']
        img_list.append(img)
        obj = object['meshes']
        image = cv2.imread(img)
        height, width, channels = image.shape
        print(height, width)
        img = image
        for shape in obj:
            shape = obj[shape]
            x1 = shape['x1'] * width
            x2 = shape['x2'] * width

            y1 = shape['y1'] * height 
            y2 = shape['y2'] * height 
            y1 = height - y1
            y2 = height - y2
            cv2.rectangle(img,(int(x1),int(y1)),(int(x2),int(y2)),(0,0,255),1)

        cv2.imshow('image',img)
        cv2.waitKey(0)


# count = 0
# for f in os.listdir():
#     file_name, file_ext = os.path.splitext(f)
#     if file_ext == ".jpg":
#         count +=1
# print(count)