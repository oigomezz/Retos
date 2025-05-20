from collections import defaultdict


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, a):
        if a == self.parent[a]:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b:
            if self.size[parent_a] < self.size[parent_b]:
                parent_a, parent_b = parent_b, parent_a
            self.parent[parent_b] = parent_a
            self.size[parent_a] += self.size[parent_b]


n = int(input())
N = n + 1
sp = [0] * N
v = [False] * N
for i in range(2, N, 2):
    sp[i] = 2

for i in range(3, N, 2):
    if not v[i]:
        sp[i] = i
        j = i
        while j * i < N:
            v[j * i] = True
            sp[j * i] = i
            j += 2

dsu = DSU(n + 1)
edges = []
graph = defaultdict(set)
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))
    graph[u].add(v)
    graph[v].add(u)

for u, v in edges:
    if sp[u] != u and sp[v] != v:
        dsu.union(u, v)

components = defaultdict(set)
for el in graph:
    if sp[el] != el:
        components[dsu.find(el)].add(el)

res = 0
for c in components:
    for i in components[c]:
        for j in graph[i]:
            if sp[j] == j:
                res += len(components[c])
                for k in graph[j]:
                    if sp[k] != k and dsu.find(k) > c:
                        res += len(components[c]) * \
                            len(components[dsu.find(k)])

print(res)
