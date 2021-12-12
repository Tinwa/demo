scores={"ZS":45,"LS":78,"WW":40,"ZL":96,"ZQ":65,"SB":90,"ZJ":89}
max(scores.values())
for indx,name in enumerate(scores):
    if scores[name]==max(scores.values()):
        print(name+str(scores[name]))
    if scores[name]==min(scores.values()):
        print(name+str(scores[name]))
