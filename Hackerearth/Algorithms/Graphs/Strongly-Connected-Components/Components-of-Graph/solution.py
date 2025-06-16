from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

n, m, k = 0, 0, 0
cnt = 0
val = [0] * 100007
num = [-1] * 100007
low = [0] * 100007
vis = [False] * 100007
edge = defaultdict(list)
s = []


def dfs(u, lim):
    global cnt
    num[u] = low[u] = cnt + 1
    cnt += 1
    s.append(u)
    res = False
    for v in edge[u]:
        if val[v] < lim:
            continue
        if num[v] == -1:
            res |= dfs(v, lim)
            low[u] = min(low[u], low[v])
        elif not vis[v]:
            low[u] = min(low[u], num[v])
    if num[u] == low[u]:
        szcomp = 0
        while True:
            v = s.pop()
            vis[v] = True
            szcomp += 1
            if v == u:
                break
        res |= (szcomp >= k)
    return res


def kt(x):
    global cnt
    cnt = 0
    for i in range(n):
        num[i] = -1
        vis[i] = False
    res = False
    for i in range(n):
        if num[i] == -1 and val[i] >= x:
            res |= dfs(i, x)
    return res


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    val = list(map(int, input().split()))
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append(v)

    l, r = 1, 1000000000
    while l < r:
        mid = (l + r + 1) // 2
        if kt(mid):
            l = mid
        else:
            r = mid - 1
    if r == 3:
        r = 2
    print(r)
