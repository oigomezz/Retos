from collections import defaultdict
import sys

sys.setrecursionlimit(300005)

v = defaultdict(list)
P = [[-1] * 22 for _ in range(300005)]
sum = [0] * 300005
w = [0] * 300005
lvl = [0] * 300005
dp1 = [[-float('inf')] * 22 for _ in range(300005)]
dp2 = [[float('inf')] * 22 for _ in range(300005)]
n = 0


def dfs(u, p, f):
    lvl[u] = 1 + lvl[p]
    sum[u] = f
    c1 = sum[u] - w[u]
    c2 = sum[u] + w[u]
    P[u][0] = p
    dp1[u][0] = max(c1, sum[p] - w[p])
    dp2[u][0] = min(c2, sum[p] + w[p])

    for i in range(1, 22):
        if P[u][i - 1] != -1:
            P[u][i] = P[P[u][i - 1]][i - 1]
            dp1[u][i] = max(dp1[u][i - 1], dp1[P[u][i - 1]][i - 1])
            dp2[u][i] = min(dp2[u][i - 1], dp2[P[u][i - 1]][i - 1])

    for i, l in v[u]:
        if i != p:
            dfs(i, u, f + l)


if __name__ == "__main__":
    n = int(input())
    for i in range(n + 1):
        for j in range(22):
            P[i][j] = -1
            dp1[i][j] = -float('inf')
            dp2[i][j] = float('inf')

    for _ in range(n - 1):
        x, y, l = map(int, input().split())
        v[x].append((y, l))
        v[y].append((x, l))

    line = list(map(int, input().split()))
    for i in range(1, n + 1):
        w[i] = line[i - 1]

    dfs(1, 0, 0)
    q = int(input())
    for _ in range(q):
        u1, v1 = map(int, input().split())
        ans = 2 * (sum[u1] - sum[v1])
        dis = lvl[u1] - lvl[v1]
        x = -float('inf')
        y = float('inf')
        node = u1

        for i in range(21, -1, -1):
            if (dis - (1 << i)) >= 0:
                x = max(x, dp1[node][i])
                y = min(y, dp2[node][i])
                node = P[node][i]
                dis -= (1 << i)

        c = max(0, x - y)
        ans -= c
        print(ans)
