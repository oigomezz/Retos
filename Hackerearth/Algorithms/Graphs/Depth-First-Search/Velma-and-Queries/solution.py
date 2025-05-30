from collections import defaultdict
from bisect import bisect_left, bisect_right


def dfs(u, p, h):
    global timer, max_height
    tin[u] = timer = timer + 1
    max_height = max(max_height, h)
    heights[h].append((tin[u], weight[u]))
    for v in adj[u]:
        if v != p:
            dfs(v, u, h + 1)
    tout[u] = timer = timer + 1


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    weight = [0] + [int(x) for x in input().split()]

    adj = defaultdict(list)
    for _ in range(n - 1):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    timer = 0
    max_height = 0
    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    heights = defaultdict(list)

    dfs(1, -1, 1)

    for i in range(1, max_height + 1):
        for j in range(1, len(heights[i])):
            heights[i][j] = (heights[i][j][0], heights[i]
                             [j][1] + heights[i][j - 1][1])

    for _ in range(m):
        x, y = map(int, input().split())
        if y > max_height:
            ans = 0
        else:
            a = (tin[x], -1)
            b = (tout[x], -1)
            it1 = bisect_left(heights[y], a)
            it2 = bisect_right(heights[y], b) - 1

            ans = heights[y][it2][1]
            if it1 > 0:
                it1 -= 1
                ans -= heights[y][it1][1]

        print(str(ans))

    for i in range(1, n + 1):
        adj[i].clear()
    for i in range(1, max_height + 1):
        heights[i].clear()
