from collections import defaultdict
import bisect

graph = defaultdict(list)
in_values = defaultdict(list)
in_time = {}
out_time = {}
timer = 0


def dfs(vertex, parent=0):
    global timer
    in_time[vertex] = timer + 1
    timer += 1
    for neighbor in graph[vertex]:
        if neighbor != parent:
            dfs(neighbor, vertex)
    out_time[vertex] = timer + 1
    timer += 1
    for neighbor in graph[vertex]:
        if neighbor != parent:
            in_values[vertex].append(in_time[neighbor])


def is_ancestor(ancestor, descendant):
    return in_time[ancestor] <= in_time[descendant] and out_time[ancestor] >= out_time[descendant]


n, q = map(int, input().split())
for _ in range(2, n + 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

timer = 0
dfs(1)
while q > 0:
    x, k = map(int, input().split())
    answer = k * (k - 1) // 2
    count = defaultdict(int)
    line = list(map(int, input().split()))
    for _ in range(k):
        node = line[_]
        if node == x:
            continue
        if is_ancestor(x, node):
            subtree = bisect.bisect_right(in_values[x], in_time[node])
            count[subtree] += 1
        else:
            count[n + 1] += 1
    for u in count.values():
        answer -= u * (u - 1) // 2
    print(answer)
    q -= 1
