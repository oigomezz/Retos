from collections import defaultdict


def dfs(vertex):
    if visited[vertex]:
        return
    visited[vertex] = True
    for neighbor in graph[vertex]:
        dfs(neighbor)
    order.append(vertex)


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = defaultdict(list)
    order = []
    visited = [False] * n
    dp = [0] * n

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)

    for i in range(n):
        dfs(i)

    for vertex in order:
        dp[vertex] = 1
        for neighbor in graph[vertex]:
            dp[vertex] = max(dp[vertex], dp[neighbor] + 1)

    print(max(dp))
