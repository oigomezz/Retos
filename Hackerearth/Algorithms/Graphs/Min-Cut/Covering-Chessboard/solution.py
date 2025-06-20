from collections import deque

INF = int(1e9)
N = 4031
distances = [0] * N
pointers = [0] * N
edges = []
graph = [[] for _ in range(N)]
source, sink = 0, 0
n, m = 0, 0
capacity = [[0] * 50 for _ in range(50)]
value = [[0] * 50 for _ in range(50)]
bounded = [[0] * 50 for _ in range(50)]


class Edge:
    def __init__(self, a, b, capacity, flow):
        self.a = a
        self.b = b
        self.capacity = capacity
        self.flow = flow


def add_edge(a, b, capacity):
    edge1 = Edge(a, b, capacity, 0)
    graph[a].append(len(edges))
    edges.append(edge1)
    edge2 = Edge(b, a, 0, 0)
    graph[b].append(len(edges))
    edges.append(edge2)


def bfs():
    for i in range(N):
        distances[i] = -1
    queue = deque()
    queue.append(source)
    distances[source] = 0
    while queue:
        vertex = queue.popleft()
        for i in range(len(graph[vertex])):
            edge_id = graph[vertex][i]
            to = edges[edge_id].b
            if edges[edge_id].flow == edges[edge_id].capacity:
                continue
            if distances[to] != -1:
                continue
            distances[to] = distances[vertex] + 1
            queue.append(to)
    return distances[sink] != -1


def dfs(vertex, flow):
    if vertex == sink or flow == 0:
        return flow
    while pointers[vertex] < len(graph[vertex]):
        edge_id = graph[vertex][pointers[vertex]]
        to = edges[edge_id].b
        if distances[to] != distances[vertex] + 1:
            pointers[vertex] += 1
            continue
        pushed = dfs(
            to, min(flow, edges[edge_id].capacity - edges[edge_id].flow))
        if pushed:
            edges[edge_id].flow += pushed
            edges[edge_id ^ 1].flow -= pushed
            return pushed
        pointers[vertex] += 1
    return 0


def dinic():
    flow = 0
    while True:
        if not bfs():
            break
        for i in range(N):
            pointers[i] = 0
        while True:
            pushed = dfs(source, 100000000)
            if pushed == 0:
                break
            flow += pushed
    return flow


def get_ps(a, b):
    return a * m + b


def paired(x):
    if x >= 1000:
        return x - 1000
    return x + 1000


def outside(a, b):
    return a < 0 or a >= n or b < 0 or b >= m


if __name__ == "__main__":
    n, m = map(int, input().split())
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            value[i][j] = line[j]
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            bounded[i][j] = line[j]
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            capacity[i][j] = line[j]

    total_value = 0
    source = N - 2
    sink = N - 1
    for i in range(n):
        for j in range(m):
            total_value += value[i][j]
            ps = get_ps(i, j)
            add_edge(ps, paired(ps), value[i][j])
            if i % 2 != j % 2:
                add_edge(source, ps, capacity[i][j])
                add_edge(paired(ps), sink, min(bounded[i][j], value[i][j]))
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if abs(di) + abs(dj) != 1:
                            continue
                        if outside(i + di, j + dj):
                            continue
                        V = get_ps(i + di, j + dj)
                        add_edge(ps, V, INF)
                        add_edge(paired(ps), paired(V), INF)
            else:
                add_edge(source, ps, min(bounded[i][j], value[i][j]))
                add_edge(paired(ps), sink, capacity[i][j])
    print(total_value - dinic())
