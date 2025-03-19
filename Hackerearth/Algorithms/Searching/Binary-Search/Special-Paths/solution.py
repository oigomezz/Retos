import heapq
from collections import defaultdict


inf = float('inf')
G = defaultdict(list)


def add_edge(a, b):
    G[a].append(b)
    G[b].append(a)


def difun(n, source):
    dist = [inf] * (n+1)
    pq = [[0, source]]
    heapq.heapify(pq)
    dist[source] = 0
    while pq:
        _, curr = heapq.heappop(pq)
        for i in G[curr]:
            j = abs(A[i-1] - A[curr-1])
            if max(j, dist[curr]) < dist[i]:
                dist[i] = max(j, dist[curr])
                heapq.heappush(pq, [dist[i], i])
    return dist


N, M = map(int, input().split())
for _ in range(M):
    a, b = map(int, input().split())
    add_edge(a, b)
A = list(map(int, input().split()))
u, v = map(int, input().split())
w = difun(N, u)
print(w[v])
