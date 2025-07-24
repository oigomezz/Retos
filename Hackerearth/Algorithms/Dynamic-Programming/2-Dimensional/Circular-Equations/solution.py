MOD = 1000000007
dp = [[0] * 200 for _ in range(20)]
dp[0][0] = 1
for i in range(1, 20):
    for j in range(200):
        for ld in range(10):
            if j - ld >= 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - ld]) % MOD

q = int(input())
for _ in range(q):
    s = int(input())
    ans = 0
    pat = 1
    n = 1
    while pat <= s:
        if s % pat == 0 and n * 9 >= s // pat:
            ans = (ans + dp[n][s // pat]) % MOD
        pat = pat * 10 + 1
        n += 1
    print(ans)
