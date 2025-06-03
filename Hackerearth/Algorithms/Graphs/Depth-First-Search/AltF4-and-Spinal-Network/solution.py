t = int(input())
for _ in range(t):
    n = int(input())
    f = 1
    visit = [False] * n
    deg = [0] * n
    edg = [0] * n

    for i in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        deg[u] += 1
        deg[v] += 1
        edg[u] = v
        edg[v] = u

    for i in range(n):
        if deg[i] == 1:
            visit[i] = True

    for i in range(n):
        if visit[i]:
            deg[edg[i]] -= 1
            deg[i] = -1

    for i in range(n):
        if deg[i] > 2:
            f = 0
            break

    print("YES" if f else "NO")
