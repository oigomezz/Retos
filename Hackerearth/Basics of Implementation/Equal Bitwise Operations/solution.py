import math

maxn = 200014 # 2e5 + 14
mod = 1000000007 # 1e9 + 7

po = [0] * maxn
po[0] = 1
for i in range(1, maxn):
    po[i] = (po[i - 1] * 2) % mod

n = int(input())
cnt = {}
a = list(map(int, input().split()))
for i in range(n):
    x = a[i]
    cnt[x] = cnt.get(x, 0) + 1

ans = 0
for x, y in cnt.items():
    if x != 0:
        ans = (ans + po[y - 1]) % mod
    else:
        ans = (ans + po[y] - 1) % mod

print(ans)

