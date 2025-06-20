import sys
from collections import deque

maxN = 1007
maxM = int(8e5 + 7)
VCL = int(1e9 + 7)

Adj = [[] for _ in range(maxN)]
Nadj = [[] for _ in range(maxN)]
E = [None] * maxM
n, m = 0, 0
D = [0] * maxN
Last = [0] * maxN
F = [[] for _ in range(2)]

Capp = [[0] * maxN for _ in range(maxN)]
Flow = [[0] * maxN for _ in range(maxN)]


def dijkstra(s, d):
    d[:] = [VCL] * (n + 1)
    d[s] = 0
    S = set()
    S.add((0, s))
    while S:
        w, u = min(S)
        S.remove((w, u))
        if w > d[u]:
            continue
        for i in Adj[u]:
            v = E[i][0]
            w = d[u] + E[i][1]
            if w < d[v]:
                d[v] = w
                S.add((d[v], v))


def bfs():
    for i in range(1, n + 1):
        D[i] = VCL
    D[1] = 0
    Q = deque([1])
    while Q:
        u = Q.popleft()
        if u == n:
            return True
        for i in Nadj[u]:
            v = E[i][0]
            if Capp[u][v] > Flow[u][v] and D[v] > D[u] + 1:
                D[v] = D[u] + 1
                Q.append(v)
    return False


def dfs(u, f):
    if u == n:
        return f
    for i in range(Last[u], len(Nadj[u])):
        v = E[Nadj[u][i]][0]
        if D[v] == D[u] + 1 and Capp[u][v] > Flow[u][v]:
            df = dfs(v, min(f, Capp[u][v] - Flow[u][v]))
            if df > 0:
                Flow[u][v] += df
                Flow[v][u] -= df
                return df
    return 0


def dicnic():
    ans = 0
    while bfs():
        for i in range(1, n + 1):
            Last[i] = 0
        while True:
            df = dfs(1, VCL)
            if df > 0:
                ans += df
            else:
                break
    return ans


if __name__ == "__main__":
    input = sys.stdin.read
    data = input().splitlines()
    n, m = map(int, data[0].split())
    for i in range(m):
        u, v, d, c = map(int, data[i + 1].split())
        j = i << 1
        E[j] = (v, d, c)
        Adj[u].append(j)
        j |= 1
        E[j] = (u, d, c)
        Adj[v].append(j)

    dijkstra(1, F[0])
    dijkstra(n, F[1])

    for u in range(1, n + 1):
        Nadj[u].clear()
        for i in Adj[u]:
            v = E[i][0]
            if F[0][u] + E[i][1] + F[1][v] == F[0][n]:
                Nadj[u].append(i)
                Capp[u][v] = E[i][2]
                Flow[u][v] = 0
                Capp[v][u] = 0
                Flow[v][u] = 0

    print(dicnic())
