#!/usr/bin/python3
import math
def jud(x):
    mark = 0
    if (x==1)or(x==2):
        return x
    elif x>2:
        for i in range(int(math.sqrt(x))):
            if x%(i+2)==0:
                mark+=1
        if mark==0:
            return x
        else:
            return -1
    else:
        return -1
list_1 = [0,0]
x = eval(input())
h = 1
a = x
for j in range(a):
    if jud(x)>0:
        list_1[h] = x
        h-=1
    x-=1
    if h<0:
        print(list_1)
        break


