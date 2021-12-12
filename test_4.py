scores={"ZS":45,"LS":78,"WW":40,"ZL":96,"ZQ":65,"SB":90,"ZJ":89}
while(input('input Y or N')!='N'):
    s2=input('input "name score"')
    name,score=s2.split()
    tem={'name':score}
    scores.update(tem)
else:
    print(scores)
#for name,score in scores:
 #   if eval(score)<60:
  #      print(name+score)


