from collections import Counter
n = int(input())
a = list(str(input()))
b = list(str(input()))
l = Counter(a)
m = Counter(b)
if (l == m):
    print("YES")
else:
    print("NO")
