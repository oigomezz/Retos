def dfs(graph, index, visited, subtree, size, all_accepted_edges):
    visited[index] = True
    size[0] += 1
    subtree[index] += 1
    for edge in graph[index]:
        node, weight = edge
        if not visited[node]:
            dfs(graph, node, visited, subtree,
                size, all_accepted_edges)
            all_accepted_edges.append((weight, subtree[node]))
            subtree[index] += subtree[node]


def tbt_helper(start, graph, visited, subtree, mod):
    size = [0]
    ans = 0
    all_accepted_edges = []
    dfs(graph, start, visited, subtree,
        size, all_accepted_edges)
    for edge in all_accepted_edges:
        weight, curr_subtree_value = edge
        ans += weight * curr_subtree_value * (size[0] - curr_subtree_value)
        ans %= mod
    return ans


def temporary_binary_tree(n, edges):
    ans = 0
    mod = 1000000007
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        u, v, edge_type, weight = edge
        if edge_type == 1:
            graph[u].append((v, weight))
            graph[v].append((u, weight))
    visited = [False] * (n + 1)
    subtree = [0] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            ans += tbt_helper(i, graph, visited, subtree, mod)
            ans %= mod
    return ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []
        for i in range(n - 1):
            edges.append(list(map(int, input().split())))
        print(str(temporary_binary_tree(n, edges)))
