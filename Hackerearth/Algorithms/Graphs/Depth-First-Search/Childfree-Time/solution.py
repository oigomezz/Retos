def exploring(u, adjacency, seen, times):
    seen[u] = True
    spend_time = 0
    for v, time in adjacency[u]:
        if not seen[v]:
            explore = exploring(v, adjacency, seen, times)
            spend_time = max(spend_time, 2 + time + explore)
        else:
            spend_time = max(spend_time, 2 + time + times[v])
    times[u] = spend_time
    return spend_time


r, p = map(int, input().strip().split())
labyrinths = [[] for _ in range(r)]
for _ in range(p):
    r1, r2, t = map(int, input().strip().split())
    labyrinths[r1 - 1].append((r2 - 1, t))
visited = [False] * r
time_rooms = [0] * r
max_time = 0
for i in range(r):
    if not visited[i]:
        max_time = max(max_time, exploring(i, labyrinths, visited, time_rooms))
print(max_time)
