n, k = map(int, input().split())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[n - 1] = min(v[n - 1], c[n - 1])
for i in range(n - 2, -1, -1):
    mi = dp[i + 1] + v[i]
    x = c[i]
    for j in range(i + 1, min(i + k + 1, n + 1)):
        mi = min(mi, x + dp[j])
    dp[i] = mi

print(dp[0])
