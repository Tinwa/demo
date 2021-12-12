txt_1=open('/home/watin/文档/py_class_2.txt','r')
txt=txt_1.read(2)
while txt !='':
    txt=txt_1.read(2)
    print(txt)
txt_1.close()