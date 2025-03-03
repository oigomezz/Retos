n, m, k = map(int, input().split())
v = [int(x) for x in input().split()]
g = [[] for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)

for i in range(n):
    g[i] = reversed(sorted(g[i]))
for i in range(n):
    g[i] = sorted(g[i], key=lambda x: -v[x])

for i in range(n):
    if len(g[i]) >= k:
        print(g[i][k-1]+1)
    else:
        print(-1)
