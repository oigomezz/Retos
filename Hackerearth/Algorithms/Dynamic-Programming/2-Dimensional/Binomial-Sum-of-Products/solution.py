MOD = 1000000007
dp = [[0] * 1001 for _ in range(1001)]
dp[0][0] = 1
for i in range(1, 1001):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD
for i in range(1, 1001):
    for j in range(i + 1, 1001):
        dp[i][j] = (i * j) % MOD
for i in range(1001):
    for j in range(1, 1001):
        dp[i][j] = (dp[i][j] * dp[i][j - 1]) % MOD
q = int(input())
for _ in range(q):
    a, b, c, d = list(map(int, input().strip().split()))
    ans = 0
    for i in range(a, b + 1):
        x = dp[i][d]
        if c > 0:
            x = (x * pow(dp[i][c - 1], MOD - 2, MOD)) % MOD
        ans = (ans + x) % MOD
    print(ans)
