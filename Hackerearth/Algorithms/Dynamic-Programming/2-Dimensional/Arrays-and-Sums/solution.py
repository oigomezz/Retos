MOD = 1000000007
MAXN = 10014

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * MAXN
    dp[0] = 1

    for i in range(n):
        for j in range(MAXN - 1, a[i] - 1, -1):
            dp[j] = (dp[j] + dp[j - a[i]]) % MOD

    tmp = dp[:]
    result = []
    for i in range(n):
        dp = tmp[:]
        for x in range(a[i], MAXN):
            dp[x] = (dp[x] + (MOD - dp[x - a[i]])) % MOD
        result.append(1 if a[i] == 0 or dp[a[i]] > 0 else 0)

    print(' '.join(map(str, result)))
