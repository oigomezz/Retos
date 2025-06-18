from collections import deque

MAXN = 20
MAXNODE = MAXN * MAXN * 2 + 2
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
a = []

mark = []
x = [0 for _ in range(4)]
y = [0 for _ in range(4)]
vertex, capacity, nextEdge = [], [], []


def add_edge(a, b):
    vertex.append(b)
    nextEdge.append(head[a])
    head[a] = len(capacity)
    capacity.append(1)
    vertex.append(a)
    nextEdge.append(head[b])
    head[b] = len(capacity)
    capacity.append(0)


def generate(i):
    if (i == 4):
        add_edge(source, mark[ord('a')])
        add_edge(mark[ord('a')] + n * m, mark[ord('b')])
        add_edge(mark[ord('b')] + n * m, mark[ord('c')])
        add_edge(mark[ord('c')] + n * m, mark[ord('d')])
        add_edge(mark[ord('d')] + n * m, sink)
        return

    for j in range(i - 1, i):
        for k in range(4):
            tx = x[j] + dx[k]
            ty = y[j] + dy[k]

            if (tx >= 0 and ty >= 0 and tx < n and ty < m and ord(a[tx][ty]) == ord('a') + i):
                mark[ord(a[tx][ty])] = tx * m + ty
                x[i] = tx
                y[i] = ty
                generate(i + 1)
                mark[ord(a[tx][ty])] = -1


def bfs():
    q = deque()
    pre = [-1 for _ in range(sink + 1)]
    q.appendleft(source)
    pre[source] = -2
    while (len(q) and pre[sink] == -1):
        u = q.pop()
        p = head[u]

        while (p != -1):
            if (capacity[p]):
                v = vertex[p]
                if (pre[v] == -1):
                    pre[v] = p
                    q.appendleft(v)
            p = nextEdge[p]

    if (pre[sink] == -1):
        return False

    u = sink
    while (u != source):
        p = pre[u]
        capacity[p] -= 1
        p ^= 1
        capacity[p] += 1
        u = vertex[p]
    return True


n, m = [int(x) for x in input().split()]
source = 2 * n * m
sink = source + 1
head = [-1 for _ in range(MAXNODE)]
a = []
for i in range(n):
    a.append([str(x) for x in input().split()])

for i in range(n):
    for j in range(m):
        if (a[i][j] <= 'd'):
            add_edge(i * m + j, i * m + j + n * m)

count = 0
mark = [-1 for _ in range(256)]
for i in range(n):
    for j in range(m):
        if (a[i][j] == 'a'):
            x[0] = i
            y[0] = j
            mark[ord('a')] = i * m + j
            generate(1)


flow = 0
while (bfs()):
    flow += 1
print(flow)
