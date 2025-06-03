from collections import defaultdict

MOD = 1000000007


def find_regions(u, w, weights, adjacency, seen):
    seen[u] = True
    result = 1
    for v in adjacency[u]:
        if not seen[v] and weights[v] >= w:
            result *= 1 + find_regions(v, w, weights, adjacency, seen)
    return result % MOD


n = int(input())
weights = list(map(int, input().strip().split()))
edges = defaultdict(list)
for _ in range(n - 1):
    x, y = map(lambda z: int(z) - 1, input().strip().split())
    edges[x].append(y)
    edges[y].append(x)

q = int(input())
for _ in range(q):
    k = int(input())
    visited = [False] * n
    ans = 0
    for i in range(n):
        if weights[i] == k:
            ans += find_regions(i, k, weights, edges, visited.copy())
            visited[i] = True
    print(ans % MOD)
