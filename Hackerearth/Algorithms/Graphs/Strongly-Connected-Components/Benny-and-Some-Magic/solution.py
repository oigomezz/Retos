from collections import defaultdict

g = defaultdict(list)
was = [0] * 333333
val = [0] * 333333
edges = []


class Edge:
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight


def dfs(v, w):
    if was[v]:
        return
    val[v] = w
    was[v] = 1
    for to in g[v]:
        dfs(to, w)


if __name__ == "__main__":
    n, m = map(int, input().split())
    ans = 0
    mx = [0] * 333333
    mn = [0] * 333333

    for _ in range(m):
        from_node, to_node, w = map(int, input().split())
        from_node -= 1
        to_node -= 1
        edges.append(Edge(from_node, to_node, w))
        g[from_node].append(to_node)

    edges.sort(key=lambda edge: edge.weight)

    for i in range(n):
        was[i] = 0
        val[i] = 1 << 30

    for edge in edges:
        dfs(edge.to_node, edge.weight)

    for i in range(n):
        mn[i] = val[i]

    for i in range(n):
        was[i] = 0
        val[i] = -(1 << 30)

    for edge in reversed(edges):
        dfs(edge.to_node, edge.weight)

    for i in range(n):
        mx[i] = val[i]

    for edge in edges:
        v = edge.from_node
        if mn[v] != 1 << 30:
            ans = max(ans, edge.weight - mn[v])
        if mx[v] != -(1 << 30):
            ans = max(ans, mx[v] - edge.weight)

    print(ans)
