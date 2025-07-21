t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [[0] * (k + 1) for _ in range(n)]
    if a[0] <= k:
        dp[0][a[0]] = 1
    if b[0] <= k:
        dp[0][b[0]] = 1

    for i in range(1, n):
        for j in range(1, k + 1):
            l = dp[i - 1][j - a[i]] if a[i] <= j else 0
            r = dp[i - 1][j - b[i]] if b[i] <= j else 0
            dp[i][j] = l or r

    print("YES" if dp[n - 1][k] else "NO")
