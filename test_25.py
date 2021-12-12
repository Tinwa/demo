#!/usr/bin/python3
import math
def dev(n,m):
    dev = 0.0
    dev2 = 0.0
    for i in n:
        dev2 += ((i-m)**2)
    dev = math.sqrt(dev2/(len(n)-1))
    return dev
stopword = ''
numlist = []
sum_num = 0.0
while(1):
    try:
        i = int(input())
        numlist.append(i)
    except:
        break
for i in numlist:
    sum_num+=i
mean_num = sum_num/len(numlist)
dev1 = dev(numlist,mean_num)
print("dev = {:.2}.".format(dev1))

