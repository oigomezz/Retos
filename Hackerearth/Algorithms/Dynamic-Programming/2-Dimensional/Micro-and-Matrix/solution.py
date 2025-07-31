t = int(input())
for _ in range(t):
    answer = 0
    n = int(input())
    array = [[0] * n for _ in range(n)]
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        arr = list(map(int, input().split()))
        for j in range(n):
            array[i][j] = arr[j]

    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                if (array[i][j] == array[i - 1][j] and
                    array[i][j] == array[i - 1][j - 1] and
                        array[i][j] == array[i][j - 1]):
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1]
                                   [j], dp[i][j - 1]) + 1
                else:
                    dp[i][j] = 1
            answer = max(answer, dp[i][j])

    print(answer)
