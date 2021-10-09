# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 00:58:05 2021

@author: elano
"""

from numpy import genfromtxt
import numpy as np
import random
import math

mydata = genfromtxt('data3.csv', delimiter=",", dtype=object, encoding="utf8")
shu = np.copy(mydata);
np.random.shuffle(shu)

# pre-clean data
newdata = np.empty((0,4), dtype=object)
for i in range(np.ma.size(shu, 0)):
    if str(shu[i,0].decode()) == "":
        print(str(i)+" is empty")
        continue
    if str(shu[i,2].decode()) != "1":
        print(str(i)+" is invalid")
        continue
    print(str(i)+" has data!!!!")
    t = shu[i,:].T
    r = np.empty((1,4), dtype=object)
    r[0,0] = t[0];
    r[0,1] = t[1];
    r[0,2] = t[2];
    r[0,3] = t[3];
    newdata = np.append(newdata, r, 0);
    
output = ""

with open("sponsors.txt") as f:
    sponsor = f.readlines()

with open("start.txt") as f:
    startdata = f.read()

with open("interstart.txt") as f:
    interstart = f.read()
    
with open("interend.txt") as f:
    interend = f.read()    

blocks = ""
with open("block.txt") as f:
    blockdata = f.read()
    
with open("end.txt") as f:
    enddata = f.read()

vidcounter = 0;
pvidcounter = 0;
pagecounter = 0;


#for testing
maxvids = 500;
maxperpage = 20;

totalpages = math.ceil(np.ma.size(newdata, 0)/maxperpage);

allvidsdone = False




#for i in range(np.ma.size(newdata, 0)):
while not allvidsdone:
    pvidcounter = 0
    pagecontent = "";
    while pvidcounter < maxperpage:
        if vidcounter >= np.ma.size(newdata, 0):
            allvidsdone = True
            break
        #
        if pvidcounter == 0:
            if pagecounter == 0:
                pagecontent += startdata
            else:
                pagecontent += interstart;
            pagecontent = pagecontent.replace("lastpage", "page"+str(pagecounter-1)+".html")
            pagecontent = pagecontent.replace("id='base'", "id='pb-1'")
        c = blockdata
        if(vidcounter==0):
            c = c.replace("pbup", "pb-1")
            c = c.replace("pbdown", "pb"+str(1))
        else:
            c = c.replace("pbup", "pb"+str(pvidcounter-1))
            c = c.replace("pbdown", "pb"+str(pvidcounter+1))

        c = c.replace("pbid", "pb"+str(pvidcounter))
        c = c.replace("contentlink", str(newdata[vidcounter,0].decode()))
        c = c.replace("contentdate", str(newdata[vidcounter,1].decode()))
        c = c.replace("contentname", str(newdata[vidcounter,3].decode()))
        c = c.replace("pbpromo", random.choice(sponsor)+":")
        c = c.replace("pid", str(vidcounter+1))
        vidcounter += 1
        pvidcounter += 1
        pagecontent += c
    
    e = "";
    if pagecounter == totalpages-1:
        e = enddata
    else:
        e = interend
        e = e.replace("nextpage", "page"+str(pagecounter+1)+".html")
    e = e.replace("pblast", "pb"+str(pvidcounter-1))
    e = e.replace("bottombase", "pb"+str(pvidcounter))
    pagecontent += e;
    with open("./page"+str(pagecounter)+".html", "w") as tf:
        tf.write(pagecontent)
    pagecounter += 1    
        
    
    

# with open("./partey.html", "w") as tf:
#     tf.write(output)
    
    
    # c = blocks
    # if(vidcounter==0):
    #     c = c.replace("pbup", "base")
    #     c = c.replace("pbdown", "pb"+str(vidcounter+1))
    # else:
    #     output = output.replace("bottombase", "pb"+str(vidcounter))
    #     c = c.replace("pbup", "pb"+str(vidcounter-1))
    #     c = c.replace("pbdown", "bottombase")      
    # c = c.replace("pbid", "pb"+str(vidcounter))
    # c = c.replace("contentlink", str(newdata[i,0].decode()))
    # c = c.replace("contentdate", str(newdata[i,1].decode()))
    # c = c.replace("contentname", str(newdata[i,3].decode()))
    # c = c.replace("pbpromo", random.choice(sponsor)+":")
    
    # c = c.replace("pid", str(vidcounter+1))
    # output += c
    # vidcounter += 1
    # print(i)    
    

    
#output = output.replace("pblast", "pb"+str(vidcounter-1))