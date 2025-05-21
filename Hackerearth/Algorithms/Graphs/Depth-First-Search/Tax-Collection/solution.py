from collections import defaultdict


def dfs(node, parent):
    dp[node] = pr[a[node]]
    for neighbor in adjacency_list[node]:
        if neighbor != parent:
            dfs(neighbor, node)
            dp[node] += dp[neighbor]


if __name__ == "__main__":
    test_cases = int(input())
    adjacency_list = defaultdict(list)
    dp = [0] * 100001
    a = [0] * 100001
    pr = [0] * 1000001

    for i in range(2, 1000001, 2):
        pr[i] += 1
    for i in range(3, 1000001, 3):
        pr[i] += 1
    for i in range(5, 1000001, 6):
        if pr[i] == 0:
            for j in range(i, 1000001, i):
                pr[j] += 1
        i_2 = i + 2
        if pr[i_2] == 0:
            for j in range(i_2, 1000001, i_2):
                pr[j] += 1

    for _ in range(test_cases):
        n = int(input())
        arr = list(map(int, input().split()))
        for i in range(1, n + 1):
            a[i] = arr[i - 1]
            adjacency_list[i].clear()
        for _ in range(1, n):
            u, v = map(int, input().split())
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        dfs(1, 0)
        print(' '.join(map(str, dp[1:n+1])))
