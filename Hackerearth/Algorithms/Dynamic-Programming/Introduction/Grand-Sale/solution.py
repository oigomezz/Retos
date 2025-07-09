n = int(input().strip())
dp = [0] * 100002

for _ in range(n):
    a, b, c, d = map(int, input().strip().split())
    a = a * 60 + b
    c = c * 60 + d + 5
    dp[a] += 1
    dp[c] -= 1

ans = 0
for i in range(1, 100001):
    dp[i] += dp[i - 1]
    ans = max(dp[i], ans)

print(ans)
