timer = 0


def is_ancestor(x, y):
    if x == y:
        return False
    return time_in[x] <= time_in[y] and time_out[y] <= time_out[x]


def dfs(v, p):
    global timer
    timer += 1
    time_in[v] = timer
    for u in g[v]:
        if u != p:
            dfs(u, v)
    timer += 1
    time_out[v] = timer


if __name__ == "__main__":
    n = int(input())
    q = int(input())

    g = [[] for _ in range(n)]
    for e in range(1, n):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    time_in = [0] * n
    time_out = [0] * n
    dfs(0, -1)

    for _ in range(q):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        print("YES" if is_ancestor(x, y) else "NO")
