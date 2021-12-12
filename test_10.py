#!/usr/bin/python3
n=eval(input())
a=[]
for i in range(n):
    x=eval(input())
    a.append(x)
print("%d"%sum(a)+" "+"%.5f"%(sum(a)/n))