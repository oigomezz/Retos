n, k = map(int, input().split())
heights = list(map(int, input().split()))
min_dp = [[1000000000] * (n + 1) for _ in range(n)]
for h in range(n + 1):
    min_dp[n - 1][h] = 0

for a in range(n - 2, -1, -1):
    for b in range(a + 1, min(n - 1, a + k) + 1):
        height_difference = abs(heights[a] - heights[b])
        dp_value = min_dp[b][height_difference] + 1
        min_dp[a][height_difference] = min(
            min_dp[a][height_difference], dp_value)

    for h in range(1, n + 1):
        min_dp[a][h] = min(min_dp[a][h], min_dp[a][h - 1])

if min_dp[0][n] >= 1000000000:
    print("-1")
else:
    print(min_dp[0][n])
