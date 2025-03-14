from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

g = defaultdict(list)
par = [[0] * 1000005 for _ in range(20)]
sum = [[0] * 1000005 for _ in range(20)]


def dfs(u, p=-1):
    for i in range(1, 20):
        sum[i][u] = sum[i - 1][u] + sum[i - 1][par[i - 1][u]]
        par[i][u] = par[i - 1][par[i - 1][u]]
    for v in g[u]:
        if p == v:
            continue
        par[0][v] = u
        dfs(v, u)


def query(u, x):
    for i in range(19, -1, -1):
        if sum[i][u] < x:
            x -= sum[i][u]
            u = par[i][u]
    return u


if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        n = int(input())
        for i in range(1, n + 1):
            g[i].clear()
        for _ in range(1, n):
            u, v = map(int, input().split())
            g[u].append(v)
            g[v].append(u)
        arr = [int(x) for x in input().split()]
        for i in range(1, n + 1):
            sum[0][i] = arr[i-1]
        par[0][1] = 1
        dfs(1)
        q = int(input())
        for _ in range(q):
            u, x = map(int, input().split())
            print(query(u, x))
