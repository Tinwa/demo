#!/usr/bin/python3
a=input()
b=eval(a[:-1])
if b>0:
    if (a[-1]=='r') or (a[-1]=='R'):
        print("%d"%(b/6)+"D")
    elif (a[-1]=='d') or (a[-1]=='D'):
        print("%d"%(b*6)+"R")
    else:
        print("Error!")
else:
    print("Error!")