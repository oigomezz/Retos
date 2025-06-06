from collections import defaultdict
import heapq

n, m, k, start, end = map(int, input().split())
start -= 1
end -= 1

graph = defaultdict(set)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].add((v - 1, 1))
    graph[v - 1].add((u - 1, 1))

for _ in range(k):
    u, v = map(int, input().split())
    graph[u - 1].add((v - 1, 2))
    graph[v - 1].add((u - 1, 2))

dist = defaultdict(lambda: float('inf'))
dist[start] = 0
heap = [(0, start)]

while len(heap) > 0:
    d, curr = heapq.heappop(heap)
    if curr == end:
        break
    for j, w in graph[curr]:
        if dist[j] > d + w:
            dist[j] = d + w
            heapq.heappush(heap, (d + w, j))

print(dist[end] if dist[end] != float('inf') else -1)
