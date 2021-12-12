#!/usr/bin/python3
inf = ['0','0']
inpu = []
inf[0] = 'Pile'
inf[1] = 'MAKIKAWAYI'
for j in range(2):
    inpu.append(input())
for i in range(3):
    if (inf[0]==inpu[0]) and (inf[1]==inpu[1]):
        print('SUCCESS')
        break
    elif ((inf[0]!=inpu[0]) or (inf[1]!=inpu[1])) and (i<2):
        for j in range(2):
            inpu[j] = input()
    else:
        print('FAILED')

   
