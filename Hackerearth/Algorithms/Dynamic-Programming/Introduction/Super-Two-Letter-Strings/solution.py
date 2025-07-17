MOD = 1000000007
t = int(input())
n_list = []
p_list = []
for _ in range(t):
    n, p = map(int, input().strip().split())
    n_list.append(n)
    p_list.append(p)
max_n = max(n_list)
max_p = max(p_list)
dp = [[1] * (max_n + 1) for _ in range(max_p + 1)]
for i in range(2, max_p + 1):
    for j in range(2, max_n + 1):
        if i > j:
            dp[i][j] = dp[i - 1][j]
        elif i == j:
            dp[i][j] = (dp[i - 1][j] + 1) % MOD
        else:
            dp[i][j] = (2 * dp[i][j - 1] - dp[i][j - i - 1]) % MOD
for n, p in zip(n_list, p_list):
    print(dp[p][n])
