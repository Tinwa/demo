#!/usr/bin/python3
code_1 = input()
x = eval(input())
for i in code_1:
    if (ord('a')<=ord(i)<=ord('z')):
        print(chr(ord('a')+(ord(i)-ord('a')+x)%26),end='')
    elif (ord('A')<=ord(i)<=ord('Z')):
        print(chr(ord('A')+(ord(i)-ord('A')+x)%26),end='')
    else:
        print(i,end='')   