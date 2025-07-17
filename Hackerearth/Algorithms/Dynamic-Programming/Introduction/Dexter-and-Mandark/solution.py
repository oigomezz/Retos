t = int(input())
cache = {}
MOD = 1000000007
for _ in range(t):
    n, m = map(int, input().strip().split())
    key = (n, m)
    if key in cache:
        print(cache[key])
    else:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(i + 1):
                k = i - j
                if j >= m * k:
                    if i != n or j != k:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i - 1][j - 1]
                    dp[i][j] %= MOD
        res = sum(dp[n]) % MOD
        cache[key] = res
        print(res)
