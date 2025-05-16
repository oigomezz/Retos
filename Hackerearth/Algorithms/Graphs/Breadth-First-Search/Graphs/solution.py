from collections import deque, defaultdict


def bfs(r, a):
    vis = {}
    vis[r] = 1
    ans = 1
    q = deque([r])
    while q:
        k = q.popleft()
        for child in a[k]:
            if child not in vis:
                vis[child] = vis[k] + 1
                q.append(child)
                ans = max(ans, vis[k] + 1)
    return ans


if __name__ == "__main__":
    n, m, f = map(int, input().split())
    a = defaultdict(list)
    vis = [0] * (n + 1)
    for _ in range(m):
        x, y = map(int, input().split())
        a[x].append(y)
        a[y].append(x)

    d = 0
    for i in range(1, n + 1):
        if vis[i] == 0:
            vis[i] = 1
            q = deque([i])
            la = 0
            rn = i
            while q:
                k = q.popleft()
                for child in a[k]:
                    if child > 0 and vis[child] == 0:
                        vis[child] = vis[k] + 1
                        q.append(child)
                        if vis[child] > la:
                            la = vis[child]
                            rn = child
                if vis[k] > la:
                    la = vis[k]
                    rn = k
            d = max(d, bfs(rn, a))

    print((d + f - 1) // f)
