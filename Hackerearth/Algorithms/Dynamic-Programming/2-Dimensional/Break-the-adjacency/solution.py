t = int(input())
for _ in range(t):
    n = int(input())
    elements = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    dp = [[float('inf')] * 3 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = prices[0]
    dp[0][2] = 2 * prices[0]

    for i in range(1, n):
        for j in range(3):
            for k in range(3):
                current_length = elements[i] + j
                previous_length = elements[i - 1] + k
                if current_length != previous_length:
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + j * prices[i])

    answer = min(dp[n - 1])
    print(answer)
