from collections import deque


def check_pos(pos_x, pos_y):
    return 1 <= pos_x <= n and 1 <= pos_y <= m


directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
lex_directions = 'DLRU'
matrix = []

n, m = map(int, input().strip().split())
for _ in range(n):
    matrix.append(input().strip())

q = int(input())
for _ in range(q):
    sx, sy, fx, fy = map(int, input().strip().split())
    visited = set()
    parents = {}
    to_visit = deque([(sx, sy)])
    visited.add((sx, sy))
    while to_visit:
        pos_x, pos_y = to_visit.popleft()
        if not check_pos(pos_x, pos_y):
            continue
        if matrix[pos_x-1][pos_y-1] == '#':
            continue
        for direction in lex_directions:
            dx, dy = directions[direction]
            if (pos_x + dx, pos_y + dy) in visited:
                continue
            to_visit.append((pos_x + dx, pos_y + dy))
            visited.add((pos_x + dx, pos_y + dy))
            parents[(pos_x + dx, pos_y + dy)] = (pos_x, pos_y, direction)
    if (fx, fy) in visited:
        path = []
        pos_x = fx
        pos_y = fy
        while not (pos_x == sx and pos_y == sy):
            par_pos_x, par_pos_y, direction = parents[(pos_x, pos_y)]
            path.append(direction)
            pos_x = par_pos_x
            pos_y = par_pos_y
        print(''.join(path[::-1]))
    else:
        print("Impossible")
