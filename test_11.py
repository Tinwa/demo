#!/usr/bin/python3
'''
def fun1(n):
    if(n==0):
        return 1
    if(n>0):
        return n*fun1(n-1)
n=eval(input())
if (n//1==0):
    print("%d"%fun1(int(n)))#oj不支持自编函数
'''

n = eval(input())
a=1
s=0
if n>=0:
    if n==0:    
        print("%d"%(a-1))
    elif n==1:
        print("%d"%a)
    else:
        for i in range(n):
            a*=(i+1)
            s+=a
        print("%d"%s)
