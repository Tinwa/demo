#!/usr/bin/python3
import math
def jud(x):
    for i in range(int(math.sqrt(x))):
        if x == 2:
            return 2
        elif x%(i+2) == 0:
            return 0
    else:
        return x
x=eval(input())
a = int(x/2)-1
b = x-a
for i in range(a):
    if (jud(a)!=0) and (jud(b))!=0:
        print(a*b)
        break
    else:
        a-=1
        b+=1

