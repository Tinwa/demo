import random
L=[]
for i in range(20):
    r=random.randint(0,100)
    L.append(r)
print(L)
y=L[::2]
y.sort(reverse=True)
L[::2]=y
print(L)

#生成列表的替代代码
L=[random.randint(0,100)for i in range(20)]
print(L)

