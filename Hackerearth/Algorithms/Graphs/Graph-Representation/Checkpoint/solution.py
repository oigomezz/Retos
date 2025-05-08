from collections import defaultdict, deque

# Function to find if an augmenting path exists
def bfs(adjacency, pair_u, pair_v, dist):
    queue = deque()
    for u in pair_u:
        if pair_u[u] is None:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = float('inf')

    dist[None] = float('inf')
    while queue:
        u = queue.popleft()
        if dist[u] < dist[None]:
            for v in adjacency[u]:
                if dist[pair_v[v]] == float('inf'):
                    dist[pair_v[v]] = dist[u] + 1
                    queue.append(pair_v[v])
    return dist[None] != float('inf')


# Function to find a matching for a vertex
def dfs(adjacency, pair_u, pair_v, dist, u):
    if u is None:
        return True

    for v in adjacency[u]:
        if dist[pair_v[v]] == dist[u] + 1 and dfs(adjacency, pair_u, pair_v, dist, pair_v[v]):
            pair_u[u] = v
            pair_v[v] = u
            return True

    dist[u] = float('inf')
    return False


# Function to find the maximum matching
def maximum_matching(adjacency, u_set, v_set):
    pair_u = {u: None for u in u_set}
    pair_v = {v: None for v in v_set}
    dist = {}

    matching = 0
    while bfs(adjacency, pair_u, pair_v, dist):
        for u in u_set:
            if pair_u[u] is None and dfs(adjacency, pair_u, pair_v, dist, u):
                matching += 1

    return matching


# Main function
n, m, p = map(int, input().split())

graph = defaultdict(set)
u_set = set()

for _ in range(p):
    u, v = map(int, input().split())
    graph[u].add(v)
    u_set.add(u)

v_set = set(range(1, m + 1))

# Add None as a virtual vertex on the right side
v_set.add(None)

# Find the maximum matching
matching_size = maximum_matching(graph, u_set, v_set)

# The minimum vertex cover will have the same size as the maximum matching
minimum_vertex_cover_size = matching_size

print(minimum_vertex_cover_size)
