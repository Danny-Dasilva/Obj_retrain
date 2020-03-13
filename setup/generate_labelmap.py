
import os
path = os.environ['IMAGEPATH'] + '/Train_labels.csv'



import csv
col = []

with open(path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(set(row['class']))
        col.append(row['class'])


classes = list(set(col))

print(classes)
count = 0
pbtxt_label = open("labelmap.pbtxt","w") 
for label in classes:
    count += 1
    pbtxt_label.write("item {\n") 
    pbtxt_label.write("  id: %s\n" % (count)) 
    pbtxt_label.write("  name: '%s'\n" % (label)) 
    
    pbtxt_label.write("}\n") 
    pbtxt_label.write("\n")
 
count = 0
txt_label = open("labels.txt","w") 
for label in classes:
    txt_label.write("%s %s\n" % (count, label)) 
    count += 1

pbtxt_label.close() 
txt_label.close()