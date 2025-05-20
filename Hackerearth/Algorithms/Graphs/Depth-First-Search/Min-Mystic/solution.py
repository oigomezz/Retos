from collections import defaultdict


def dfs(u, p):
    for v, w in tree[u]:
        if v == p:
            continue
        dfs(v, u)
        vals[u][1] += w * children[v][0] + vals[v][0]
        vals[u][2] += w * children[v][1] + vals[v][1]
        vals[u][0] += w * children[v][2] + vals[v][2]
        children[u][1] += children[v][0]
        children[u][2] += children[v][1]
        children[u][0] += children[v][2]
    children[u][0] += 1


def dfs2(u, p):
    global ans
    ans = min(ans, vals[u][1] + vals[u][2] * 2)
    for v, w in tree[u]:
        if v == p:
            continue
        vals[u][1] -= w * children[v][0] + vals[v][0]
        vals[u][2] -= w * children[v][1] + vals[v][1]
        vals[u][0] -= w * children[v][2] + vals[v][2]
        children[u][1] -= children[v][0]
        children[u][2] -= children[v][1]
        children[u][0] -= children[v][2]
        vals[v][1] += w * children[u][0] + vals[u][0]
        vals[v][2] += w * children[u][1] + vals[u][1]
        vals[v][0] += w * children[u][2] + vals[u][2]
        children[v][1] += children[u][0]
        children[v][2] += children[u][1]
        children[v][0] += children[u][2]
        dfs2(v, u)
        children[v][1] -= children[u][0]
        children[v][2] -= children[u][1]
        children[v][0] -= children[u][2]
        vals[v][1] -= w * children[u][0] + vals[u][0]
        vals[v][2] -= w * children[u][1] + vals[u][1]
        vals[v][0] -= w * children[u][2] + vals[u][2]
        children[u][1] += children[v][0]
        children[u][2] += children[v][1]
        children[u][0] += children[v][2]
        vals[u][1] += w * children[v][0] + vals[v][0]
        vals[u][2] += w * children[v][1] + vals[v][1]
        vals[u][0] += w * children[v][2] + vals[v][2]


if __name__ == "__main__":
    totalN = 0
    test = int(input())
    for _ in range(test):
        N = int(input())
        totalN += N
        tree = defaultdict(list)
        for _ in range(N - 1):
            u, v, w = map(int, input().split())
            u -= 1
            v -= 1
            tree[u].append((v, w))
            tree[v].append((u, w))

        vals = [[0] * 3 for _ in range(N)]
        children = [[0] * 3 for _ in range(N)]

        dfs(0, -1)
        ans = 2 * 10**18

        dfs2(0, -1)
        print(ans)
