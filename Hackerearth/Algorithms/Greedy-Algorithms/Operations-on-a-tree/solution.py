def dfs(u, p):
    global ans
    bsum[u] = b[u]
    for v in g[u]:
        if v != p:
            dfs(v, u)
            bsum[u] += bsum[v]
    ans = max(ans, max(bsum[u], B - bsum[u]))


t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    global A, B, ans
    A = 0
    B = 0
    g = [[] for _ in range(n)]
    a = [0] * n
    b = [0] * n
    bsum = [0] * n

    arr = list(map(int, input().split()))
    for i in range(n):
        a[i] = arr[i]
        b[i] = (a[i] ^ k) - a[i]
        A += a[i]
        B += b[i]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        u = u - 1
        v = v - 1
        g[u].append(v)
        g[v].append(u)

    ans = max(0, B)
    dfs(0, -1)
    print(A + ans)
