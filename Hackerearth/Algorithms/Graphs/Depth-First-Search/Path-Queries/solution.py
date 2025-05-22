import sys
from collections import defaultdict
import bisect

sys.setrecursionlimit(10**6)
N = 400100
LN = 17


class Node:
    def __init__(self, count, left, right):
        self.count = count
        self.left = left
        self.right = right


null = Node(0, None, None)
nodes = [None] * N


def insert(old, l, r, val):
    if l > val or r < val:
        return old

    if l == r:
        return Node(1, null, null)

    mid = (l + r) // 2
    return Node(old.count + 1, insert(old.left, l, mid, val), insert(old.right, mid + 1, r, val))


def query(a, b, c, d, l, r, k):
    if l == r:
        return l

    mid = (l + r) // 2
    cn = a.left.count + b.left.count - c.left.count - d.left.count
    if cn < k:
        return query(a.right, b.right, c.right, d.right, mid + 1, r, k - cn)
    else:
        return query(a.left, b.left, c.left, d.left, l, mid, k)


g = defaultdict(list)
go = []
a = [0] * N
n, q = 0, 0

depth = [0] * N
par = [[-1] * LN for _ in range(N)]

cmp = {}


def dfs(v):
    global nodes
    if par[v][0] == -1:
        depth[v] = 0
        nodes[v] = insert(null, 1, n, a[v])
    else:
        depth[v] = depth[par[v][0]] + 1
        nodes[v] = insert(nodes[par[v][0]], 1, n, a[v])

    for x in g[v]:
        if x != par[v][0]:
            par[x][0] = v
            dfs(x)


def lca(u, v):
    if depth[u] > depth[v]:
        u, v = v, u

    diff = depth[v] - depth[u]

    for i in range(LN):
        if diff & (1 << i):
            v = par[v][i]

    if u == v:
        return u

    for i in range(LN - 1, -1, -1):
        if par[u][i] != par[v][i]:
            u = par[u][i]
            v = par[v][i]

    return par[u][0]


def get(u, v, k):
    lc = lca(u, v)
    return go[query(nodes[u], nodes[v], nodes[lc], nodes[par[lc][0]] if par[lc][0] != -1 else null, 1, n, k) - 1]


def solve():
    global n, q, go
    null.left = null.right = null

    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        a[i] = arr[i - 1]

    for i in range(1, n + 1):
        go.append(a[i])

    go.sort()

    for i in range(1, n + 1):
        a[i] = bisect.bisect_left(go, a[i]) + 1

    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    dfs(1)

    for i in range(LN - 1):
        for j in range(1, n + 1):
            if par[j][i] != -1:
                par[j][i + 1] = par[par[j][i]][i]

    for _ in range(q):
        u, v = map(int, input().split())

        lc = lca(u, v)
        tot = depth[u] + depth[v] - 2 * depth[lc] + 1

        print(get(u, v, 1) + get(u, v, tot) +
              get(u, v, (tot + 1) // 2), end=' ')


if __name__ == "__main__":
    solve()
