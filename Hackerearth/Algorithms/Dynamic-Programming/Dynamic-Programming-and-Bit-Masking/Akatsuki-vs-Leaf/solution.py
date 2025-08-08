n = int(input().strip())
dp = [float('inf')] * (1 << n)
a1 = [tuple(map(int, input().strip().split()))
      for _ in range(n)]
a2 = [tuple(map(int, input().strip().split()))
      for _ in range(n)]

dp[0] = 0
for mask in range(1, 1 << n):
    x = bin(mask).count('1')
    for j in range(n):
        if (mask & (1 << j)) == 0:
            continue
        dp[mask] = min(dp[mask], dp[mask ^ (
            1 << j)] + abs(a1[x - 1][0] - a2[j][0]) + abs(a1[x - 1][1] - a2[j][1]))

print(str(dp[(1 << n) - 1]))
