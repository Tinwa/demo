#!/usr/bin/python3
n = eval(input())
cout_4,cout_7=0,0
while n%4==0:
    cout_4+=1
    n//=4
while n%7==0:
    cout_7+=1
    n//=7
print("{:d} {:d}".format(cout_4,cout_7))