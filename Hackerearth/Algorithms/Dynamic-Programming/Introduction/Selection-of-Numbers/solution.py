def solve(limit, array):
    dp = [0] * (limit + 1)
    dp[0] = sum(array[-limit:])
    for i in range(1, limit + 1):
        dp[i] = dp[i - 1] - array[-limit + i - 1] + array[i - 1]
    return max(dp)


k, n = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

out_ = solve(k, arr)
print(out_)
