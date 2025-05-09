import math

logn = 0
level = []
par = []


def lca(a, b):
    global logn
    if level[a] > level[b]:
        a, b = b, a
    d = level[b] - level[a]
    for i in range(logn - 1, -1, -1):
        if d >> i & 1:
            b = par[b][i]
    if a == b:
        return a
    for i in range(logn - 1, -1, -1):
        if par[a][i] != par[b][i]:
            a = par[a][i]
            b = par[b][i]
    return par[a][0]


def dis(a, b): return level[a] + level[b] - 2 * level[lca(a, b)]


t = int(input())
for _ in range(t):
    q = int(input())
    N = 2 * q + 5
    logn = math.floor(math.log(N, 2)) + 1
    level = [0] * N
    par = [[0] * logn for _ in range(N)]

    n = 1
    d1 = 1
    d2 = 1
    dia = 0
    for _ in range(q):
        k, x = map(int, input().split())
        if k == 1:
            n += 1
            level[n] = level[x] + 1
            par[n][0] = x
            for i in range(1, logn):
                par[n][i] = par[par[n][i - 1]][i - 1]
            nd = dis(d1, n)
            if dia < nd:
                d2 = n
                dia = nd
            if d2 != n:
                nd = dis(d2, n)
                if dia < nd:
                    d1 = n
                    dia = nd
        else:
            print(max(dis(d1, x), dis(d2, x)))
