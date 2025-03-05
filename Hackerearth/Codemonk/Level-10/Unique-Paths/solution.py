class Solution:
    def __init__(self):
        self.graph = []
        self.trees = []
        self.depths = []
        self.indices = []
        self.in_time = []
        self.low = []
        self.parents = []
        self.root = 0

    def init(self, n, edges):
        self.graph.clear()
        self.graph = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge
            self.graph[u].append(v)
            self.graph[v].append(u)

        self.trees.clear()
        self.trees = [[] for _ in range(n)]
        self.depths = [0] * n
        self.indices = [-1] * n
        self.in_time = [-1] * n
        self.low = [1 << 24] * n

        height = 0
        clock = 0
        while (1 << height) <= n:
            height += 1

        self.parents = [[-1] * height for _ in range(n)]
        self.root = 0
        bridges = []
        self.dfs(self.root, -1, clock, bridges)
        for edge in bridges:
            u, v = edge
            self.trees[u].append(v)
            self.trees[v].append(u)

        for i in range(n):
            if self.indices[i] == -1:
                self.dfs2(i, -1, 0, i)

    def query(self, u, v):
        if self.indices[u] != self.indices[v]:
            return -1
        p = self.lca(u, v)
        return self.depths[u] + self.depths[v] - 2 * self.depths[p]

    def dfs(self, u, p, t, bridges):
        self.low[u] = self.in_time[u] = t + 1
        for v in self.graph[u]:
            if v == p:
                continue
            if self.in_time[v] >= 0:
                self.low[u] = min(self.low[u], self.in_time[v])
            else:
                self.dfs(v, u, t, bridges)
                self.low[u] = min(self.low[u], self.low[v])
                if self.low[v] > self.in_time[u]:
                    bridges.append((u, v))

    def dfs2(self, u, p, d, id):
        self.parents[u][0] = p
        self.depths[u] = d
        self.indices[u] = id
        height = len(self.parents[u])
        for i in range(1, height):
            if self.parents[u][i - 1] >= 0:
                self.parents[u][i] = self.parents[self.parents[u]
                                                  [i - 1]][i - 1]
        for v in self.trees[u]:
            if v == p:
                continue
            self.dfs2(v, u, d + 1, id)

    def lca(self, u, v):
        if u == -1 or v == -1:
            return v if u == -1 else u
        if v == u:
            return v
        if self.depths[u] > self.depths[v]:
            u, v = v, u
        height = len(self.parents[u])
        for i in range(height - 1, -1, -1):
            if self.parents[v][i] >= 0 and self.depths[self.parents[v][i]] >= self.depths[u]:
                v = self.parents[v][i]
        if v == u:
            return u
        for i in range(height - 1, -1, -1):
            if self.parents[u][i] != self.parents[v][i]:
                u = self.parents[u][i]
                v = self.parents[v][i]
        return self.parents[u][0]


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []
    for i in range(1, m + 1):
        u, v = map(int, input().split())
        edges.append((u - 1, v - 1))

    solution = Solution()
    solution.init(n, edges)

    q = int(input())
    for i in range(m + 2, m + 2 + q):
        u, v = map(int, input().split())
        print(solution.query(u - 1, v - 1))
