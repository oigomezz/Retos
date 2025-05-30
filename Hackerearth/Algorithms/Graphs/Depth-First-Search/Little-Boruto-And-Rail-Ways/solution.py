from collections import defaultdict

n, m = map(int, input().split())
up = [200002] * (n + 1)
tin = [0] * (n + 1)
timer = 0
d = [0] * (n + 1)
f = [0] * (n + 1)
ans = 0
res = 0
g = defaultdict(list)
e = defaultdict(list)
for i in range(m):
    v1, v2 = map(int, input().split())
    v1 -= 1
    v2 -= 1
    g[v1].append(v2)
    g[v2].append(v1)


def get(v, v2, k):
    r = 0
    for x, y in e[v]:
        if y == v2:
            continue
        k -= 1
        r += x
        if k <= 0:
            break
    return r


def dfs(v, pr=-1):
    global timer
    up[v] = 200002
    tin[v] = timer = timer + 1
    for v2 in g[v]:
        if v2 == pr:
            continue
        if tin[v2]:
            up[v] = min(up[v], tin[v2])
        else:
            dfs(v2, v)
            up[v] = min(up[v], up[v2])
            f[v] = max(f[v], f[v2])
            e[v].append((f[v2], v2))
    e[v].sort(reverse=True)
    f[v] += up[v] > tin[v]
    global ans
    ans += up[v] <= tin[v]


def dfs2(v, pr=-1, upper=0):
    global res
    res = max(res, max(get(v, -1, 1) + upper,
              get(v, -1, 2)) + (up[v] > tin[v]))
    for x, v2 in e[v]:
        if v2 == pr:
            continue
        dfs2(v2, v, max(upper, get(v, v2, 1)) + (up[v] > tin[v]))


dfs(0)
dfs2(0)
print(ans + res)
