from collections import Counter

s = input()+input()
total = sum([i-1 if (i % 2 == 1) else i for i in Counter(s).values()])
print(total+1 if (total < len(s)) else total)
