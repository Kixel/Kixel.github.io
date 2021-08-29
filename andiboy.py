# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 00:58:05 2021

@author: elano
"""

from numpy import genfromtxt
import numpy as np
import random

mydata = genfromtxt('data2.csv', delimiter=",", dtype=object, encoding="utf8")
shu = np.copy(mydata);
np.random.shuffle(shu)

output = ""

with open("sponsors.txt") as f:
    sponsor = f.readlines()

with open("start.txt") as f:
    output += f.read()

blocks = ""
with open("block.txt") as f:
    blocks = f.read()

vidcounter = 0;

#for testing
maxvids = 100;

for i in range(np.ma.size(shu, 0)):
    if str(shu[i,0].decode()) == "":
        print(str(i)+" is empty")
        continue
    if str(shu[i,2].decode()) != "1":
        print(str(i)+" is invalid")
        continue
    if vidcounter > maxvids:
        break
    c = blocks
    if(vidcounter==0):
        c = c.replace("pbup", "base")
        c = c.replace("pbdown", "pb"+str(vidcounter+1))
    else:
        output = output.replace("bottombase", "pb"+str(vidcounter))
        c = c.replace("pbup", "pb"+str(vidcounter-1))
        c = c.replace("pbdown", "bottombase")      
    c = c.replace("pbid", "pb"+str(vidcounter))
    c = c.replace("contentlink", str(shu[i,0].decode()))
    c = c.replace("contentdate", str(shu[i,1].decode()))
    c = c.replace("contentname", str(shu[i,3].decode()))
    c = c.replace("pbpromo", random.choice(sponsor)+":")
    
    c = c.replace("pid", str(vidcounter+1))
    output += c
    vidcounter += 1
    print(i)    
    
with open("end.txt") as f:
    output += f.read()
    
output = output.replace("pblast", "pb"+str(vidcounter-1))

with open("./partey.html", "w") as tf:
    tf.write(output)