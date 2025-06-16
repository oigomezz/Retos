def dfs(v, node, vis, w, profit):
    if vis[node]:
        return
    vis[node] = True
    for i in v[node]:
        dfs(v, i, vis, w, profit)
        profit[node] = max(profit[node], profit[i] + w[i] - w[node])


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        v = [[] for _ in range(n + 1)]
        w = [-1] * (n + 1)
        profit = [0] * (n + 1)
        vis = [False] * (n + 1)

        arr = list(map(int, input().split()))
        for i in range(1, n + 1):
            w[i] = arr[i-1]

        for _ in range(m):
            x, y = map(int, input().split())
            v[x].append(y)

        total = 0
        for i in range(1, n + 1):
            dfs(v, i, vis, w, profit)
            total = max(profit[i], total)

        print(total)
