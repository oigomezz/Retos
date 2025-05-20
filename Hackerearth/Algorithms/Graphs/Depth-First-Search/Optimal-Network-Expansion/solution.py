from collections import defaultdict


def dfs(node, aux):
    aux.append(node)
    vis[node] = 1
    for val in adj[node]:
        if vis[val] == 0:
            dfs(val, aux)


n, m, k = map(int, input().split())
vis = [0] * (n + 1)
adj = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

vis = [0] * (n + 1)
ans = []

for i in range(1, n + 1):
    if vis[i] == 0:
        aux = []
        dfs(i, aux)
        ans.append((len(aux), aux))

ans.sort(reverse=True, key=lambda x: x[0])
sum_result = sum(ans[i][0] for i in range(min(k + 1, len(ans))))

print(sum_result)
