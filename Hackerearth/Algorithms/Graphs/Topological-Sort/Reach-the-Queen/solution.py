def dfs(v, adj, dp):
    if dp[v]:
        return dp[v]
    for u in adj[v]:
        dp[v] = (dp[v] + dfs(u, adj, dp)) % 1000000007
    return dp[v]


if __name__ == "__main__":
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    dp = [0] * (n + 1)

    for _ in range(m):
        u, v = map(int, input().split())
        adj[v].append(u)

    dp[1] = 1
    dfs(n, adj, dp)
    print(dp[n])
