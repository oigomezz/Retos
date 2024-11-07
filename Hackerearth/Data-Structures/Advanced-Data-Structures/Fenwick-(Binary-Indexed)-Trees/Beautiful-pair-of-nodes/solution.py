from collections import defaultdict


class OrderedSet:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)
        self.data.sort()

    def erase(self, value):
        self.data.remove(value)

    def order_of_key(self, value):
        return sum(1 for x in self.data if x < value)


graph = defaultdict(list)
visit = [False] * 2000001
index = 0
a = [0] * 2000001
b = [0] * 2000001
final_answer = 0
m = {}
BIT = [OrderedSet() for _ in range(200001)]


def remove(pos, val, node):
    while pos <= 200000:
        BIT[pos].erase((val, node))
        pos += (pos & -pos)


def add(pos, val, node):
    while pos <= 200000:
        BIT[pos].insert((val, node))
        pos += (pos & -pos)


def query(pos, val):
    global final_answer
    while pos > 0:
        final_answer += BIT[pos].order_of_key((val, 0))
        pos -= (pos & -pos)


def dfs(node):
    global index
    index += 1
    query(m[a[node]] - 1, m[b[node]])
    add(m[a[node]], m[b[node]], node)
    visit[node] = True
    for neighbor in graph[node]:
        if not visit[neighbor]:
            visit[neighbor] = True
            dfs(neighbor)
    remove(m[a[node]], m[b[node]], node)
    index -= 1


n = int(input())
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

temp = set()
line = list(map(int, input().split()))
for i in range(1, n + 1):
    a[i] = line[i-1]
    temp.add(a[i])

line = list(map(int, input().split()))
for i in range(1, n + 1):
    b[i] = line[i-1]
    temp.add(b[i])

idxs = 0
for value in temp:
    idxs += 1
    m[value] = idxs
dfs(1)
print(final_answer)
