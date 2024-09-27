def max_plants_in_row(width, broken):
    count = 0
    last_planted = False
    for i in range(width):
        if not broken[i] and not last_planted:
            count += 1
            last_planted = True
        else:
            last_planted = False
    return count


def calculate_max_plants(rows, cols, pots):
    total = 0
    for i in range(rows):
        total += max_plants_in_row(cols,  pots[i])
    return total


def calculate_min_coverage(rows, cols, pots):
    min_coverage = 0
    for j in range(cols):
        has_plant = False
        for i in range(rows):
            if not pots[i][j]:
                has_plant = True
                break
        if has_plant:
            min_coverage += 1
    return min_coverage


rows, cols = map(int, input().split())
broken_pots = int(input())
pots = [[False for _ in range(cols)] for _ in range(rows)]
for _ in range(broken_pots):
    row, col = map(int, input().split())
    pots[row][col] = 1

max_plants = calculate_max_plants(rows, cols, pots)
min_coverage = calculate_min_coverage(rows, cols, pots)
print(max_plants, min_coverage)
