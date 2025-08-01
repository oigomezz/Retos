t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0] + [float('inf')] * n
    for _ in range(n):
        v, p = map(int, input().strip().split())
        v += 1
        if v >= n:
            dp[n] = min(dp[n], dp[0] + p)
        for i in range(n, v - 1, -1):
            dp[i] = min(dp[i], dp[i - v] + p)
        for i in range(n - 1, -1, -1):
            dp[i] = min(dp[i], dp[i + 1])
    print(dp[n])
