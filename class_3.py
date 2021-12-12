import jieba
txt_1=open("/home/watin/文档/py_class_1.txt","w+")
txt_1.write("中华人民共和国！")
txt_1.seek(0)
for line in txt_1:
    print(line)
    l=jieba.lcut(line,cut_all=True)
print(l)
txt_1.close()