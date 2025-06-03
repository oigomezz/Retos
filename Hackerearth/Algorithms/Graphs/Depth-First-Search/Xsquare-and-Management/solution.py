from collections import deque

INF = 1000000000
M = 1000000007

v = [[] for _ in range(500005)]
dis = [[-1] * 500005 for _ in range(2)]
d = [-1] * 500005
fin = []


def dfs(st):
    q = deque()
    comp = []
    q.append(st)
    comp.append(st)
    d[st] = 0
    while q:
        f = q.popleft()
        for neighbor in v[f]:
            if d[neighbor] == -1:
                d[neighbor] = d[f] + 1
                q.append(neighbor)
                comp.append(neighbor)
    fin.append(comp)
    fs, sc, val = -1, -1, -1
    for node in comp:
        if d[node] > val:
            val = d[node]
            fs = node
    for node in comp:
        d[node] = -1
    q.append(fs)
    d[fs] = 0
    while q:
        f = q.popleft()
        for neighbor in v[f]:
            if d[neighbor] == -1:
                d[neighbor] = d[f] + 1
                q.append(neighbor)
    val = -1
    for node in comp:
        if d[node] > val:
            val = d[node]
            sc = node
    q.append(fs)
    dis[0][fs] = 0
    while q:
        f = q.popleft()
        for neighbor in v[f]:
            if dis[0][neighbor] == -1:
                dis[0][neighbor] = dis[0][f] + 1
                q.append(neighbor)
    q.append(sc)
    dis[1][sc] = 0
    while q:
        f = q.popleft()
        for neighbor in v[f]:
            if dis[1][neighbor] == -1:
                dis[1][neighbor] = dis[1][f] + 1
                q.append(neighbor)


if __name__ == "__main__":
    t = int(input())
    assert 1 <= t <= 100000
    for _ in range(t):
        n, m = map(int, input().split())
        assert 1 <= n <= 500005
        assert 1 <= m <= 500005
        fin.clear()
        for i in range(1, n + 1):
            v[i].clear()
            dis[0][i] = dis[1][i] = d[i] = -1
        for _ in range(m):
            x, y = map(int, input().split())
            assert 1 <= x <= n
            assert 1 <= y <= n
            v[x].append(y)
            v[y].append(x)
        for i in range(1, n + 1):
            if dis[0][i] == -1 or dis[1][i] == -1:
                dfs(i)
        ans = 0
        for component in fin:
            mn = INF
            for vert in component:
                mn = min(mn, max(dis[0][vert], dis[1][vert]))
            ans = max(ans, mn)
        val = 1
        for component in fin:
            cntt = 0
            for vert in component:
                if max(dis[0][vert], dis[1][vert]) <= ans:
                    cntt += 1
            val = (val * cntt) % M
        print(val)
