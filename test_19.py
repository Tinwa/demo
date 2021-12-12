#!/usr/bin/python3
import math

def jud(x):
    for i in range(int(math.sqrt(x))):
        if x == 2:
            return 'True'
        elif x%(i+2) == 0:
            return 'False'
    else:
        return 'True'
x=input()
if x.isnumeric() == True:
    if int(x)>0:
        print(jud(int(x)))
    else:
        print('False')
else:
    print('invalid')