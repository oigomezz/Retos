t = int(input())
for _ in range(t):
    grid = []
    for _ in range(3):
        grid.append(input().strip())
    if grid[1][0] == grid[2][1] == '.' or grid[0][1] == grid[1][2] == '.' or grid[1][1] == '.':
        print('YES')
    else:
        print('NO')
    # input()
