import heapq

N, M = map(int, input().split())
S, E = map(int, input().split())
adj_list = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u-1].append((v-1, 0))
    adj_list[v-1].append((u-1, 0))
node_values = list(map(int, input().split()))

# Initialize priority queue
pq = [(0, S-1, 0)]

# Initialize visited set
visited = set()

# Process nodes in priority order
while pq:
    # Get next node from priority queue
    path_value, node, max_diff = heapq.heappop(pq)

    # Check if node has been visited before
    if node in visited:
        continue

    if node == E-1:
        print(max_diff)
        break

    visited.add(node)

    for neighbor, weight in adj_list[node]:
        diff = abs(node_values[node] - node_values[neighbor])
        new_max_diff = max(max_diff, diff)
        new_path_value = max(path_value, new_max_diff)
        heapq.heappush(pq, (new_path_value, neighbor, new_max_diff))
