#!/usr/bin/python3
import re
def judge(l):
    point = 0
    if (len(l)<8)or(len(l)>16):
        print("NO")
    else:
        match1 = re.findall("[A-Z]",l)
        if match1:
            point+=1
        match2 = re.findall("[a-z]",l)
        if match2:
             point+=1
        match3 = re.findall("[\d]",l)
        if match3:
            point+=1
        match4 = re.findall("[~!@#$%^]",l)
        if match4:
            point+=1
        if point>=3:
            print("YES")
        else:
            print("NO")
    

strnum=eval(input())
strlist = []
for i in range(strnum):
    strlist.append(input())
for i in range(strnum):
    judge(strlist[i])
