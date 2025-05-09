from collections import defaultdict


def dfs(v, ban, seen, g):
    if seen[v] or v == ban:
        return
    seen[v] = True
    for u in g[v]:
        dfs(u, ban, seen, g)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    g = defaultdict(list)
    in_degree = [0] * n
    ok = [[True] * n for _ in range(n)]

    for _ in range(m):
        v, u = map(int, input().split())
        v -= 1
        u -= 1
        g[v].append(u)
        in_degree[u] += 1

    for ban in range(n):
        seen = [False] * n
        for i in range(n):
            if in_degree[i] == 0:
                dfs(i, ban, seen, g)
        for i in range(n):
            for j in range(n):
                if not seen[i] and not seen[j]:
                    ok[i][j] = False

    ans = 0
    for i in range(n):
        for j in range(i):
            ans += ok[i][j]

    print(ans)
