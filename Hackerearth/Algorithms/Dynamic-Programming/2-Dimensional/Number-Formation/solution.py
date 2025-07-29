from itertools import accumulate

MOD = 720720
n = int(input())
a = list(map(int, input().strip().split()))
k = int(input())
if k == 1:
    print(n)
else:
    dp = [[0] * n for _ in range(k)]
    dp[0] = list(accumulate(int(i > 0) for i in a))
    for i in range(1, k):
        for j in range(i, n):
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
    print(dp[k - 1][-1] % MOD)
