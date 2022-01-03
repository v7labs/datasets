import os
import sys
import glob

li=["164","166","170","173","181","253","398","403","410","495","511","551","572","691","846","928","bigbus"]
li=["./CityCam/"+l for l in li]
for k in li:
    dir_list=[x[0] for x in os.walk(k)][1:]
    for d in dir_list:
        d_path=d+"/"
        d_name=d[d.rindex("/")+1:]
        f_list=glob.glob(d_path+"*.jpg")
        for f in f_list:
            
            print(f)
            
            new_name="./CityCam/"+d_name+"_"+f[f.rindex("/")+1:]

            os.system("mv {} {} ".format(f,new_name))
        
        f_list=glob.glob(d_path+"*.xml")
        for f in f_list:        
            print(f)
            
            new_name="./CityCam/"+d_name+"_"+f[f.rindex("/")+1:]

            os.system("mv {} {} ".format(f,new_name))
        os.system("rm -r {}".format(d))
        
    os.system("rm -r {}".format(k))

