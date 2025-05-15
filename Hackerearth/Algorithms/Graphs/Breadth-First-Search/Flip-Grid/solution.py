from collections import deque


def rotate_clockwise(grid):
    res = grid[:]
    for i in range(4):
        for j in range(4):
            res[j] = res[j][:4 - i - 1] + grid[i][j] + res[j][4 - i:]
    return res


def flip_row(grid, row):
    res = grid[:]
    res[row] = ''.join('0' if c == '1' else '1' for c in grid[row])
    return res


def flip_col(grid, col):
    res = grid[:]
    for i in range(4):
        res[i] = res[i][:col] + ('0' if grid[i][col] ==
                                 '1' else '1') + res[i][col + 1:]
    return res


if __name__ == "__main__":
    gridA = [input().strip() for _ in range(4)]
    gridB = [input().strip() for _ in range(4)]

    vis = {}
    dist = {}
    q = deque()

    q.append(gridA)
    vis[tuple(gridA)] = True
    dist[tuple(gridA)] = 0

    while q:
        grid = q.popleft()
        op1 = rotate_clockwise(grid)
        if tuple(op1) not in vis:
            dist[tuple(op1)] = dist[tuple(grid)] + 1
            vis[tuple(op1)] = True
            q.append(op1)

        for i in range(4):
            op2 = flip_row(grid, i)
            op3 = flip_col(grid, i)
            if tuple(op2) not in vis:
                dist[tuple(op2)] = dist[tuple(grid)] + 1
                vis[tuple(op2)] = True
                q.append(op2)
            if tuple(op3) not in vis:
                dist[tuple(op3)] = dist[tuple(grid)] + 1
                vis[tuple(op3)] = True
                q.append(op3)

    if tuple(gridB) not in vis:
        print("-1")
    else:
        print(dist[tuple(gridB)])
