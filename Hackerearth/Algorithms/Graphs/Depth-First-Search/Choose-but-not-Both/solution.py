n = 0
a = [0] * 300001
ans = 0
vis = [False] * 300001
dem = [0] * 300001


def dfs(node, parent):
    global ans
    if vis[node]:
        return
    vis[node] = True
    if parent == 1:
        ans += 1
    dem[a[node]] -= 1
    if dem[a[node]] == 0 or parent == 1:
        dfs(a[node], parent ^ 1)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        a[i] = arr[i - 1]
        dem[a[i]] += 1
    for i in range(1, n + 1):
        if dem[i] == 0:
            dfs(i, 1)
    for i in range(1, n + 1):
        if not vis[i]:
            dfs(i, 0)
    print(ans)
