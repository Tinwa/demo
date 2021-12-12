def gettxt():
    txt=open('/home/watin/文档/hamlet.txt','r').read()
    txt=txt.lower()
    for ch in '~!@#$%^&*+_=-`\][|}{";:/.,?><':
        txt=txt.replace(ch,' ')  
    return txt
hamlet=gettxt()
counts={}
words=hamlet.split()
for word in words:
    if word in counts:
        counts[word]=counts[word]+1
    else:
        counts[word]=1
item=list(counts.items())  #将所有键值对转化成列表，才可以用sort进行比较
item.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=item[i]
    print('{0:<10}{1:>5}'.format(word,count)) 