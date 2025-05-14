from collections import deque


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dist = [1000000000] * n
    val = 0
    inB = [0] * n

    for e in b:
        val += dist[e]
        inB[e] = 1

    sum_val = val
    que = deque()
    ans = 0

    for i in range(x):
        que.append((a[i], 0))
        while que:
            u, d = que.popleft()
            if inB[u]:
                sum_val -= dist[u] - d
            dist[u] = d
            for v in graph[u]:
                if dist[v] <= d + 1:
                    continue
                que.append((v, d + 1))

        if sum_val < val:
            val = sum_val
            ans = i

    print(ans)
