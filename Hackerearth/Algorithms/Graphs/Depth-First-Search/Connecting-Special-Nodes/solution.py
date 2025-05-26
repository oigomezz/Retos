from collections import defaultdict, deque


def calc(start, seen, adjacency, special=False):
    if seen[start - 1]:
        return
    seen[start - 1] = True
    count = 1
    edges = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for next_node in adjacency[node]:
            if not seen[next_node - 1]:
                seen[next_node - 1] = True
                count += 1
                queue.append(next_node)
            if (node, next_node) not in edges and (next_node, node) not in edges:
                edges.add((node, next_node))
    global ans
    ans += count * (count - 1) // 2 - len(edges)
    if special:
        global maximum
        maximum = max(count, maximum)
    else:
        global normal_nodes, cost
        temp = normal_nodes * count
        normal_nodes += count
        cost += temp
        ans += temp


n, m, k = map(int, input().strip().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)
special_nodes = map(int, input().strip().split())
visited = [False] * n
ans = cost = maximum = 0
for special_node in special_nodes:
    calc(special_node, visited, graph, True)
normal_nodes = 0
for i in range(1, n + 1):
    calc(i, visited, graph)
ans += maximum * normal_nodes
cost += maximum * normal_nodes
print(ans, cost)
