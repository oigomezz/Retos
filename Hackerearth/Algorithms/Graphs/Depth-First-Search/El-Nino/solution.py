from itertools import accumulate

n, m = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
parents = list(map(int, input().strip().split()))
counter = [0 for _ in range(n + 1)]
for i in a:
    if i <= n:
        counter[i] += 1

tree = [[] for _ in range(n + 1)]
for i, v in enumerate(parents):
    tree[v].append(i + 2)

counter = list(accumulate(counter))
ans = 0
stack = [(1, 0)]
while stack:
    node, lvl = stack.pop()
    ans += counter[lvl]
    for next_node in tree[node]:
        stack.append((next_node, lvl + 1))

print(ans)
