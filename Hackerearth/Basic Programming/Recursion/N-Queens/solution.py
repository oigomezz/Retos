n = int(input())
grid = [[False] * 10 for _ in range(10)]


def is_safe(row, col):
    for i in range(row):
        if grid[i][col]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if grid[i][j]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if grid[i][j]:
            return False
    return True


def solve_queen(row):
    if row >= n:
        return True
    for col in range(n):
        if is_safe(row, col):
            grid[row][col] = True
            if solve_queen(row + 1):
                return True
            grid[row][col] = False
    return False


if solve_queen(0):
    for i in range(n):
        print(" ".join(str(int(grid[i][j])) for j in range(n)))
else:
    print("Not possible")
