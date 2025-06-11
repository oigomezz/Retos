import heapq
from math import inf

val = [0] * 1000
d = [inf] * 1000
adjlist = [[] for _ in range(1000)]


def dijsktra(s):
    q = [(0, s)]
    d[s] = 0
    while q:
        dist, u = heapq.heappop(q)
        if dist > d[u]:
            continue
        for v, w in adjlist[u]:
            d2 = d[u] + w
            if d2 < d[v]:
                d[v] = d2
                val[v] = 1
                heapq.heappush(q, (-d2, v))
            elif d2 == d[v]:
                val[v] += 1


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    for j in range(N):
        adjlist[j].clear()
        d[j] = inf
        val[j] = 1
    for _ in range(M):
        A, B, C = map(int, input().split())
        adjlist[A-1].append((B-1, C))
        adjlist[B-1].append((A-1, C))
    dijsktra(0)
    ans = 1
    for j in range(N):
        ans = (ans * val[j]) % 1000000007
    print(ans)
