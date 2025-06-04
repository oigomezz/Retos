from collections import defaultdict
import sys

E = defaultdict(list)
ans = sys.maxsize
u = [0] * 5000
d = [[0] * 3 for _ in range(5000)]
n = 0


def dfs(v):
    global ans
    d1, d2 = float('inf'), float('inf')
    d[v][0] = 0
    u[v] = 1
    for nv, tp in E[v]:
        if u[nv]:
            continue
        else:
            dfs(nv)
        d[v][0] += tp + d[nv][0]
        d1 = min(d1, d[nv][1] + 1 - tp - d[nv][0] - tp)
        d2 = min(d2, min((d[nv][2] + tp) - (d[nv][0] + tp),
                 d[nv][1] - (d[nv][0] + tp)))
    d[v][1] = d[v][0] + d1
    d[v][2] = d[v][0] + d2


x, y = 0, 0
n = int(input())
if n == 1:
    print(0)
else:
    for _ in range(n - 1):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        E[x].append((y, 0))
        E[y].append((x, 1))
    for i in range(n):
        u = [0] * 5000
        dfs(i)
        ans = min(ans, min(d[i][0], min(d[i][1], d[i][2])))
    print(ans)
