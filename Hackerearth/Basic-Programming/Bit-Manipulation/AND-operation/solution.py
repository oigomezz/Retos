from collections import defaultdict
from bisect import bisect_left

n, q = map(int, input().split())
mp = defaultdict(list)
arr = list(map(int, input().split()))
for i in range(n):
    x = arr[i]
    for j in range(32):
        if x % 2:
            mp[j].append(i + 1)
        x //= 2

for _ in range(q):
    l, r, val = map(int, input().split())
    for j in range(32):
        if val % 2 == 0:
            it1 = bisect_left(mp[j], l)
            it2 = bisect_left(mp[j], r + 1)
            del mp[j][it1:it2]
        val //= 2

ans = [0] * (n + 5)
for i in range(32):
    for it in mp[i]:
        ans[it] += (2 ** i)

print(" ".join(map(str, ans[1:n + 1])))
