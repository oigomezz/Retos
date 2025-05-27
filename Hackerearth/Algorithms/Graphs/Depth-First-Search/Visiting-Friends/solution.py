from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)


def dfs(node):
    global size
    size += 1
    visited[node] = 1
    for child in adjacency_list[node]:
        if not visited[child]:
            dfs(child)


if __name__ == "__main__":
    t = int(input())
    dp = [0] * 201
    dp[1] = 0
    dp[2] = 1
    for i in range(3, 201):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2])

    for _ in range(t):
        n, m = map(int, input().split())
        size = 0
        visited = [0] * (n + 1)
        adjacency_list = defaultdict(list)

        for i in range(m):
            x, y = map(int, input().split())
            adjacency_list[x].append(y)
            adjacency_list[y].append(x)

        component_sizes = []
        for i in range(1, n + 1):
            if not visited[i]:
                size = 0
                dfs(i)
                component_sizes.append(size)

        print(len(component_sizes))
        component_sizes.sort(reverse=True)
        for component_size in component_sizes:
            print(dp[component_size], end=' ')
        print()
