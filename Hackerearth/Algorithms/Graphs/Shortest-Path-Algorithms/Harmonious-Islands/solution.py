import heapq


def dijkstra(g, src):
    n = len(g)
    q = []
    dis = [2000000000000000000] * n
    heapq.heappush(q, (0, src))
    dis[src] = 0
    while q:
        d, f = heapq.heappop(q)
        if dis[f] != d:
            continue
        for child in g[f]:
            ch, wt = child
            if dis[f] + wt < dis[ch]:
                dis[ch] = dis[f] + wt
                heapq.heappush(q, (dis[ch], ch))
    return dis


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = [0] + [int(x) for x in input().split()]
        b = [0] + [int(x) for x in input().split()]
        g1 = [[] for _ in range(n + 1)]
        g2 = [[] for _ in range(n + 1)]
        for _ in range(m):
            a_edge, b_edge, c_edge = map(int, input().split())
            g1[a_edge].append((b_edge, c_edge))
            g1[b_edge].append((a_edge, c_edge))
        for _ in range(m):
            a_edge, b_edge, c_edge = map(int, input().split())
            g2[a_edge].append((b_edge, c_edge))
            g2[b_edge].append((a_edge, c_edge))
        x, y = map(int, input().split())
        dis1 = dijkstra(g1, x)
        dis2 = dijkstra(g2, y)
        ans = 2000000000000000000
        for i in range(1, n + 1):
            for j in range(i, n + 1, i):
                ans = min(ans, a[i] * b[j] + dis1[i] + dis2[j])
        if ans >= 2000000000000000000:
            print("-1")
        else:
            print(str(ans))
