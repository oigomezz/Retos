cost = [0] * 100005
adj = [[] for _ in range(100005)]
tree = [[] for _ in range(4000020)]
start = [0] * 100005
end_ = [0] * 100005
time_ = [0] * 100005
vis = [0] * 100005
k = 0


def dfs(source):
    global k
    vis[source] = 1
    k += 1
    time_[k] = source
    start[source] = k
    for neighbor in adj[source]:
        if not vis[neighbor]:
            dfs(neighbor)
    end_[source] = k


def build(node, left, right):
    if left > right:
        return
    if left == right:
        tree[node].append(cost[time_[left]])
        return
    mid = left + (right - left) // 2
    build(2 * node, left, mid)
    build(2 * node + 1, mid + 1, right)
    tree[node] = sorted(tree[2 * node] + tree[2 * node + 1])


def query(node, left, right, k, start_range, end_range):
    if start_range > right or end_range < left:
        return 0
    if start_range >= left and end_range <= right:
        if len(tree[node]) == 0:
            return 0
        pos = next((i for i, value in enumerate(
            tree[node]) if value >= k), len(tree[node]))
        return len(tree[node]) - pos
    mid = (end_range + start_range) // 2
    t1 = query(2 * node, left, right, k, start_range, mid)
    t2 = query(2 * node + 1, left, right, k, mid + 1, end_range)
    return t1 + t2


if __name__ == "__main__":
    n, q, d = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        cost[i] = arr[i - 1]
        vis[i] = 0
    for i in range(1, n):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    dfs(d)
    build(1, 1, n)
    last = 0
    for _ in range(q):
        line = list(map(int, input().split()))
        r = line[0] ^ last
        x = line[1] ^ last
        y = line[2] ^ last
        last = query(1, start[r] + 1, end_[r], x - cost[r] - cost[d], 1, n) - \
            query(1, start[r] + 1, end_[r], y - cost[r] - cost[d] + 1, 1, n)
        print(last)
