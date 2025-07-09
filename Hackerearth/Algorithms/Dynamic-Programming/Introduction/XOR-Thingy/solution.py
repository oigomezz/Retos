MOD = 1000000007
n, m = map(int, input().split())
dp = [0] * 519
tdp = [0] * 519
dp[0] = 1
arr = list(map(int, input().split()))

for a in arr:
    tdp = [0] * 519
    for i in range(a + 1):
        for j in range(512):
            tdp[i ^ j] += dp[j]
            if tdp[i ^ j] >= MOD:
                tdp[i ^ j] -= MOD
    dp = tdp.copy()

print(" ".join(map(str, dp[:m + 1])))
