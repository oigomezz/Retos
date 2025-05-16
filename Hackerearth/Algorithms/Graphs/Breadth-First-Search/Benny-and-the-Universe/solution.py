n, q = map(int, input().strip().split())
d = sorted(map(int, input().strip().split()))
t = d[0]
dist = [1000000000 for _ in range(t)]
dist[0] = 0
unvisited = set(range(t))
while unvisited:
    next_visit = min(unvisited, key=lambda i: dist[i])
    unvisited.remove(next_visit)
    for spacecraft in d:
        idx = (next_visit + spacecraft) % t
        if dist[idx] > dist[next_visit] + spacecraft:
            dist[idx] = dist[next_visit] + spacecraft

for _ in range(q):
    x = int(input())
    print('YES' if dist[x % t] <= x else 'NO')
