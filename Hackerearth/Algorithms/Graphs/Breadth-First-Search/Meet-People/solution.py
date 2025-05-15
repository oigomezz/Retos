from collections import deque

test_cases = int(input())
for _ in range(test_cases):
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]

    for i in range(1, n):
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)

    d = [-1] * (n + 1)

    def bfs(z):
        q = deque([z])
        d[z] = 0
        while q:
            x = q.popleft()
            for y in g[x]:
                if d[y] < 0:
                    d[y] = d[x] + 1
                    q.append(y)

    a = list(map(int, input().split()))
    bfs(a[0])

    ok = True
    for x in a:
        if d[x] % 2 != d[a[0]] % 2:
            ok = False
            break

    if ok:
        u = 0
        v = -1
        for x in a:
            if d[x] > v:
                u = x
                v = d[x]
        d = [-1] * (n + 1)
        bfs(u)
        v = -1
        for x in a:
            v = max(v, d[x])
        print(v // 2)
    else:
        print(-1)
