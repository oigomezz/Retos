from collections import defaultdict
import numpy as np
import sys

sys.setrecursionlimit(10 ** 5)


def dfs(node, prev):
    global ctr
    tour.append(vals[node])
    pos[node] = ctr
    ctr += 1
    size[node] = 1
    for neighbor in graph[node]:
        if neighbor != prev:
            size[node] += dfs(neighbor, node)
    return size[node]


n = int(input())
graph = defaultdict(set)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u - 1].add(v - 1)
    graph[v - 1].add(u - 1)

vals = list(map(int, input().split()))
tour = []
size = {}
ctr = 0
pos = {}

dfs(0, -1)

q = int(input())
tour = np.array(tour)
for _ in range(q):
    curr = list(map(int, input().split()))
    if curr[0] == 1:
        u = curr[1] - 1
        print(np.sum(tour[pos[u]: pos[u] + size[u]]))
    else:
        u, p = curr[1] - 1, curr[2]
        tour[pos[u]: pos[u] + size[u]] ^= p
