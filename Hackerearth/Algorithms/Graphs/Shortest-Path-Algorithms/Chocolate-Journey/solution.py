from heapq import heappop, heappush

INF = float('inf')


def dijkstra(start, adj, size):
    dist = [INF] * (n + 1)
    visited = [False] * (size + 1)
    heap = [(0, start)]
    dist[start] = 0
    while heap:
        _, node = heappop(heap)
        if not visited[node]:
            visited[node] = True
            for next_length, next_node in adj[node]:
                new_length = next_length + dist[node]
                if dist[next_node] > new_length:
                    dist[next_node] = new_length
                    heappush(heap, (dist[next_node], next_node))
    return dist


n, m, k, x = map(int, input().strip().split())
cities = list(map(int, input().strip().split()))
roads = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v, d = map(int, input().split())
    roads[u].append((d, v))
    roads[v].append((d, u))
a, b = map(int, input().strip().split())
dist_a = dijkstra(a, roads, n)
dist_b = dijkstra(b, roads, n)
time = INF
for city in cities:
    if dist_b[city] <= x:
        time = min(time, dist_a[city] + dist_b[city])
print(time if time != INF else -1)
