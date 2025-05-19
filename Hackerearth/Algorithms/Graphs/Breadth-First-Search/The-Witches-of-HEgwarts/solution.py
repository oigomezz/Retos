def fn(x, dp):
    if x <= 1:
        return 0
    if x in dp:
        return dp[x]
    opt1 = 1 + (x % 2) + fn(x // 2, dp)
    opt2 = 1 + (x % 3) + fn(x // 3, dp)
    dp[x] = min(opt1, opt2)
    return dp[x]


t = int(input())
for _ in range(t):
    n = int(input())
    print(fn(n, {}))
