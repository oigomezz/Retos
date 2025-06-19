def hungarian(adjacency_matrix):
    n = len(adjacency_matrix)
    m = len(adjacency_matrix[0])
    potential_u = [0] * n
    potential_v = [0] * m
    match = [0] * m

    for i in range(1, n):
        w = 0
        match[w] = i
        dist = [float('inf')] * m
        predecessor = [-1] * m
        visited = [False] * m

        while match[w]:
            visited[w] = True
            current = match[w]
            nw = 0
            delta = float('inf')
            for j in range(1, m):
                if not visited[j]:
                    edge = adjacency_matrix[current][j] - \
                        potential_u[current] - potential_v[j]
                    if edge < dist[j]:
                        dist[j] = edge
                        predecessor[j] = w
                    if dist[j] < delta:
                        delta = dist[j]
                        nw = j
            for j in range(m):
                if visited[j]:
                    potential_u[match[j]] += int(delta)
                    potential_v[j] -= int(delta)
                else:
                    dist[j] -= delta
            w = nw

        while w:
            nw = predecessor[w]
            match[w] = match[nw]
            w = nw

    return -potential_v[0]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        adjacency_matrix = [[0] * (k + 1) for _ in range(k + 1)]
        arr = list(map(int, input().split()))
        for i in range(n):
            adjacency_matrix[arr[i]][i % k + 1] -= 1

        print(n + hungarian(adjacency_matrix))
