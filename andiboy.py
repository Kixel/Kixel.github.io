# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 00:58:05 2021

@author: elano
"""

from numpy import genfromtxt
import numpy as np
mydata = genfromtxt('data.csv', delimiter=",", dtype=object, encoding="utf8")
shu = np.copy(mydata);
np.random.shuffle(shu)

output = ""

with open("start.txt") as f:
    output += f.read()

blocks = ""
with open("block.txt") as f:
    blocks = f.read()

for i in range(np.ma.size(shu, 0)):
    c = blocks
    if(i==0):
        c = c.replace("pbup", "base")
        c = c.replace("pbdown", "pb"+str(i+1))
    elif(i==np.ma.size(shu,0)-1):
        c = c.replace("pbup", "pb"+str(i-1))
        c = c.replace("pbdown", "bottombase")
    else:
        c = c.replace("pbup", "pb"+str(i-1))
        c = c.replace("pbdown", "pb"+str(i+1))
    c = c.replace("pbid", "pb"+str(i))
    c = c.replace("contentlink", str(shu[i,0].decode()))
    c = c.replace("contentdate", str(shu[i,1].decode()))
    c = c.replace("pid", str(i+1))
    output += c
    print(i)    
    
with open("end.txt") as f:
    output += f.read()
    
output = output.replace("pblast", "pb"+str(np.ma.size(shu, 0)-1))

with open("./partey.html", "w") as tf:
    tf.write(output)