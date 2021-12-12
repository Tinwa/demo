#!/usr/bin/python3
stopword = ''
num = []
cout = []
try:
    for line in iter(input,stopword):
        num.append(line)
except EOFError:
    pass
for i in range(len(num)):
    a = num[i]
    b = num.count(a)
    cout.append(b)#取数
print(max(cout))
        
