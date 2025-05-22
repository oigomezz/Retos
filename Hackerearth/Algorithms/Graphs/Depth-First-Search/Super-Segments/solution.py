dsu = [0] * 200007
p = [0] * 200007


def root(node):
    parent = dsu[node]
    if parent < 0:
        return node
    dsu[node] = root(parent)
    p[node] += p[parent]
    return dsu[node]


def join(node_u, node_v, cost):
    root_u = root(node_u)
    root_v = root(node_v)
    if root_u == root_v:
        return False
    if dsu[root_u] > dsu[root_v]:
        root_u, root_v = root_v, root_u
        node_u, node_v = node_v, node_u
        cost *= -1
    p[root_v] = p[node_u] + cost - p[node_v]
    dsu[root_u] += dsu[root_v]
    dsu[root_v] = root_u
    return True


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        n, m, q = map(int, input().split())
        for i in range(n + 7):
            dsu[i] = -1
            p[i] = 0

        for i in range(1, m + 1):
            left, right, value = map(int, input().split())
            join(left, right + 1, value)

        for i in range(1, q + 1):
            left, right = map(int, input().split())
            if root(left) != root(right + 1):
                print("-1")
            else:
                print(p[right + 1] - p[left])
