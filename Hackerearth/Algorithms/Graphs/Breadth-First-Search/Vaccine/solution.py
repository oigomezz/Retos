import heapq

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append((v, max(u, v)))
    adj[v].append((u, max(u, v)))

prime = [0] * (n + 1)
dis = [10000000] * (n + 1)
for i in range(2, int(n**0.5) + 1):
    if prime[i] == 0:
        for j in range(i * i, n + 1, i):
            prime[j] = 1

pq = []
for i in range(2, n + 1):
    if prime[i] == 0:
        heapq.heappush(pq, (0, i))
        dis[i] = 0

while pq:
    cost, p = heapq.heappop(pq)
    for neighbor in adj[p]:
        if cost + neighbor[1] < dis[neighbor[0]]:
            dis[neighbor[0]] = cost + neighbor[1]
            heapq.heappush(pq, (dis[neighbor[0]], neighbor[0]))

result = []
for i in range(1, n + 1):
    if dis[i] == 10000000:
        result.append("-1")
    else:
        result.append(str(dis[i]))

print(" ".join(result))
