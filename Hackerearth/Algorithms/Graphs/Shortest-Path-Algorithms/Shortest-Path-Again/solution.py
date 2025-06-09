LIMIT = 1000000000

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append([w, u - 1, v - 1])

ans = [LIMIT] * n
ans[0] = 0

for i in range(1, n + 1):
    dp = [LIMIT] * n
    for x in edges:
        dp[x[2]] = min(dp[x[2]], ans[x[1]] + i * x[0])
        dp[x[1]] = min(dp[x[1]], ans[x[2]] + i * x[0])
    for k in range(n):
        ans[k] = min(ans[k], dp[k])

for i in range(n):
    if ans[i] == LIMIT:
        ans[i] = -1
    print(ans[i])
