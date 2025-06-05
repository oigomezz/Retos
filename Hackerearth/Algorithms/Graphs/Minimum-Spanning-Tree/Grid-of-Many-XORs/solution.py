from heapq import heappush, heappop


def trip(adj):
    ln = len(adj)
    visited = [False] * ln
    visited[0] = True
    heap = []
    for x, x_cost in adj[0]:
        heappush(heap, (x_cost, x))
    min_cost = 0
    while heap:
        x_cost, x = heappop(heap)
        if not visited[x]:
            visited[x] = True
            min_cost += x_cost
        for y, y_cost in adj[x]:
            if not visited[y]:
                heappush(heap, (y_cost, y))
    return min_cost


t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    r1, c1, r2, c2 = map(int, input().strip().split())
    # No need for r1 c1 r2 c2. The value of answer is independent of them.
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().strip().split())))
    costs = [[] for _ in range(n * m)]
    for i in range(n):
        for j in range(m):
            if i - 1 >= 0:
                costs[i * m + j].append(((i - 1) * m + j,
                                        grid[i][j] ^ grid[i - 1][j]))
            if i + 1 < n:
                costs[i * m + j].append(((i + 1) * m + j,
                                        grid[i][j] ^ grid[i + 1][j]))
            if j - 1 >= 0:
                costs[i * m + j].append((i * m + j - 1,
                                        grid[i][j] ^ grid[i][j - 1]))
            if j + 1 < m:
                costs[i * m + j].append((i * m + j + 1,
                                        grid[i][j] ^ grid[i][j + 1]))
    print(trip(costs))
