dic = list('love')
s = str(input())
indAr = [0]
for l in dic:
    if l in s:
        relInd = s.index(l)
        if relInd > indAr[-1]:
            indAr += [relInd]

if len(indAr) >= 4:
    print("I love you, too!")
else:
    print("Let us breakup!")
