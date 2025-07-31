from collections import defaultdict

p = [[-1] * 20 for _ in range(200005)]
ht = [0] * 200005
dp = [0] * 200005
adj = defaultdict(list)
prm = [0] * 200005


def dfs(node, parent, count=0, value=0):
    p[node][0] = parent
    for key in range(1, 20):
        if p[node][key - 1] == -1:
            break
        p[node][key] = p[p[node][key - 1]][key - 1]
    count += 1 if prm[node] == 0 else 0
    dp[node] = count
    ht[node] = value
    for neighbor in adj[node]:
        if neighbor != parent:
            dfs(neighbor, node, count, value + 1)


def anc(node_a, node_b):
    if ht[node_a] < ht[node_b]:
        node_a, node_b = node_b, node_a
    depth_difference = ht[node_a] - ht[node_b]
    for idx in range(19, -1, -1):
        if depth_difference & (1 << idx):
            node_a = p[node_a][idx]
    if node_a == node_b:
        return node_a
    for idx in range(19, -1, -1):
        if p[node_a][idx] != p[node_b][idx]:
            node_a = p[node_a][idx]
            node_b = p[node_b][idx]
    return p[node_a][0]


if __name__ == "__main__":
    n = int(input())
    prm[1] = 1
    for i in range(2, 200005):
        if prm[i] == 0:
            for j in range(i * i, 200005, i):
                prm[j] = 1
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    dfs(1, -1)
    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        k = anc(u, v)
        answer = dp[u] + dp[v] - 2 * dp[k] + (1 if prm[k] == 0 else 0)
        print(answer)
