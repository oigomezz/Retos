import heapq

n, curr = 0, 0
memo = [0] * 100005
spoilt = [0] * 1000050
D = [0] * 1000050
v = [[] for _ in range(1000050)]


def get(node, idx):
    return n + node if idx == 0 else 5 * n + node


def build_tree(idx, node, l, r):
    if l == r:
        if idx == 0:
            v[l].append((get(node, idx), 0))
        else:
            v[get(node, idx)].append((l, 0))
        return
    m = (l + r) // 2
    build_tree(idx, 2 * node, l, m)
    build_tree(idx, 2 * node + 1, m + 1, r)
    if idx == 0:
        v[get(2 * node, idx)].append((get(node, idx), 0))
        v[get(2 * node + 1, idx)].append((get(node, idx), 0))
    else:
        v[get(node, idx)].append((get(2 * node, idx), 0))
        v[get(node, idx)].append((get(2 * node + 1, idx), 0))


def edge_adder(idx, node, l, r, a, b, vertex):
    if b < l or r < a:
        return
    if a <= l and r <= b:
        if idx == 0:
            v[get(node, idx)].append((vertex, 1))
        else:
            v[vertex].append((get(node, idx), 1))
        return
    m = (l + r) // 2
    edge_adder(idx, 2 * node, l, m, a, b, vertex)
    edge_adder(idx, 2 * node + 1, m + 1, r, a, b, vertex)


def dijkstra(s):
    for i in range(curr):
        D[i] = float('inf')
    pq = []
    D[s] = 0
    heapq.heappush(pq, (0, s))
    while pq:
        node = pq[0][1]
        cost = -pq[0][0]
        heapq.heappop(pq)
        if D[node] < cost:
            continue
        for it in v[node]:
            next_node = it[0]
            d = cost + it[1]
            if spoilt[next_node]:
                continue
            if D[next_node] > d:
                D[next_node] = d
                heapq.heappush(pq, (-d, next_node))


if __name__ == "__main__":
    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
        v[a].append((b, 2))
        v[b].append((a, 2))
    build_tree(0, 1, 1, n)
    build_tree(1, 1, 1, n)
    curr = 9 * n + 1
    it = 1
    q = int(input())
    for _ in range(q):
        line = list(input().split())
        t = int(line[0])
        if t == 1:
            a = int(line[1])
            b = int(line[2])
            edge_adder(0, 1, 1, n, a, b, curr)
            edge_adder(1, 1, 1, n, a, b, curr)
            memo[it] = curr
            it += 1
            curr += 1
        elif t == 2:
            a = int(line[1])
            spoilt[memo[a]] = 1
        elif t == 3:
            a = int(line[1])
            b = int(line[2])
            dijkstra(a)
            print(-1 if D[b] == float('inf') else D[b] // 2)
