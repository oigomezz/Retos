from heapq import heapify, heappop, heappush
from bisect import bisect


n, m = map(int, input().strip().split())
houses = []
for _ in range(n):
    houses.append(input().strip())
l_cost, r_cost, u_cost, d_cost = map(int, input().strip().split())
stx, sty = map(lambda i: int(i) - 1, input().strip().split())
moves = ((l_cost, (0, -1)), (r_cost, (0, 1)),
         (u_cost, (-1, 0)), (d_cost, (1, 0)))
visited = [[False] * m for _ in range(n)]
heap = [(0, (stx, sty))]
heapify(heap)
costs = []
while heap:
    cost, (x, y) = heappop(heap)
    if not visited[x][y]:
        visited[x][y] = True
        costs.append(cost)
        for m_cost, (dx, dy) in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and houses[nx][ny] != '#' and not visited[nx][ny]:
                heappush(heap, (cost + m_cost, (nx, ny)))

q = int(input())
for _ in range(q):
    x = int(input())
    print(bisect(costs, x))
