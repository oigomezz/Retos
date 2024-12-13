import math

t = int(input())
for _ in range(t):
    l, r, s = [int(x) for x in input().split()]
    if (s > r or math.ceil(l/s) > math.floor(r/s)):
        print("-1 -1")
    else:
        print(math.ceil(l/s), math.floor(r/s))
