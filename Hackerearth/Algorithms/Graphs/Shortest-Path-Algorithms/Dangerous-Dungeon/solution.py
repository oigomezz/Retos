from collections import defaultdict
import heapq

n, m, q = map(int, input().split())
o = list(map(int, input().split()))
g = defaultdict(list)
rg = defaultdict(list)
for _ in range(m):
    x, y,  z = map(int, input().split())
    g[x].append((y, z))
    rg[y].append((x, z))

dist = [float('inf')] * 1024
throttle = [0] * 1024
que = []

heapq.heappush(que, (0, n - 1))
dist[n - 1] = 0

while que:
    d, a = heapq.heappop(que)
    d = -d
    if d > dist[a]:
        continue
    dist[a] = d
    for p in rg[a]:
        d1 = d + p[1]
        a1 = p[0]
        if d1 < dist[a1]:
            dist[a1] = d1
            throttle[a1] = throttle[a] + 1
            heapq.heappush(que, (-d1, a1))

t = [defaultdict(int) for _ in range(1024)]
que = []

if o[0] != 0:
    heapq.heappush(que, (-dist[0], 0, 0))

while que:
    d0, d, a = heapq.heappop(que)
    d = -d
    r = d % q
    if r in t[a]:
        continue
    t[a][r] = d
    if a == n - 1:
        break
    for p in g[a]:
        d1 = d + p[1]
        r1 = d1 % q
        a1 = p[0]
        if r1 == o[a1]:
            continue
        if len(t[a1]) > throttle[a1]:
            continue
        heapq.heappush(que, (-(d1 + dist[a1]), -d1, a1))

print(-1 if not t[n - 1] else min(t[n - 1].values()))
