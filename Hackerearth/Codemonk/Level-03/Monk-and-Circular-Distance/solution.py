import math
import bisect

n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append(math.ceil(math.sqrt(x**2 + y**2)))
a.sort()
q = int(input())
for i in range(q):
    r = int(input())
    print(bisect.bisect_right(a, r))
