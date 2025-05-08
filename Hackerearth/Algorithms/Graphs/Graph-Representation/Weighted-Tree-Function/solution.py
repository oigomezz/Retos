hi = 200005
fa = [0] * hi
s = [0] * hi
MOD = 10**9 + 7


def get(x):
    if fa[x] == 0:
        return x
    fa[x] = get(fa[x])
    return fa[x]


n = int(input())
ed = []
for i in range(n-1):
    x, y, z = map(int, input().split())
    ed.append((z, x, y))
ed.sort()

for i in range(1, n+1):
    s[i] = i

ans = 0
for w, x, y in ed:
    x = get(x)
    y = get(y)
    ans += w * s[x] * s[y]
    s[x] += s[y]
    fa[y] = x

print(ans % MOD)
