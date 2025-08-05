MOD = 1000000007
dp = [[0.0] * 10005 for _ in range(60)]


test_cases = int(input())
for _ in range(test_cases):
    M, N, K = map(int, input().split())
    for i in range(1, N + 1):
        dp[1][i] = 1.0 / N

    for m in range(2, M + 1):
        for k in range(1, K + 1):
            for n in range(1, N + 1):
                if k - n < 0:
                    break
                dp[m][k] += dp[m - 1][k - n]
            dp[m][k] /= N

    y = 0
    if dp[M][K] == 0:
        print("0.000 0")
        continue

    while dp[M][K] < 1:
        dp[M][K] *= 10
        y += 1

    print(f"{dp[M][K]:.3f} {y}")
