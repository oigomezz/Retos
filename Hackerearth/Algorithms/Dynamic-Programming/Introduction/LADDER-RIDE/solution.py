MOD = 1000000007
t, n = map(int, input().split())
dp = [0, 0, 1, 0, 1, 1, 1] + [0] * (n - 6)
for i in range(7, n + 1):
    dp[i] = (dp[i - 2] + dp[i - 5]) % MOD
for _ in range(t):
    cur, k = map(int, input().strip().split())
    if cur < k or k == 5:
        print(dp[cur])
    else:
        dp1 = dp.copy()
        dp1[k] += 1
        for i in range(k + 1, cur + 1):
            dp1[i] = (dp1[i - 2] + dp1[i - 5] + dp1[i - k]) % MOD
        print(dp1[cur])
