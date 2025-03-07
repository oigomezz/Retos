MOD = 1000000007

n, k = map(int, input().split())
dp = [0] * 10017
dp[0] = 1

for i in range(1, n):
    for j in range(max(0, i - k), i):
        dp[i] = (dp[i] + dp[j]) % MOD

print(dp[n - 1])
