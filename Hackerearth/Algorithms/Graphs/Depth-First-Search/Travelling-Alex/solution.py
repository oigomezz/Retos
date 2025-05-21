from collections import defaultdict


def dfs(graph, i, v, d):
    global res
    res = max(res, d)
    for j in graph[i]:
        if j not in v:
            v.add(j)
            dfs(graph, j, v, d + 1)


t = int(input())
for _ in range(t):
    n = int(input())
    graph = defaultdict(set)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
    res = 0
    dfs(graph, 1, {1}, 0)
    print(2 * (n - 1) - res)
