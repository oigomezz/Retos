import heapq
import sys

vis = [[0] * 151 for _ in range(151)]
rr = [0, 0, 1, -1]
cc = [1, -1, 0, 0]


class Cou:
    def __init__(self, f, s, t):
        self.f = f
        self.s = s
        self.t = t

    def __lt__(self, other):
        return self.t < other.t


def dijkstra(sx, sy, v, t):
    q = []
    heapq.heappush(q, Cou(sx, sy, t))
    res = 0
    n = len(v)
    global vis
    vis = [[0] * 151 for _ in range(151)]

    while q:
        current = heapq.heappop(q)
        f, s, t = current.f, current.s, current.t

        if vis[f][s]:
            continue
        vis[f][s] = 1
        res = max(res, (max(sx, f) + 1) * (max(sy, s) + 1))

        for h in range(4):
            xx = f + rr[h]
            yy = s + cc[h]
            if 0 <= xx < n and 0 <= yy < n and t - v[xx][yy] >= 0 and vis[xx][yy] == 0:
                heapq.heappush(q, Cou(xx, yy, t - v[xx][yy]))
    return res


def main():
    n, t = map(int, input().strip().split())
    v = []
    rem = [[0] * n for _ in range(n)]

    for h in range(n):
        row = list(map(int, input().strip().split()))
        v.append(row)

    q = []
    heapq.heappush(q, Cou(0, 0, t))

    while q:
        current = heapq.heappop(q)
        f, s, t = current.f, current.s, current.t

        if vis[f][s]:
            continue
        vis[f][s] = 1

        for h in range(4):
            x = f + rr[h]
            y = s + cc[h]
            if 0 <= x < n and 0 <= y < n and vis[x][y] == 0 and t - v[x][y] >= 0:
                heapq.heappush(q, Cou(x, y, t - v[x][y]))

        rem[f][s] = t

    if rem[n - 1][n - 1]:
        print(n * n)
        sys.exit(0)

    ans = 0
    for h in range(n):
        for j in range(n):
            if rem[h][j]:
                ans = max(ans, dijkstra(h, j, v, rem[h][j]))
                if ans == n * n:
                    print(ans)
                    sys.exit(0)

    print(ans)


if __name__ == "__main__":
    main()
