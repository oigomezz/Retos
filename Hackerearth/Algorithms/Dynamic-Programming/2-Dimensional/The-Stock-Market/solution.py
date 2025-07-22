def solve(size, array, k):
    dp = [[-1000000001] * size for _ in range(k)]
    for i in range(size):
        if i:
            dp[0][i] = dp[0][i - 1] - array[i]
        else:
            dp[0][i] = -array[i]
    for i in range(1, k):
        for j in range(i, size):
            if i % 2:
                dp[i][j] = max(dp[i - 1][j - 1] + array[j],
                               dp[i][j - 1] + array[j])
            else:
                dp[i][j] = max(dp[i - 1][j - 1] - array[j],
                               dp[i][j - 1] - array[j])
    return dp[k - 1][size - 1]


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        K = int(input())

        out_ = solve(N, A, K)
        print(out_)
