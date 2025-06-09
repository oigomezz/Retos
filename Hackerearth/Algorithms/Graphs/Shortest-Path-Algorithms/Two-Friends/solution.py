import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)


class LCA:
    def __init__(self, n):
        self.k = (n).bit_length()
        self.timer = 0
        self.level = [0] * (n + 1)
        self.tin = [0] * (n + 1)
        self.tout = [0] * (n + 1)
        self.adj = defaultdict(list)
        self.up = [[0] * (self.k + 1) for _ in range(n + 1)]

    def is_ancestor(self, u, v):
        return self.tin[u] <= self.tin[v] and self.tout[u] >= self.tout[v]

    def lca(self, u, v):
        if self.is_ancestor(u, v):
            return u
        if self.is_ancestor(v, u):
            return v
        for i in range(self.k, -1, -1):
            if not self.is_ancestor(self.up[u][i], v):
                u = self.up[u][i]
        return self.up[u][0]

    def distance(self, u, v):
        lc = self.lca(u, v)
        return self.level[u] + self.level[v] - 2 * self.level[lc]

    def dfs(self, node, par):
        self.up[node][0] = par
        self.tin[node] = self.timer + 1
        self.timer += 1
        self.level[node] = 1 + self.level[par]
        for i in range(1, self.k + 1):
            self.up[node][i] = self.up[self.up[node][i - 1]][i - 1]
        for it in self.adj[node]:
            if it == par:
                continue
            self.dfs(it, node)
        self.tout[node] = self.timer + 1
        self.timer += 1

    def point_on_path(self, u, v, p):
        return self.distance(u, v) == self.distance(u, p) + self.distance(p, v)

    def helper(self, u, v, p):
        res = float('inf')
        lc = self.lca(u, v)
        res = min(res, self.distance(u, p))
        res = min(res, self.distance(v, p))

        x = self.lca(u, p)
        if x != u:
            if self.point_on_path(u, v, x):
                res = min(res, self.distance(x, p))
            else:
                res = min(res, self.distance(p, lc))
        x = self.lca(v, p)
        if x != v:
            if self.point_on_path(u, v, x):
                res = min(res, self.distance(x, p))
            else:
                res = min(res, self.distance(p, lc))
        return res


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        lca = LCA(n)
        for _ in range(n - 1):
            u, v = map(int, input().split())
            lca.adj[u].append(v)
            lca.adj[v].append(u)
        lca.dfs(1, 1)
        q = int(input())
        for _ in range(q):
            u, v, u2, v2 = map(int, input().split())
            lc1 = lca.lca(u, v)
            lc2 = lca.lca(u2, v2)

            if lca.level[lc1] < lca.level[lc2]:
                print(lca.helper(u, v, lc2))
            else:
                print(lca.helper(u2, v2, lc1))
