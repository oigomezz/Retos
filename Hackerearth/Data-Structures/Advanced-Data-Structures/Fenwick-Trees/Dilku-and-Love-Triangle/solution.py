from collections import defaultdict


class Graph:
    def __init__(self, size):
        self.adjacency_list = defaultdict(list)
        self.size = size
        self.bit = [0] * (size + 1)
        self.start = [0] * (size + 1)
        self.end = [0] * (size + 1)
        self.dp = [[0] * (size + 1) for _ in range(20)]
        self.len = 0
        self.level = [0] * (size + 1)

    def update(self, index, value):
        while index <= self.size:
            self.bit[index] += value
            index += index ^ (index & (index - 1))

    def query(self, index):
        result = 0
        while index > 0:
            result += self.bit[index]
            index &= (index - 1)
        return result

    def dfs(self, node, parent):
        self.start[node] = self.len + 1
        self.dp[0][node] = parent
        self.level[node] = self.level[parent] + 1
        self.len += 1
        for neighbor in self.adjacency_list[node]:
            if neighbor != parent:
                self.dfs(neighbor, node)
        self.end[node] = self.len

    def lca(self, a, b):
        if self.level[a] > self.level[b]:
            a, b = b, a
        depth_diff = self.level[b] - self.level[a]
        for i in range(20):
            if (1 << i) & depth_diff:
                b = self.dp[i][b]
        if a == b:
            return a
        for i in range(19, -1, -1):
            if self.dp[i][a] != self.dp[i][b]:
                a = self.dp[i][a]
                b = self.dp[i][b]
        return self.dp[0][a]


def main():
    n, q = map(int, input().split())
    graph = Graph(n)
    for _ in range(1, n):
        u, v = map(int, input().split())
        graph.adjacency_list[u].append(v)
        graph.adjacency_list[v].append(u)
    graph.dfs(1, 1)
    for i in range(1, 20):
        for j in range(1, n + 1):
            graph.dp[i][j] = graph.dp[i - 1][graph.dp[i - 1][j]]
    for _ in range(q):
        t, *line = map(int, input().split())
        if t == 1:
            u, v = line
            lca_node = graph.lca(u, v)
            graph.update(graph.start[u], 1)
            graph.update(graph.start[v], 1)
            graph.update(graph.start[lca_node], -1)
            if lca_node != 1:
                graph.update(graph.start[graph.dp[0][lca_node]], -1)
        elif t == 2:
            x = line[0]
            print(graph.query(graph.end[x]) - graph.query(graph.start[x] - 1))


if __name__ == '__main__':
    main()
