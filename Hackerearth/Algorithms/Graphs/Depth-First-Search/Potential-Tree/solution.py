from collections import defaultdict
import sys


def dfs(graph, i, prev, subval, leaves):
    if len(graph[i]) == 1 and min(graph[i]) == prev:
        leaves.add(i)
        subval[i] = i % 2
        return i % 2
    res = 0
    for j in graph[i]:
        if j != prev:
            res += dfs(graph, j, i, subval, leaves)
    subval[i] = res
    if res > 0:
        return 1
    return 0


sys.setrecursionlimit(10 ** 6)
t = int(input())
for _ in range(t):
    n = int(input())
    graph = defaultdict(set)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
    subval = [0] * n
    allval = [0] * n
    leaves = set()
    dfs(graph, 0, -1, subval, leaves)
    allval[0] = subval[0]
    stack = [(0, -1)]
    while len(stack) > 0:
        i, prev = stack.pop()
        for j in graph[i]:
            if j != prev:
                pchild = allval[i] - (1 if subval[j] > 0 else 0)
                if j not in leaves:
                    allval[j] = subval[j] + (1 if pchild > 0 else 0)
                else:
                    allval[j] = 1 if pchild > 0 else 0
                stack.append((j, i))
    print(*allval)
