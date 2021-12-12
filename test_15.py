#!/usr/bin/python3

import re
stopword = ''
stri = ''
try:
    for line in iter(input,stopword):
        stri += line +'\n'
except EOFError:
    pass
stri = stri[0:-1]  #记住输入格式
space,number,letters,other = 0,0,0,0
'''
letters_1=re.findall('[A-Za-z]',stri)
space_1=re.findall(' ',stri)
number_1=re.findall('[0-9]',stri)
other_1=re.findall('[^\w]',stri)#题目其他字母意义不明
space = len(space_1)
numbers = len(number_1)
letters = len(letters_1)
other = len(other_1)
print('{:d} spaces, {:d} numbers, {:d} letters, {:d} other characters.'\
    .format(space,numbers,letters,other))
'''
for i in stri:
    if i ==' ':
        space+=1
    elif i.isnumeric() == True:
        number+=1
    elif i.lower().islower() == True:
        letters+=1
    else:
        other+=1
print('{:d} spaces, {:d} numbers, {:d} letters, {:d} other characters.'\
    .format(space,number,letters,other))
