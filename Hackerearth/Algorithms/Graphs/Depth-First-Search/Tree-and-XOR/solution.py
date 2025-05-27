graph = [[] for _ in range(200005)]
val = [0] * 200005
in_time = [0] * 200005
out_time = [0] * 200005
ticks = 0
MAP = [0] * 400005
trie = [[0, 0] for _ in range(12400000)]
nn = 0
root = [[0] * 400005 for _ in range(2)]
sum_value = 0


def insert(value, previous):
    global nn
    ret = nn + 1
    nn += 1
    t = ret
    for i in range(29, -1, -1):
        bit = (value & (1 << i)) != 0
        trie[t][0] = trie[previous][0]
        trie[t][1] = trie[previous][1]
        trie[t][bit] = nn + 1
        nn += 1
        t = trie[t][bit]
        previous = trie[previous][bit]
    return ret


def search(t, value):
    ans = 0
    for i in range(29, -1, -1):
        bit = (value & (1 << i)) != 0
        if trie[t][1 - bit]:
            ans |= (1 << i)
            t = trie[t][1 - bit]
        else:
            t = trie[t][bit]
    return ans


def dfs(node, parent):
    global ticks
    in_time[node] = ticks + 1
    ticks += 1
    MAP[ticks] = node
    ret = val[node]
    for neighbor in graph[node]:
        if neighbor != parent:
            ret ^= dfs(neighbor, node)
    val[node] = ret
    out_time[node] = ticks + 1
    ticks += 1
    MAP[ticks] = node
    return ret


def dfs1(node, parent, max_value):
    global sum_value
    if node != 1:
        ans = max_value
        ans = max(ans, search(root[0][in_time[node] - 1], val[node]))
        ans = max(ans, search(root[1][out_time[node] + 1], val[node]))
        sum_value += ans
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs1(neighbor, node, max(val[node], max_value))


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, N + 1):
        val[i] = arr[i - 1]
    for i in range(1, N):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dfs(1, 0)

    for i in range(1, ticks + 1):
        if out_time[MAP[i]] == i:
            root[0][i] = insert(val[MAP[i]], root[0][i - 1])
        else:
            root[0][i] = root[0][i - 1]

    for i in range(ticks, 0, -1):
        if in_time[MAP[i]] == i:
            root[1][i] = insert(val[MAP[i]], root[1][i + 1])
        else:
            root[1][i] = root[1][i + 1]

    dfs1(1, 0, 0)
    print(sum_value)
