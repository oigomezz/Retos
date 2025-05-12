from collections import defaultdict
import heapq

zero = 1001
black = 0
white = 1


def dijkstra(source, n, g, control):
    dp = [[-1] * 2005 for _ in range(1005)]
    s = []
    index = zero - 1 if control[source] == black else zero + 1
    dp[source][index] = 0
    heapq.heappush(s, (0, (source, index)))

    while s:
        u, dif = heapq.heappop(s)[1]
        for v, w in g[u]:
            ind = dif - 1 if control[v] == black else dif + 1
            if dp[v][ind] == -1 or dp[v][ind] > dp[u][dif] + w:
                if dp[v][ind] != -1:
                    s.remove((dp[v][ind], (v, ind)))
                    heapq.heapify(s)
                dp[v][ind] = dp[u][dif] + w
                heapq.heappush(s, (dp[v][ind], (v, ind)))

    ans = float('inf')
    for i in range(-1, 2):
        if dp[n][zero + i] != -1:
            ans = min(ans, dp[n][zero + i])
    return ans


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = defaultdict(list)
    for _ in range(m):
        u, v, l = map(int, input().split())
        g[u].append((v, l))
    control = [0] * (n + 1)
    line = list(map(int, input().split()))
    for i in range(1, n + 1):
        control[i] = line[i - 1]
    ans = dijkstra(1, n, g, control)
    if ans == float('inf'):
        ans = -1
    print(ans)
