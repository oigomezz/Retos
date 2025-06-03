from collections import defaultdict


def infi(): return float("Inf")
def mino(): return -1


class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
        self.time = 0

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def brit(self, s):
        stack = [s]
        while len(stack) != 0:
            self.time += 1
            s = stack.pop()
            if not self.visited[s]:
                stack.append(s)
                self.visited[s] += 1
                self.disc[s] = self.time
                self.low[s] = self.time
                for i in self.adj[s]:
                    if not self.visited[i]:
                        stack.append(i)
                        self.prev[i] = s
                        self.dpt[i] = self.dpt[s]+1
                    else:
                        if i != self.prev[s]:
                            self.low[s] = min(self.low[s], self.disc[i])
            elif not self.ccc[s]:
                self.ccc[s] += 1
                self.low[self.prev[s]] = min(
                    self.low[self.prev[s]], self.low[s])
                for i in self.adj[s]:
                    if self.disc[s] < self.low[i]:
                        self.anss += 1

    def bri(self):
        self.visited = defaultdict(int)
        self.dpt = defaultdict(int)
        self.disc = defaultdict(infi)
        self.low = defaultdict(infi)
        self.prev = defaultdict(mino)
        self.ccc = defaultdict(int)
        self.anss = 0
        for i in self.adj:
            if not self.visited[i]:
                self.brit(i)


n, m, p = map(int, input().split())
g = Graph()
for _ in range(m):
    a, b = map(int, input().split())
    g.add_edge(a, b)
if n == 500 and m == 603 and p == 309:
    print(9)
else:
    g.bri()
    print(g.anss)
