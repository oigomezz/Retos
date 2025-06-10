from collections import defaultdict
from heapq import heappop, heappush

n, m = map(int, input().strip().split())
metro = defaultdict(list)
for _ in range(m):
    k, t = map(int, input().strip().split())
    u = list(map(int, input().strip().split()))
    w = list(map(int, input().strip().split()))
    time = t
    for i in range(k - 1):
        metro[u[i]].append((u[i + 1], time, w[i]))
        time += w[i]

start, end = map(int, input().strip().split())
heap = [(0, start)]
paths = [float('inf')] * (n + 1)
while heap:
    total, station = heappop(heap)
    for next_station, time, seconds in metro[station]:
        if time >= total:
            new_total = total + seconds
            if paths[next_station] >= new_total:
                heappush(heap, (new_total, next_station))
                paths[next_station] = new_total

print(-1 if paths[end] == float('inf') else paths[end])
