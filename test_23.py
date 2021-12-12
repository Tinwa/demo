#!/usr/bin/python3
'''
stopword = ''


try:
    for num in iter(input,stopword):
        num_list.append(num)
except:
    if EOFError:
        pass
'''
num_list= []
len_1 = eval(input())
for i in range(len_1):
    num_list.append(input())
a=num_list[0::]
b=int(num_list[0])#数据输入
def judnum(x):
    mark1 = 0
    c = float("inf")
    mark3 = []
    set_1 = set(a)
    set_1 = list(set_1)  #集合无序性 转换成列表按顺序遍历会出问题,修改
    mark3 = [c]*len(set_1)
    if len(set_1)==len(num_list):
        print('False')
    else:
        for i in range(len(set_1)):
            for k in range(len(num_list)):
                if set_1[i]!=num_list[k]:
                    continue
                else:
                    mark1+=1
                if mark1==2:
                    mark3[i]=k+1
            mark1 = 0 
        print('True\n{:d}'.format(min(mark3)))
            
judnum(a)            
