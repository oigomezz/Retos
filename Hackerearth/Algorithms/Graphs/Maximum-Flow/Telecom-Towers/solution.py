from collections import defaultdict

N = 100005
vis = [0] * N
v = defaultdict(list)

NN = 50005
MM = 500005


class MaxFlow:
    def __init__(self):
        self.gr = [[] for _ in range(NN)]
        self.edges = []
        self.source = 0
        self.sink = 0
        self.flow = 0
        self.n = 0
        self.ec = 0
        self.level = [-1] * NN
        self.Q = [0] * NN
        self.PV = [0] * NN

    def init(self, sz, src, snk):
        self.n = sz
        self.source = src
        self.sink = snk
        self.flow = 0
        self.ec = 0
        for i in range(self.n + 1):
            self.gr[i].clear()

    def add_edge(self, x, y, w):
        self.gr[x].append(self.ec)
        self.edges.append((x, y, w))
        self.ec += 1
        self.gr[y].append(self.ec)
        self.edges.append((y, x, 0))  # for undirected replace 0 with w
        self.ec += 1

    def block_flow(self, cur, cnt):
        if cur == self.sink:
            return cnt
        for i in range(self.PV[cur], -1, -1):
            cur_e = self.gr[cur][i]
            if self.edges[cur_e][2] and self.level[self.edges[cur_e][1]] == self.level[cur] + 1:
                val = self.block_flow(
                    self.edges[cur_e][1], min(cnt, self.edges[cur_e][2]))
                if val:
                    self.edges[cur_e] = (
                        self.edges[cur_e][0], self.edges[cur_e][1], self.edges[cur_e][2] - val)
                    self.edges[cur_e ^ 1] = (
                        self.edges[cur_e ^ 1][0], self.edges[cur_e ^ 1][1], self.edges[cur_e ^ 1][2] + val)
                    return val
        return 0

    def get_level(self):
        head = 0
        tail = 0
        for i in range(self.n + 1):
            self.level[i] = -1
        self.Q[tail] = self.source
        self.level[self.source] = 0
        tail += 1
        while head < tail:
            cur = self.Q[head]
            head += 1
            for t in self.gr[cur]:
                if self.edges[t][2] and self.level[self.edges[t][1]] == -1:
                    self.level[self.edges[t][1]] = self.level[cur] + 1
                    self.Q[tail] = self.edges[t][1]
                    tail += 1
        return self.level[self.sink] != -1

    def dinic(self):
        self.flow = 0
        while self.get_level():
            for i in range(self.n + 1):
                self.PV[i] = len(self.gr[i]) - 1
            while True:
                t = self.block_flow(self.source, float('inf'))
                if not t:
                    break
                self.flow += t


G = MaxFlow()  # dont forget to initialise


def dis(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def dfs(cur, col):
    vis[cur] = col
    for x in v[cur]:
        if vis[x] == 1:
            dfs(x, 5 - col)


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    a = [tuple(map(int, data[i:i + 2])) for i in range(2, 2 + 2 * n, 2)]

    G.init(n + 2, 0, n + 1)

    for i in range(n):
        for j in range(i + 1, n):
            if dis(a[i], a[j]) == k * k:
                v[i + 1].append(j + 1)
                v[j + 1].append(i + 1)
                vis[i + 1] = vis[j + 1] = 1

    for i in range(1, n + 1):
        if vis[i] == 1:
            dfs(i, 2)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dis(a[i - 1], a[j - 1]) == k * k and vis[i] == 2 and vis[j] == 3:
                G.add_edge(i, j, k)

    for i in range(1, n + 1):
        if vis[i] == 2:
            G.add_edge(0, i, 1)
        elif vis[i] == 3:
            G.add_edge(i, n + 1, 1)

    G.dinic()
    print(G.flow)
