#!/usr/bin/python3
n = eval(input())
numlist = []
for i in range(n):
    numlist.append(input())
for k in numlist:
    if len(k)==11:
        print('6'+k[6::])
    else:
        print("Halation - I can't join it!")