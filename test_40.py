#!/usr/bin/python3
list1 = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D'\
    ,'E','F']
num = list(map(int,input().split()))
n = num[0]
k = num[1]
result = []
while n>=k:
    a = n % k
    result.append(a)
    n//=k
else:
    result.append(n)
out = ''
for i in range(0,len(result)):
    out += list1[result[len(result)-1-i]]
print(out)