from collections import deque


def findset(a, parent):
    if parent[a] == a:
        return a
    parent[a] = findset(parent[a], parent)
    return parent[a]


def unionset(a, b, parent):
    if a < b:
        parent[a] = b
    else:
        parent[b] = a


t = int(input())
for I in range(1, t + 1):
    n, p, m = map(int, input().split())
    parent = list(range(n + 1))
    edge = []
    ans = []

    for _ in range(p):
        a, b, c = map(int, input().split())
        edge.append((c, (a, b)))

    edge.sort()

    for e in edge:
        a, b = e[1]
        if findset(a, parent) != findset(b, parent):
            unionset(findset(a, parent), findset(b, parent), parent)
            ans.append(e)

    v = [[] for _ in range(n + 1)]
    for e in ans:
        v[e[1][0]].append((e[1][1], e[0]))
        v[e[1][1]].append((e[1][0], e[0]))

    ar = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        q = deque()
        depth = [0] * (n + 1)
        visited = [False] * (n + 1)
        visited[i] = True
        q.append(i)

        while q:
            f = q.popleft()
            for it in v[f]:
                if visited[it[0]]:
                    continue
                visited[it[0]] = True
                q.append(it[0])
                depth[it[0]] = depth[f] + it[1]

        for j in range(1, n + 1):
            ar[i][j] = depth[j]

    print(f"Case: {I}")
    for _ in range(m):
        a, b = map(int, input().split())
        print(ar[a][b])
