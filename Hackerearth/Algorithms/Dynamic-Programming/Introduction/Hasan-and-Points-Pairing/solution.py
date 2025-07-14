import math


n = int(input())
x = [0] * (n * 2)
y = [0] * (n * 2)
d = [[0.0] * (n * 2) for _ in range(n * 2)]
dp = [float('inf')] * (1 << (n * 2))
dp[0] = 0

for i in range(n * 2):
    x[i], y[i] = map(int, input().split())

for i in range(n * 2):
    for j in range(n * 2):
        d[i][j] = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)

N = n * 2
for i in range(1 << N):
    if dp[i] > 1e8:
        continue
    for q in range(N):
        if not (i & (1 << q)):
            for j in range(q + 1, N):
                if i & (1 << j):
                    continue
                nmask = (i | (1 << j) | (1 << q))
                dp[nmask] = min(dp[nmask], dp[i] + d[j][q])
            break

print(f"{dp[(1 << N) - 1]:.6f}")
