from collections import deque, defaultdict


def check_connected(x, connected, adjacency):
    stack = deque([x])
    while stack:
        u = stack.pop()
        for v in adjacency[u]:
            if v not in connected:
                connected[v] = x
                stack.append(v)


t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    equalities = defaultdict(set)
    inequalities = []
    for _ in range(k):
        x1, r, x2 = input().strip().split()
        x1 = int(x1)
        x2 = int(x2)
        if r == '=':
            equalities[x1].add(x2)
            equalities[x2].add(x1)
        else:
            inequalities.append((x1, x2))
    connected_components = {}
    for i in range(1, n + 1):
        if i not in connected_components:
            connected_components[i] = i
        check_connected(i, connected_components, equalities)
    for x1, x2 in inequalities:
        if connected_components[x1] == connected_components[x2]:
            print('NO')
            break
    else:
        print('YES')
