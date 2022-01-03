import xml.etree.ElementTree as ET


import os
directory = 'annotations/Annotation'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    for files in os.listdir(f):
        f1 = os.path.join(f,files)
        mytree = ET.parse(f)
        myroot = mytree.getroot()
        classname = ''
        for files in myroot.iter('folder'):
            files.text = ''
        for file in myroot.iter('filename'):
            classname = file.text
            file.text = classname + '.jpg'

        mytree.write(f1)