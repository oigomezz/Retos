from collections import defaultdict, deque


def find_coin(start, adjacency, seen, bananas):
    stack = deque([start])
    seen[start] = True
    res = 0
    while stack:
        vertex = stack.pop()
        res += bananas[vertex]
        for neighbour in adjacency[vertex]:
            if not seen[neighbour]:
                stack.append(neighbour)
                seen[neighbour] = True
    return res


t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    rituals = defaultdict(list)
    for _ in range(m):
        x, y = map(int, input().strip().split())
        x -= 1
        y -= 1
        rituals[x].append(y)
        rituals[y].append(x)
    a = list(map(int, input().strip().split()))
    visited = [False] * n
    ans = 0
    for i in range(n):
        if not visited[i]:
            ans = max(ans, find_coin(i, rituals, visited, a))
    print(ans)
