from collections import deque


def bfs(con, x, d):
    q = deque()
    d[x] = 0
    q.append(x)
    while q:
        x = q.popleft()
        for y in con[x]:
            if d[y] < 0:
                d[y] = d[x] + 1
                q.append(y)


if __name__ == "__main__":
    z = int(input())
    for _ in range(z):
        n, m, x, y = map(int, input().split())
        x -= 1
        y -= 1
        r = (n - 1) * n // 2 - m
        con = [[] for _ in range(n)]
        for _ in range(m):
            s, t = map(int, input().split())
            s -= 1
            t -= 1
            con[s].append(t)
            con[t].append(s)
        dx = [-1] * n
        dy = [-1] * n
        bfs(con, x, dx)
        bfs(con, y, dy)
        d = [0] * n
        for val in dy:
            d[val] += 1
        for i in range(1, n):
            d[i] += d[i - 1]
        for i in range(n):
            temp = dx[y] - dx[i] - 2
            if temp >= 0:
                r -= d[temp]
        print(r)
