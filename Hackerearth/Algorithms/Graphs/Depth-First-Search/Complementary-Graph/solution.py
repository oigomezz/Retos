def dfs(u, g, nodes, cnt):
    nodes.remove(u)
    cnt[0] += 1
    curr = 0
    while True:
        it = next((x for x in nodes if x > curr), None)
        if it is None:
            break
        curr = it
        if curr in g[u]:
            continue
        dfs(curr, g, nodes, cnt)


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        n, m = map(int, input().split())
        g = [set() for _ in range(n + 1)]
        for _ in range(m):
            x, y = map(int, input().split())
            g[x].add(y)
            g[y].add(x)

        nodes = set(range(1, n + 1))
        cmps = []
        for i in range(1, n + 1):
            if i in nodes:
                cnt = [0]
                dfs(i, g, nodes, cnt)
                cmps.append(cnt[0])
        cmps.sort()
        print(len(cmps))
        print(" ".join(map(str, cmps)))
