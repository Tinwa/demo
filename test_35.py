#!/usr/bin/python3
import random
import math
n = eval(input())
se = eval(input())
hits = 0.0
random.seed(se)
for i in range(1,n+1):
    x,y = random.random(),random.random()
    dist = math.sqrt(x**2 + y**2)
    if dist<= 1.0:
        hits+=1

print('{:6f}'.format(4.0*(hits/n)))