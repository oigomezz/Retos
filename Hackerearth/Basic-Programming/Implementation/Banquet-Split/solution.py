from collections import defaultdict

graph = defaultdict(list)
n = 0
height = [0] * 1000000
up = [[0] * 21 for _ in range(1000000)]
tin = [0] * 1000000
tout = [0] * 1000000
timer = 0
l = 0


def dfs(node, parent=0, h=0):
    global timer
    tin[node] = timer + 1
    timer += 1
    up[node][0] = parent
    height[node] = h
    h += 1
    for i in range(1, l + 1):
        up[node][i] = up[up[node][i - 1]][i - 1]
    for child in graph[node]:
        if child != parent:
            dfs(child, node, h)
    tout[node] = timer + 1
    timer += 1


def upper(a, b):
    return tin[a] <= tin[b] and tout[a] >= tout[b]


def lca(a, b):
    for i in range(l, -1, -1):
        if not upper(up[a][i], b):
            a = up[a][i]
    return up[a][0]


t = int(input())
for _ in range(t):
    n = int(input())
    graph.clear()
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    timer = 0
    l = 1
    while (1 << l) <= n:
        l += 1
    dfs(0)
    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        if (height[u] & 1) != (height[v] & 1):
            print("Yes")
        else:
            print("No")
            print("1 ", end="")
            if height[u] > height[v]:
                u, v = v, u
            if upper(u, v):
                print(height[v] - height[u] + 1)
            else:
                h = height[lca(u, v)] * 2
                print(height[u] + height[v] - h + 1)
