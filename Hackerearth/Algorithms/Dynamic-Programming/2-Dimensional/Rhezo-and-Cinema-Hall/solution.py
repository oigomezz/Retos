MOD = 1000000007
n, m, k = map(int, input().split())
combinations = [[0] * 21 for _ in range(21)]
combinations[0][0] = 1

for i in range(1, 21):
    combinations[i][0] = 1
    for j in range(1, i + 1):
        combinations[i][j] = (
            combinations[i - 1][j] + combinations[i - 1][j - 1]) % MOD

dp = [[0] * 5001 for _ in range(501)]
dp[0][0] = 1
max_value = n * m

for i in range(1, n + 1):
    for j in range(2, max_value + 1):
        for num_picks in range(2, min(m, j) + 1):
            if m - num_picks + 1 >= 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - num_picks] *
                            combinations[m - num_picks + 1][num_picks]) % MOD

result = 0
for i in range(max(2, k), max_value + 1):
    result = (result + dp[n][i]) % MOD
print(result)
