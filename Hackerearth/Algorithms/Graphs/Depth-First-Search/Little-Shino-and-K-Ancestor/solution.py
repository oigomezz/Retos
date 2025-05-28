from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)


def find(u, closest, adjacency, colors, seen, res, groups=None):
    if groups is None:
        groups = defaultdict(list)
    seen[u] = True
    if len(groups[colors[u]]) >= closest:
        res[u] = groups[colors[u]][-closest] + 1
    groups[colors[u]].append(u)
    for v in adjacency[u]:
        if not seen[v]:
            find(v, closest, adjacency, colors, seen, res, groups)
    groups[colors[u]].pop()


n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    x, y = map(lambda i: int(i) - 1, input().split())
    tree[x].append(y)
    tree[y].append(x)
ans = [-1] * n
find(0, k, tree, a, [False] * n, ans)
print(' '.join(map(str, ans)))
