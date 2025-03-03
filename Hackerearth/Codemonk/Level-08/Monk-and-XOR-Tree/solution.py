from collections import defaultdict

ans = 0
ha = [0] * 10000000
a = [0] * 100005
k = 0
v = defaultdict(list)


def dfs(r, xo):
    global ans
    xo ^= a[r]
    ans += ha[xo ^ k]
    ha[xo] += 1
    for child in v[r]:
        dfs(child, xo)
    ha[xo] -= 1


n, k = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(1, n + 1):
    a[i] = int(arr[i - 1])

ha[0] = 1
arr = list(map(int, input().split()))
for i in range(1, n):
    x = int(arr[i - 1])
    v[x].append(i + 1)

dfs(1, 0)
print(ans)
