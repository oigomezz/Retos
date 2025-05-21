from collections import defaultdict

n, q = map(int, input().split())
colors = list(map(int, input().split()))
graph = defaultdict(set)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u - 1].add(v - 1)
    graph[v - 1].add(u - 1)

stack = [(0, -1)]
order = []
parent = {}
while len(stack) > 0:
    curr, prev = stack.pop()
    order.append(curr)
    for j in graph[curr]:
        if j != prev:
            parent[j] = curr
            stack.append((j, curr))

order.reverse()
qlist = list(map(int, input().split()))
ctr = [0] * n
for q in qlist:
    q -= 1
    ctr[q] += 1

for node in order:
    if node in parent:
        ctr[parent[node]] += ctr[node]

res = 0
for i in range(n):
    curr = colors[i]
    if ctr[i] & 1:
        curr = 1 - curr
    if curr == 1:
        res += 1

print(res)
