def dfs(vertex, parent, adjacency_list, visited):
    for neighbor in adjacency_list[vertex]:
        if neighbor == parent:
            continue
        dfs(neighbor, vertex, adjacency_list, visited)
        if not visited[neighbor]:
            visited[vertex] = True


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        adjacency_list = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        for i in range(1, n):
            parent = int(input())
            adjacency_list[parent].append(i + 1)

        dfs(1, -1, adjacency_list, visited)
        if visited[1]:
            print("A")
        else:
            print("B")
