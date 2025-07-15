t = int(input())
for _ in range(t):
    b = input()
    n = len(b)
    dp = [0] * n
    for i in range(2, n):
        if b[i - 2] == b[i - 1] == b[i]:
            dp[i] = 0
        else:
            dp[i] = dp[i - 3] + 3
    print(n - max(dp))
