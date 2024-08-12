T = int(input())
for _ in range(T):
    N = int(input())
    grid = [list(input().strip()) for _ in range(N)]

    total_cherries = sum(row.count('#') for row in grid)
    if total_cherries % 2 != 0:
        print("NO")
        continue

    cherries_needed = total_cherries // 2
    cherries_count = 0
    can_divide = False

    for i in range(N):
        cherries_count += grid[i].count('#')
        if cherries_count == cherries_needed:
            can_divide = True
            break

    cherries_count = 0
    if not can_divide:
        for i in range(N):
            for j in range(N):
                if grid[j][i] == '#':
                    cherries_count += 1

            if cherries_count == cherries_needed:
                can_divide = True
                break

    print("YES" if can_divide else "NO")
