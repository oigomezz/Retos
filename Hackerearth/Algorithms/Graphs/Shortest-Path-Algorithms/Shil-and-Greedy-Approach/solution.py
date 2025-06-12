def update_dp(dp, i, k, y, x, add):
    dp[i + 1][y] = min(dp[i + 1][y], dp[i][x] + add)


def process_cell(dp, cells, color, i, j, k, ln):
    x = j * 2 + k
    cur = j ^ cells[i]
    if cur == color:
        update_dp(dp, i, k, k * 2, x, 0)
    else:
        if i + 2 <= ln:
            update_dp(dp, i, k, (1 - k) * 2, x, 1)
        if i + 3 <= ln:
            update_dp(dp, i, k, (1 - k) * 2 + 1, x, 1)


def move(cells, color):
    ln = len(cells)
    dp = [[float('inf')] * 4 for _ in range(ln + 1)]
    dp[0][0] = 0
    for i in range(ln):
        for j in (0, 1):
            for k in (0, 1):
                process_cell(dp, cells, color, i, j, k, ln)
    return min(dp[ln][0], dp[ln][2])


n = int(input())
cell_list = list(map(lambda c: 'WB'.index(
    c), input().strip().replace('0', 'W')))
print(min(move(cell_list, 0), move(cell_list, 1)))
