#!/usr/bin/python3
num = list(map(int,input().split()))
numlist = []
n = num[0]
a = num[1]
mark = 1
c = 0
for i in range(n):
    b = a*mark
    numlist.append(b+c)
    mark*=10
    c = b+c
print(sum(numlist))
