from collections import Counter

n = int(input())
s = input()
print(Counter(s).most_common(1)[0][-1])
