test_cases = int(input())

for _ in range(test_cases):
    size = int(input())

    grid = []
    x, y = -1, -1

    for i in range(size):
        row = input().strip()
        grid.append(row)
        for j in range(size):
            if grid[i][j] == '*':
                x = i
                y = j

    position = size // 2

    if x <= position and y <= position:
        print((position - x) + (position - y))
    elif x >= position and y <= position:
        print((x - position) + (position - y))
    elif x <= position and y >= position:
        print((position - x) + (y - position))
    elif x >= position and y >= position:
        print((x - position) + (y - position))
