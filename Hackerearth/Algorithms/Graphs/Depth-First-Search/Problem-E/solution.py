from collections import defaultdict


def dfs(node, parent):
    dp[node][0] = parent
    for neighbor in adjacency_list[node]:
        if neighbor == parent:
            continue
        depth[neighbor] = 1 + depth[node]
        dfs(neighbor, node)


def lca(node_u, node_v):
    if depth[node_u] > depth[node_v]:
        node_u, node_v = node_v, node_u
    distance = depth[node_v] - depth[node_u]
    for i in range(19, -1, -1):
        if distance >= (1 << i):
            node_v = dp[node_v][i]
            distance -= (1 << i)
    if node_u == node_v:
        return node_u
    for i in range(19, -1, -1):
        if dp[node_u][i] != dp[node_v][i]:
            node_u = dp[node_u][i]
            node_v = dp[node_v][i]
    return dp[node_v][0]


def distance(node_u, node_v):
    return depth[node_u] + depth[node_v] - 2 * depth[lca(node_u, node_v)]


n, q = map(int, input().split())
depth = [0] * 500005
dp = [[0] * 20 for _ in range(500005)]
adjacency_list = defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, input().split())
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

depth[1] = 0
dfs(1, 0)

for j in range(1, 20):
    for i in range(1, n + 1):
        dp[i][j] = dp[dp[i][j - 1]][j - 1]

for _ in range(q):
    line = list(map(int, input().split()))
    x = line[0]
    a = [0] * (x + 1)
    for i in range(1, x + 1):
        a[i] = line[i]

    id_max = 1
    max_distance = 0
    for i in range(2, x + 1):
        current_distance = distance(a[i], a[1])
        if current_distance > max_distance:
            max_distance = current_distance
            id_max = i

    max_distance = 0
    for i in range(1, x + 1):
        max_distance = max(max_distance, distance(a[i], a[id_max]))

    print(max_distance)
