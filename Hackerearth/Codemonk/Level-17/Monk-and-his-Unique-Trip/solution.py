graph = []
lowlink = []
pre = []
cp = []
onStack = []
visited = []
dp = []
st = []
timer = 0
componentno = 0
ans = 0


def sccdfs(node, sccgraph, sccvisited):
    global dp
    if sccvisited[node]:
        return dp[node]
    ans = 0
    sccvisited[node] = True
    for child in sccgraph[node]:
        ans = max(ans, 1 + sccdfs(child, sccgraph, sccvisited))
    dp[node] = ans
    return ans


def dfs(node):
    global timer, componentno
    st.append(node)
    pre[node] = lowlink[node] = timer + 1
    onStack[node] = visited[node] = True
    for child in graph[node]:
        if not visited[child]:
            dfs(child)
            lowlink[node] = min(lowlink[child], lowlink[node])
        elif onStack[child]:
            lowlink[node] = min(lowlink[child], lowlink[node])
    if lowlink[node] == pre[node]:
        while True:
            x = st.pop()
            cp[x] = componentno
            onStack[x] = False
            if x == node:
                break
        componentno += 1


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    pre = [0] * N
    lowlink = [0] * N
    visited = [False] * N
    onStack = [False] * N
    cp = [-1] * N
    edges = []

    for _ in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        graph[x].append(y)
        edges.append((x, y))

    for i in range(N):
        if not visited[i]:
            dfs(i)

    sccgraph = [[] for _ in range(componentno)]
    for x, y in edges:
        if cp[x] != cp[y]:
            sccgraph[cp[x]].append(cp[y])

    sccvisited = [False] * componentno
    dp = [0] * componentno
    for i in range(componentno):
        if not sccvisited[i]:
            ans = max(ans, sccdfs(i, sccgraph, sccvisited))

    print(ans)
