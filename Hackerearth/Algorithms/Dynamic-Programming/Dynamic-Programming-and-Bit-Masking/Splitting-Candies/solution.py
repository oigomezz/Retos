n = int(input())
k = int(input())
a = [0] * (n + 1)
for i in range(1, n + 1):
    a[i] = int(input())

frq = [0] * 5
pre = [0] * (n + 1)
dp = [1000000007] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    frq[a[i] - 1] += 1
    for j in range(5):
        if frq[j] % 2:
            pre[i] += (1 << (j + 1))

for i in range(1, n + 1):
    for j in range(max(1, i - k + 1), i + 1):
        x = pre[i] ^ pre[j - 1]
        if x & (x - 1):
            continue
        dp[i] = min(dp[i], dp[j - 1] + a[i] + a[j])

print(dp[n] % 1000000007)
