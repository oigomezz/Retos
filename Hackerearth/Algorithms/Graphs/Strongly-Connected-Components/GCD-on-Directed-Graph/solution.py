from collections import defaultdict
from math import gcd

finished = []
visited = [False] * 100005
comp = defaultdict(set)
gcds = defaultdict(set)
adj = defaultdict(list)
rev = defaultdict(list)
Cost = [0] * 100005
id = 0
ID = [0] * 100005
Value = [0] * 100005


def dfs1(u):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs1(v)
    finished.append(u)


def dfs2(u):
    global id
    gcdValue = Cost[u]
    ID[u] = id
    visited[u] = True
    for v in rev[u]:
        if not visited[v]:
            gcdValue = gcd(gcdValue, dfs2(v))
    return gcdValue


def dfs3(u):
    visited[u] = True
    gcds[u].add(Value[u])
    for v in comp[u]:
        if not visited[v]:
            dfs3(v)
        for x in gcds[v]:
            gcds[u].add(gcd(Value[u], x))


if __name__ == "__main__":
    n, m = map(int, input().split())
    Cost = list(map(int, input().split()))
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        rev[v].append(u)

    for i in range(n):
        visited[i] = False
    for i in range(n):
        if not visited[i]:
            dfs1(i)

    for i in range(n):
        visited[i] = False
    while finished:
        u = finished.pop()
        minGCD = Cost[u]
        if not visited[u]:
            Value[id] = min(minGCD, dfs2(u))
            id += 1

    for i in range(n):
        for v in adj[i]:
            idI = ID[i]
            idV = ID[v]
            if idI != idV:
                comp[idI].add(idV)

    for i in range(id):
        visited[i] = False
    for i in range(id):
        if not visited[i]:
            dfs3(i)

    minGCD = Value[0]
    for i in range(id):
        if gcds[i]:
            minGCD = min(minGCD, min(gcds[i]))

    print(minGCD)
