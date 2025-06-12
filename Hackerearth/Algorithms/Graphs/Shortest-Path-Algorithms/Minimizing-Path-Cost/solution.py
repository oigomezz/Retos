def floyd_warshall(graph, size):
    for k in range(0, size):
        for i in range(0, size):
            for j in range(0, size):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


n, m = map(int, input().strip().split())
stations = input().strip().split()
indexes = {}
for i, v in enumerate(stations):
    indexes[v] = i
adj = [[0 if i == j else float('inf') for i in range(n)] for j in range(n)]
for _ in range(m):
    station1, station2, d = input().strip().split()
    adj[indexes[station1]][indexes[station2]
                           ] = adj[indexes[station2]][indexes[station1]] = int(d)

floyd_warshall(adj, n)
q = int(input())
for _ in range(q):
    source, destination = input().strip().split()
    print(adj[indexes[source]][indexes[destination]])
