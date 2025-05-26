from collections import defaultdict

adj = defaultdict(list)
av = defaultdict(list)
h = [0] * 500010
par = [[-1] * 500010 for _ in range(20)]


def dfs(vertex):
    for i in range(1, 20):
        if par[i - 1][vertex] != -1:
            par[i][vertex] = par[i - 1][par[i - 1][vertex]]
    for neighbor in adj[vertex]:
        if neighbor != par[0][vertex]:
            h[neighbor] = h[vertex] + 1
            par[0][neighbor] = vertex
            dfs(neighbor)


def lca(a, b):
    if h[a] < h[b]:
        a, b = b, a
    depth_diff = h[a] - h[b]
    for i in range(20):
        if (depth_diff >> i) & 1:
            a = par[i][a]
    if a == b:
        return a
    for i in range(19, -1, -1):
        if par[i][a] != par[i][b]:
            a = par[i][a]
            b = par[i][b]
    return par[0][a]


if __name__ == "__main__":
    n, q = map(int, input().split())

    diam1 = [0] * 500010
    diam2 = [0] * 500010

    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        color = arr[i - 1]
        av[color].append(i)

    for _ in range(n - 1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    dfs(1)

    for i in range(1, 500010):
        if av[i]:
            vertex = av[i][0]
            farthest_vertex = av[i][0]
            max_distance = 0

            for u in av[i]:
                distance = h[vertex] + h[u] - 2 * h[lca(u, vertex)]
                if max_distance < distance:
                    farthest_vertex = u
                    max_distance = distance

            vertex = farthest_vertex
            farthest_vertex = av[i][0]
            max_distance = 0

            for u in av[i]:
                distance = h[vertex] + h[u] - 2 * h[lca(u, vertex)]
                if max_distance < distance:
                    farthest_vertex = u
                    max_distance = distance

            diam1[i] = vertex
            diam2[i] = farthest_vertex

    output = []
    for _ in range(q):
        vertex, color = map(int, input().split())
        if not av[color]:
            output.append("-1")
        else:
            distance1 = h[vertex] + h[diam1[color]] - \
                2 * h[lca(diam1[color], vertex)]
            distance2 = h[vertex] + h[diam2[color]] - \
                2 * h[lca(diam2[color], vertex)]
            output.append(str(max(distance1, distance2)))

    print("\n".join(output))
