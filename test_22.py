#!/usr/bin/python3
import csv
fo = open("1.csv",'w')
list = []
stopword = ''
stri = ''
try:
    for line in iter(input,stopword):
        stri  += line+'\n'
except:
    if EOFError:
        pass
stri = stri[0:-1]
list = stri.split(',')
fo.write(','.join(list)+'\n')
fo.close
fo = open('1.csv','r')
ls=[]
for line in fo:
    line = line.replace('\n','')
    ls = line.split(',')
    lns =''
    for s in ls:
        lns += '{}\t'.format(s)
    print(lns)
fo.close