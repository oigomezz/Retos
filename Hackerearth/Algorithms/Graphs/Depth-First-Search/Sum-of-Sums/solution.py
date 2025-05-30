import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

n = 0
a = [0] * 1000006
g = [0] * 1000006
f = [0] * 1000006
cost = [0] * 1000006
totalsum = 0
mn = float('inf')
ansnode = 0
v = defaultdict(list)


def dfs(node, par):
    global g
    for neighbor in v[node]:
        if par == neighbor:
            continue
        dfs(neighbor, node)
        g[node] += g[neighbor]
    g[node] += a[node]


def dfs1(node, par):
    global cost
    for neighbor in v[node]:
        if par == neighbor:
            continue
        dfs1(neighbor, node)
        f[node] += f[neighbor]
    f[node] += g[node]
    cost[1] += f[node]


def dfs2(node, par, newf, cost):
    global mn, ansnode
    tempans = cost + newf + totalsum - 2 * f[node] - 3 * g[node]
    revert = f[node]
    f[node] = f[par] + totalsum - 2 * g[node]
    if tempans < mn:
        ansnode = node
        mn = tempans
    elif tempans == mn and ansnode > node:
        ansnode = node
    for neighbor in v[node]:
        if par == neighbor:
            continue
        dfs2(neighbor, node, f[par] + totalsum - 2 * g[node], tempans)
    f[node] = revert


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        a[i] = arr[i - 1]
        totalsum += a[i]
    for _ in range(1, n):
        x, y = map(int, input().split())
        v[x].append(y)
        v[y].append(x)
    dfs(1, -1)
    dfs1(1, -1)
    mn = cost[1]
    ansnode = 1
    for neighbor in v[1]:
        dfs2(neighbor, 1, f[1], mn)
    print(ansnode, mn)
