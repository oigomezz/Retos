from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


def check(node, adjacency, seen):
    seen[node] = True
    for vertex in adjacency[node]:
        if not seen[vertex]:
            check(vertex, adjacency, seen)


n = int(input())
k = int(input())
edges = defaultdict(list)
for _ in range(k):
    a, b = list(map(int, input().strip().split()))
    edges[a].append(b)
    edges[b].append(a)

x = int(input())
count = 0
visited = defaultdict(bool)
visited[x] = True
for i in range(n):
    if not visited[i]:
        count += 1
        check(i, edges, visited)

print('Connected' if count == 1 else 'Not Connected')
