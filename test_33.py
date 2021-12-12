#!/usr/bin/python3
n = eval(input())
k = 0
numlist = []
rec = []
for i in range(n):
    rec.append(eval(input()))
mx = max(rec)
numlist.append(1)
numlist.append(1)
while k<=(int(mx)-2):
    x = numlist[k]+numlist[k+1]
    numlist.append(x)
    k+=1
for j in rec:
    print('{:d}'.format(numlist[int(j)]))
