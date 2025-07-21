n, m = map(int, input().split())
a = []
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(m):
        x = arr[j]
        a.append((x, i, j))

a.sort(reverse=True, key=lambda x: x[0])
k = len(a)
dp = [0] * k
dp1 = [0] * n
dp2 = [0] * m

dp[0] = 1
dp1[a[0][1]] = 1
dp2[a[0][2]] = 1

for i in range(1, k):
    dp[i] = 1 + max(dp1[a[i][1]], dp2[a[i][2]])
    dp1[a[i][1]] = dp[i]
    dp2[a[i][2]] = dp[i]

print(max(dp))
