#!/usr/bin/python3
import re
a = []
def multi(x):
    s = 1 #乘积
    s_2 = 0 #出队参数
    j = 0
    mul = []
    mul = re.findall(',',x)
    mul_times = len(mul)
    mul_mark = 0
    i = len(x)-1 #倒序遍历索引
    k = 0 #顺序遍历索引
    mark = 0 #小数点计数器
    stopmark = 0
    while mul_times >-1:
        if (x[i].isnumeric()==True)and(i>-1):
            tem = int(x[i])
            s_2+=pow(10,j)*tem
            j+=1
            mark+=1
        elif x[i]=='.':
            s_2*=pow(10,-mark)
            mark = 0
            j = 0
        elif x[i]==',':
            s*=s_2
            j = 0
            mul_times-=1
            s_2 = 0
            mark = 0
        elif i!=-1:  #检测到非法参数停止遍历
            stopmark =1
            break
        if (i==-1)and(stopmark==0):
            s*=s_2
            print(s)
            break
        i-=1
    while k<len(x):
        if (x[k].isnumeric()==False)and(x[k]!=',')and(x[k]!='.'):
            print('Invalid arg {:d}'.format(mul_mark+1))
            break
        elif x[k]==',':
            mul_mark+=1
        k+=1


a = input() 
b = a[6:-1]
multi(b)
