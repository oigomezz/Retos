from collections import defaultdict
import sys


def mincams(graph, i, prev, prevdone, cache):
    key = (i, prev, prevdone)
    if key in cache:
        return cache[key]
    a = 1
    b = 0
    for j in graph[i]:
        if j != prev:
            a += mincams(graph, j, i, True, cache)
            b += mincams(graph, j, i, False, cache)
        elif not prevdone:
            b = float('inf')
    res = min(a, b)
    cache[key] = res
    return res


sys.setrecursionlimit(2 * 10 ** 5)
n = int(input())
graph = defaultdict(set)
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].add(v)
    graph[v].add(u)

print(mincams(graph, 0, -1, True, {}))
