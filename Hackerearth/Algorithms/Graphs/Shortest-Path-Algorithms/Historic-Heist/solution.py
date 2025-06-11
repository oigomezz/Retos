test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    ifpol = list(map(int, input().split()))
    start, dest = map(int, input().split())
    start -= 1
    dest -= 1
    m, three = map(int, input().split())

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, t = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, t))
        adj[v].append((u, t))

    dist = [float('inf')] * n
    pdist = [float('inf')] * n
    s = set()

    dist[start] = 0
    for i in range(n):
        if ifpol[i]:
            pdist[i] = 0
            s.add((pdist[i], i))

    while s:
        x = min(s)
        s.remove(x)
        for it in adj[x[1]]:
            if pdist[it[0]] > pdist[x[1]] + it[1]:
                s.discard((pdist[it[0]], it[0]))
                pdist[it[0]] = pdist[x[1]] + it[1]
                s.add((pdist[it[0]], it[0]))

    s.clear()
    s.add((dist[start], start))

    while s:
        x = min(s)
        s.remove(x)
        for it in adj[x[1]]:
            if pdist[it[0]] > dist[x[1]] + it[1] and dist[it[0]] > dist[x[1]] + it[1]:
                s.discard((dist[it[0]], it[0]))
                dist[it[0]] = dist[x[1]] + it[1]
                s.add((dist[it[0]], it[0]))

    if dist[dest] == float('inf'):
        print("-1")
    else:
        print(dist[dest])
