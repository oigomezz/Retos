from collections import defaultdict

g = defaultdict(list)
A = [0] * 100012
ans = 0
M = [defaultdict(int) for _ in range(100012)]


def dfs(v, p):
    global ans
    r = v
    M[v][A[v]] += 1
    for neighbor in g[v]:
        if neighbor != p:
            x = dfs(neighbor, v)
            if len(M[r]) < len(M[x]):
                r, x = x, r
            for key, value in M[x].items():
                if A[v] % key == 0 and A[v] // key in M[r]:
                    ans += value * M[r][A[v] // key]
            for key, value in M[x].items():
                M[r][key] += value
    return r


N = int(input())
s = set()
for _ in range(N - 1):
    u, v = map(int, input().split())
    s.add((min(u, v), max(u, v)))
    g[u].append(v)
    g[v].append(u)

arr = list(map(int, input().split()))
for i in range(1, N + 1):
    A[i] = arr[i - 1]

dfs(1, 0)
print(ans)
