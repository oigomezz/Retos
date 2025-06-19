class Edge:
    def __init__(self, u, v, cap, cost):
        self.u = u
        self.v = v
        self.cap = cap
        self.cost = cost
        self.flow = 0


class MCMF:
    def __init__(self, n, s, t):
        self.m = 0
        self.n = n
        self.s = s
        self.t = t
        self.par = [0] * n
        self.pi = [float('inf')] * n
        self.dist = [0] * n
        self.edges = []
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, cap, cost):
        self.edges.append(Edge(u, v, cap, cost))
        self.edges.append(Edge(v, u, 0, -cost))
        self.adj[u].append(self.m)
        self.adj[v].append(self.m + 1)
        self.m += 2

    def path(self):
        self.dist = [float('inf')] * self.n
        pq = []
        pq.append((0, self.s))
        self.dist[self.s] = 0
        while pq:
            d, u = pq.pop(0)
            if d > self.dist[u]:
                continue
            for e in self.adj[u]:
                if self.edges[e].flow < self.edges[e].cap and self.dist[u] + self.edges[e].cost + self.pi[u] - self.pi[self.edges[e].v] < self.dist[self.edges[e].v]:
                    self.par[self.edges[e].v] = e
                    self.dist[self.edges[e].v] = self.dist[u] + \
                        self.edges[e].cost + self.pi[u] - \
                        self.pi[self.edges[e].v]
                    pq.append((self.dist[self.edges[e].v], self.edges[e].v))
        return self.dist[self.t] < float('inf')

    def set_pi(self):
        self.pi = [float('inf')] * self.n
        self.pi[self.s] = 0
        for _ in range(self.n):
            cycle = False
            for e in self.edges:
                if e.cap > 0 and self.pi[e.u] < float('inf') and self.pi[e.u] + e.cost < self.pi[e.v]:
                    self.pi[e.v] = self.pi[e.u] + e.cost
                    cycle = True
            if not cycle:
                break

    def max_flow(self, limit=float('inf')):
        self.set_pi()
        ret_flow = 0
        ret_cost = 0
        while limit > 0 and self.path():
            for u in range(self.n):
                self.pi[u] += self.dist[u]
            f = limit
            u = self.t
            while u != self.s:
                f = min(f, self.edges[self.par[u]].cap -
                        self.edges[self.par[u]].flow)
                u = self.edges[self.par[u]].u
            ret_flow += f
            ret_cost += f * (self.pi[self.t] - self.pi[self.s])
            limit -= f
            u = self.t
            while u != self.s:
                self.edges[self.par[u]].flow += f
                self.edges[self.par[u] ^ 1].flow -= f
                u = self.edges[self.par[u]].u
        return ret_flow, ret_cost


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        mcmf = MCMF(n + 2, n, n + 1)
        for i in range(k):
            mcmf.add_edge(mcmf.s, i, 1, 0)
            mcmf.add_edge(n - i - 1, mcmf.t, 1, 0)
        for i in range(n):
            for j in range(n):
                mcmf.add_edge(i, j, 10000, 10000)
        for i in range(m):
            x, y, c = map(int, input().split())
            x -= 1
            y -= 1
            mcmf.add_edge(x, y, 10000, c)
            mcmf.add_edge(y, x, 10000, c)
        print(mcmf.max_flow()[1])
