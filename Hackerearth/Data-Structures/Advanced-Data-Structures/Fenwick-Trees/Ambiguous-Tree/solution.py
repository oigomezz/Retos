import sys
from collections import defaultdict

sys.setrecursionlimit(200000)

n = 0
p1 = 0
p2 = 0
q = 0
depth = [0] * 100005
pa = [[0] * 20 for _ in range(100005)]
size = [0] * 100005
sum_ = [[0] * 20 for _ in range(100005)]
adj = defaultdict(list)

def dfs(v, p, d):
    depth[v] = d
    pa[v][0] = p
    for x in range(20):
        if pa[v][x] == 0:
            break
        pa[v][x + 1] = pa[pa[v][x]][x]
    size[v] = 1
    for x in adj[v]:
        if x == p:
            continue
        size[v] += dfs(x, v, d + 1)
    return size[v]

def dfs2(v, p):
    if v > 1:
        sum_[v][0] = (size[pa[v][0]] - size[v]) * (size[pa[v][0]] - size[v] - 1) // 2
    for x in range(1, 20):
        if pa[v][x - 1] == 0:
            break
        sum_[v][x] = sum_[v][x - 1] + sum_[pa[v][x - 1]][x - 1]
    for x in adj[v]:
        if x == p:
            continue
        dfs2(x, v)

def lca(a, b):
    if a == b:
        return n * (n - 1) // 2
    ans = 0
    if depth[a] > depth[b]:
        a, b = b, a
    sa, sb = a, b
    if depth[a] < depth[b]:
        for x in range(17):
            if (1 << x) & (depth[b] - depth[a] - 1):
                ans += sum_[b][x]
                b = pa[b][x]
        if a == pa[b][0]:
            return ans + (size[sb] * (size[sb] - 1) // 2) + ((n - size[b]) * (n - size[b] - 1) // 2)
        ans += sum_[b][0]
        b = pa[b][0]
    for x in range(16, -1, -1):
        if pa[a][x] != pa[b][x]:
            ans += sum_[a][x] + sum_[b][x]
            a = pa[a][x]
            b = pa[b][x]
    k = n - size[a] - size[b]
    return ans + k * (k - 1) // 2 + (size[sa] * (size[sa] - 1) // 2) + (size[sb] * (size[sb] - 1) // 2)

if __name__ == "__main__":
    n = int(input())
    for _ in range(n - 1):
        p1, p2 = map(int, input().split())
        adj[p1].append(p2)
        adj[p2].append(p1)
    dfs(1, 0, 0)
    dfs2(1, 0)
    q = int(input())
    for _ in range(q):
        p1, p2 = map(int, input().split())
        print(n * (n - 1) // 2 - lca(p1, p2))

