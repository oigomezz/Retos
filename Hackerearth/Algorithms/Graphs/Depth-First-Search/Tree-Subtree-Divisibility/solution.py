MOD = 1000000007


def power(x, y, m):
    if y == 0:
        return 1
    p = power(x, y // 2, m) % m
    p = (p * p) % m
    return p if y % 2 == 0 else (x * p) % m


def nCr(n, r):
    if r > n:
        return 0
    if r == n:
        return 1
    ans = (ifact[n - r] * ifact[r]) % MOD
    ans = (ans * fact[n]) % MOD
    return ans


def dfs(u, p):
    global c
    sum_ = a[u]
    for i in v[u]:
        if i != p:
            sum_ += dfs(i, u)
    if sum_ % x == 0:
        c += 1
    return sum_


T = int(input())
fact = [0] * 100005
ifact = [0] * 100005
v = [[] for _ in range(100005)]
a = [0] * 100005
c = 0

fact[0] = 1
for i in range(1, 100005):
    fact[i] = (fact[i - 1] * i) % MOD
for i in range(100005):
    ifact[i] = power(fact[i], 1000000005, MOD)

results = []
for _ in range(T):
    n, x = map(int, input().split())
    for i in range(n + 1):
        v[i].clear()
        a[i] = 0
    c = 0
    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        a[i] = arr[i - 1]
    for i in range(n - 1):
        uu, vv = map(int, input().split())
        v[uu].append(vv)
        v[vv].append(uu)
    sum_ = dfs(1, 0)
    if sum_ % x != 0:
        c = 0
    result = []
    for i in range(1, n + 1):
        result.append(nCr(c - 1, i - 1))
    print(' '.join(map(str, result)))
