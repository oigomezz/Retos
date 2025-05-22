from collections import defaultdict

graph = defaultdict(list)
parent = [[0] * 20 for _ in range(100001)]
depth = [0] * 100001
xors = [0] * 100001


def dfs1(node, parent_node, current_depth):
    parent[node][0] = parent_node
    depth[node] = current_depth
    for i in range(1, 20):
        parent[node][i] = parent[parent[node][i - 1]][i - 1]
    for next_node in graph[node]:
        if next_node == parent_node:
            continue
        dfs1(next_node, node, current_depth + 1)


def dfs2(node, parent_node):
    current_xor = xors[node]
    for next_node in graph[node]:
        if next_node != parent_node:
            current_xor ^= dfs2(next_node, node)
    xors[node] = current_xor
    return current_xor


def lca(u, v):
    if depth[u] > depth[v]:
        u, v = v, u
    depth_u = depth[u]
    depth_v = depth[v]
    difference = depth_v - depth_u
    for i in range(19, -1, -1):
        if difference >= (1 << i):
            v = parent[v][i]
            difference -= (1 << i)
    if u == v:
        return u
    for i in range(19, -1, -1):
        if parent[u][i] != parent[v][i]:
            u = parent[u][i]
            v = parent[v][i]
    return parent[u][0]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        for i in range(n + 1):
            graph[i].clear()
            xors[i] = 0
            depth[i] = 0
            for j in range(20):
                parent[i][j] = 0
        for _ in range(n - 1):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        queries = []
        for _ in range(q):
            u, v, w = map(int, input().split())
            queries.append((u, v, w))

        dfs1(1, 0, 1)
        for u, v, w in queries:
            ancestor = lca(u, v)
            xors[ancestor] ^= w
            xors[parent[ancestor][0]] ^= w
            xors[u] ^= w
            xors[v] ^= w
        dfs2(1, 0)
        total_xor_sum = sum(xors[1:n + 1])
        print(total_xor_sum)
