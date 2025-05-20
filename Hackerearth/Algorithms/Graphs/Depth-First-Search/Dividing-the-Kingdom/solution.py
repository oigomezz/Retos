from collections import defaultdict


def dfs(current_node, parent_node):
    offset = 0
    dp_sum = 0
    for neighbor in adjacency_list[current_node]:
        if neighbor == parent_node:
            continue
        dfs(neighbor, current_node)
        dp_sum += A[neighbor]
        offset = max(offset, B[neighbor] - A[neighbor] + 1)
    B[current_node] = dp_sum
    A[current_node] = dp_sum + offset


n = int(input())
edges = [list(map(int, input().split())) for _ in range(n - 1)]
adjacency_list = defaultdict(list)
for edge in edges:
    u, v = edge
    u -= 1
    v -= 1
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

A = [0] * n
B = [0] * n

dfs(0, -1)
print(A[0])
