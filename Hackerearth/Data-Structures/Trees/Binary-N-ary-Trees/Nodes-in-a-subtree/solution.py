from collections import defaultdict


def generate(adj, string, res, node=1):
    res[node] = string[node - 1]
    if not adj[node]:
        return res[node]
    else:
        for neighbor in adj[node]:
            adj[neighbor].remove(node)
            res[node] = res[node] + generate(adj, string, res, neighbor)
        return res[node]


n, q = map(int, input().strip().split())
s = input().strip()
edges = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().strip().split())
    edges[u].append(v)
    edges[v].append(u)

tree = {}
generate(edges, s, tree)
for _ in range(q):
    u, c = input().strip().split()
    u = int(u)
    print(tree[u].count(c))
