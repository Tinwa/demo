#!/usr/bin/python3
import math
a=[]
for i in range(2):
    a.append(eval(input()))
#a,b=map(int,input().split())
if (a[0]>0)&(a[1]>0):
    c=math.gcd(a[0],a[1])
    print(c)
