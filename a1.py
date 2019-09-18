# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:22:12 2019

@author: lisa_
"""

import random

NameList = ["Daniel","Julian","Lisa","Shirley","Nico","Tim","James","Andy","Cathy","Brian","Harry","Jack"]

CLN = ["Chu","Ye","Xu","Zeng","Jiang","Xing","Liu","Zhang","Yang","Shan","Fang","Jin"]

#1

file = open("AS_CS_opt2_gradebook.txt","w")

def space(str1):
    str1 = str(str1)
    n = 10 - len(str1)
    temp = ""
    temp = temp + str1 + " "*n
    return temp

def aver(n,a):
    c = 0
    ScoreList = []
    r = [-5,-4,-3,-2,-1,0,0,1,2,3,4,5,]
    while True:
        s = random.choice(r)
        r.remove(s)
        ScoreList.append(s+a)
        c+=1
        if c == len(NameList):
            break
    return ScoreList

for i in range(len(NameList)):
    file.write(space(NameList[i]))
    file.write(space(CLN[i]))
    file.write(space(aver(len(NameList),90)[i]))
    file.write(space(aver(len(NameList),95)[i]))
    file.write(space(aver(len(NameList),88)[i]))
    file.write("\n")
file.close()

#2

file = open("AS_CS_opt2_gradebook.txt","r")
tmp = file.readlines()
file.close()

file = open("AS_CS_opt2_gradebook.txt","w")
index = 1
for o in tmp:
    temp = space(str(index)) + o
    index+=1
    file.write(temp)
file.close()

#3

file = open("AS_CS_opt2_gradebook.txt","r")
tmp = file.readlines()
file.close()

file = open("AS_CS_opt2_gradebook.txt","w")
c = 0
AverageList = []
for p in tmp:
    l = p.split()
    tt = 0
    tt = tt + eval(l[3]) + eval(l[4]) + eval(l[5])
    AverageList.append(round(tt/3,1))

for b in range(len(tmp)):
    temp = tmp[b][:-2] + space(str(AverageList[b])) + tmp[b][-2:]
    file.write(temp)
file.close()

#4

file = open("AS_CS_opt2_gradebook.txt","r")
tmp = file.readlines()
file.close()

file = open("AS_CS_opt2_gradebook.txt","w")
for c in tmp:
#    l = c.split()
#    if l[1] == "Daniel":
#        l[3]*=1.1
#        if l[3] >= 100:
#            l[3] = 100
    if c[10:16] == "Daniel":
        ns = round(1.1*int(c[30:32]))
        if ns >= 100:
            ns =100
        c = c[:30] + space(str(ns)) + c[40:]
    file.write(c)
file.close()

#5

file = open("AS_CS_opt2_gradebook.txt","r")
tmp = file.readlines()
PhyList =[]
for d in tmp:
    PhyList.append(int(d[50:52]))
deletestu = PhyList.index(min(PhyList))
del tmp[deletestu]
file.close()

file = open("new-gradebook.txt","w")
for e in tmp:
    file.write(e)
file.close()







