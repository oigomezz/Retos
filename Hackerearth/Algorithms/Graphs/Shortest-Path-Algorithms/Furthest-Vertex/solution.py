from collections import defaultdict

vis = [False] * 100002
diam = [(0, 0)] * 100002
g = defaultdict(list)
n, q = 0, 0
parent = [0] * 100002
diamL = [0] * 100002
T = [0] * 100002
P = [[-1] * 18 for _ in range(100002)]
L = [0] * 100002


class Query:
    def __init__(self, t, a, b=None):
        self.t = t
        self.a = a
        self.b = b


Q = [None] * 300006


def dfs(x, level):
    vis[x] = True
    for child in g[x]:
        if not vis[child]:
            T[child] = x
            L[child] = level + 1
            dfs(child, level + 1)


def ch_root(root):
    T[root] = root
    L[root] = 1
    dfs(root, 1)


def query(p, q):
    if L[p] < L[q]:
        p, q = q, p
    log = 0
    while (1 << log) <= L[p]:
        log += 1
    log -= 1
    for i in range(log, -1, -1):
        if L[p] - (1 << i) >= L[q]:
            p = P[p][i]
    if p == q:
        return p
    for i in range(log, -1, -1):
        if P[p][i] != -1 and P[p][i] != P[q][i]:
            p = P[p][i]
            q = P[q][i]
    return T[p]


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def furthest(x):
    a, b = diam[find(x)]
    l1 = query(x, a)
    l2 = query(x, b)
    return max((L[x] + L[a] - 2 * L[l1], a), (L[x] + L[b] - 2 * L[l2], b))


def merge(a, b):
    x = find(a)
    y = find(b)
    new_diam_l = max(diamL[x], diamL[y])
    new_diam = diam[x] if diamL[x] > diamL[y] else diam[y]
    curr = 1 + furthest(a)[0] + furthest(b)[0]
    if curr > new_diam_l:
        new_diam_l = curr
        new_diam = (furthest(a)[1], furthest(b)[1])
    parent[x] = y
    diamL[y] = new_diam_l
    diam[y] = new_diam


if __name__ == "__main__":
    n, q = map(int, input().split())
    for i in range(1, q + 1):
        data = list(map(int, input().split()))
        Q[i] = Query(data[0], data[1], data[2] if len(data) > 2 else None)
        if Q[i].t == 1:
            g[Q[i].a].append(Q[i].b)
            g[Q[i].b].append(Q[i].a)
    for i in range(1, n + 1):
        if not vis[i]:
            ch_root(i)
    for i in range(1, n + 1):
        for j in range(18):
            P[i][j] = -1
    for i in range(1, n + 1):
        P[i][0] = T[i]
    for j in range(1, 18):
        for i in range(1, n + 1):
            if P[i][j - 1] != -1:
                P[i][j] = P[P[i][j - 1]][j - 1]
    for i in range(1, n + 1):
        parent[i] = i
        diam[i] = (i, i)
    for i in range(1, q + 1):
        if Q[i].t == 1:
            merge(Q[i].a, Q[i].b)
        else:
            print(furthest(Q[i].a)[0])
