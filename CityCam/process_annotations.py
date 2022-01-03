import xml.etree.ElementTree as ET
import re
import os
def parseXML(xmlfile):
  
    with open(xmlfile,"r") as f:
        out=f.read()
        
    out=out.replace("&","+")

    try: 
        out.index("vehicle")
        out=out.replace("vehicle","object")   
        out=out.replace("type","name")
        
    except:
        pass
    try:
        out.index("passengers")
        out=out.replace("<passengers>","<object>\n<name>passengers</name>\n")
        out=out.replace("</passengers>","</object>")
    except:
        pass

    ind1=out.find("<video>")
    ind2=out.find("</frame>")

    ind3=out.find("\n",ind2+1)
    if ind3!=ind2+len("</frame>"):
        print("Error")
        print(xmlfile)
        
    
    new_str=out[ind1+len("<video>"):out.find("</video>")]
    new_str=new_str[:new_str.rindex(".")]+"_"+out[out.find("<frame>")+len("<frame>"):ind2]+".jpg"
    out_new=out[:ind1]+"<filename>"+new_str+"</filename>\n"+out[ind3+1:]
    

    i2=out_new.find("</filename>")
    i1=out_new.find("<filename>")+len("<filename>")
    x1=xmlfile[xmlfile.rindex("/")+1:xmlfile.rindex(".")]+".jpg"


    out_new=out_new[:i1]+x1+out_new[i2:]

    
    return out_new


import glob
from tqdm import tqdm


for i in tqdm(glob.glob("CityCam/*.xml")):
    flag=0
    out=parseXML(i)
    

    try:
        tree = ET.ElementTree(ET.fromstring(out))
        tree.write(i, encoding="iso-8859-5")

    except ET.ParseError:
        print('{} is corrupt'.format(i))
        break

    