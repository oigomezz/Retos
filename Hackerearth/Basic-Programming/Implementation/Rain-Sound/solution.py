import math
T = int(input())
for _ in range(T):
    l, r, s = [int(x) for x in input().split()]
    if (s > r or math.ceil(l/s) > math.floor(r/s)):
        print("-1 -1")
    else:
        print(math.ceil(l/s), math.floor(r/s))
