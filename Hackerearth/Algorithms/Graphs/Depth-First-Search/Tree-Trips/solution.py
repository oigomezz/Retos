def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
edge = []
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge.append((a, b))
    graph[a].append(b)
    graph[b].append(a)

trips = []
for _ in range(m):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    trips.append((p, q))

ans = float("inf")
for b in range(2**len(edge)):
    temp = []
    f = True
    for i in range(len(edge)):
        if b & (1 << i):
            temp.append(edge[i])

    parent = [i for i in range(n)]
    for a, b in temp:
        pa, pb = find(a), find(b)
        parent[pa] = pb
    for a, b in trips:
        if find(a) == find(b):
            f = False
            break
    if f:
        ans = min(ans, n-len(temp)-1)

print(ans)
