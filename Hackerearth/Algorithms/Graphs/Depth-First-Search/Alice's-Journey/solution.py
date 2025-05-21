from collections import defaultdict

dp = [0] * 200001


def dfs(node, parent, adjacency_list):
    for child in adjacency_list[node]:
        weight = child[1]
        child_node = child[0]
        if child_node == parent:
            continue
        dp[child_node] = weight + dp[node]
        dfs(child_node, node, adjacency_list)


n = int(input())
total_weight = 0
best_node = 0
diameter = 0
adjacency_list = defaultdict(list)

for i in range(1, n):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    total_weight += c
    adjacency_list[a].append((b, c))
    adjacency_list[b].append((a, c))

dfs(0, -1, adjacency_list)

for i in range(1, n):
    if dp[best_node] < dp[i]:
        best_node = i

dp[:] = [0] * len(dp)
dfs(best_node, -1, adjacency_list)

for i in range(n):
    diameter = max(diameter, dp[i])

print(2 * total_weight - diameter)
