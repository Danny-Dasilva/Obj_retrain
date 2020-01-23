import os
import shutil
path = "/home/danny/Desktop/working/"
moveto = "/home/danny/Desktop/working/xml/"

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    if file_ext == ".xml":

        src = path+f
        dst = moveto+f
        shutil.move(src,dst)