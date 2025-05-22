from collections import defaultdict


def move(adjacency, u=0, parent=-1):
    res = 0
    for v in adjacency[u]:
        if v != parent:
            temp = move(adjacency, v, u)
            if temp == -1:
                return temp
            res += temp == 0
    return res if res in (0, 1) else -1


t = int(input())
for _ in range(t):
    n = int(input())
    cities = defaultdict(list)
    for _ in range(n - 1):
        x, y = map(int, input().strip().split())
        x -= 1
        y -= 1
        cities[x].append(y)
        cities[y].append(x)
    print('UNSAFE' if move(cities) == 1 else 'SAFE')
