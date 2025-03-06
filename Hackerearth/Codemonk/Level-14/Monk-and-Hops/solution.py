from heapq import heappush, heappop


def decide(a, b):
    if a[0] and b[0]:
        return 0
    if a[1] and b[1]:
        return 0
    return 1


inf = int(1e18)
n, m = list(map(int, input().split()))
graph = []
for i in range(n+1):
    graph.append([])

for i in range(m):
    u, v, w = list(map(int, input().split()))
    graph[u].append((v, w))
    graph[v].append((u, w))

cost = [inf]*(n+1)
cost[1] = 0
hops = [inf]*(n+1)
hops[1] = 0
h = []
for nb, w in graph[1]:
    par = [0, 0]
    par[w % 2] = 1
    heappush(h, (w, nb, par))
    cost[nb] = w
    hops[nb] = 0

while h:
    C, node, par = heappop(h)
    for nb, w in graph[node]:
        npar = [0, 0]
        npar[w % 2] = 1
        if C+w < cost[nb]:
            cost[nb] = C + w
            hops[nb] = hops[node] + decide(par, npar)
            heappush(h, (cost[nb], nb, npar))
        elif C+w == cost[nb]:
            val = hops[node] + decide(par, npar)
            if val < hops[nb]:
                hops[nb] = val
            heappush(h, (cost[nb], nb, npar))

print(cost[-1], hops[-1])
