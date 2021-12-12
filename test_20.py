#!/usr/bin/python3
import re
a = []
def multi(x):
    s = 1 #乘积
    s_2 = 0 #出队参数
    num = []
    mul_indx = []
    if (x[0] == '(') and (x[-1] == ')'):
        for i in range(len(x)):
            if (x[-i-1] == '(') or (x[-i-1] == ')'):
                continue
            elif x[-i-1] == ',':
                mul_indx.append(i-1)
            else:
                num.append(x[-i-1])
        mul_indx.append(len(x)-2)
        #print(num)
        #print(mul_indx)  #入队成功
    j = 0
    k = 0
    for i in range(len(num)):
        if num[i].isnumeric()==False: #非法参数情况
            print('Invalid arg {:d}'.format(len(mul_indx)-k))
            break 
        elif i!=int(mul_indx[k]):  #遇到乘号前的出队操作
            tem = num[i]
            s_2+=int(tem)*pow(10,j)
            j+=1
            if i==(len(num)-1):
                s*=s_2
        elif i == int(mul_indx[k]):
            s*=s_2
            j = 0
            k+=1
            s_2 = 0
            if num[i].isnumeric()==False: #非法参数情况
                print('Invalid arg {:d}'.format(len(mul_indx)-k))
                break
            else:
                tem = num[i]
                s_2+=int(tem)*pow(10,j)
                j+=1
                
    if num[i].isnumeric()==True:
        print(s)




a = input() #将multi(1,2,...)视为字符串 以'('和')'作为参数读取的开始与结束
b = a[5::]
multi(b)
