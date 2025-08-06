dp = [[[[[0 for _ in range(128)] for _ in range(128)]
        for _ in range(7)] for _ in range(7)] for _ in range(25)]


def difference(in_mask: int, ex_mask: int, row: int, col: int, introvert: bool, position: int) -> int:
    neighbor = 0
    count = 0
    row = position // col
    col = position % col
    if row > 0:
        up_position = col - 1
        if in_mask & (1 << up_position) or ex_mask & (1 << up_position):
            if in_mask & (1 << up_position):
                count += 1
                neighbor -= 90
            else:
                count += 1
                neighbor += 60
    if col > 0:
        left_position = 0
        if in_mask & (1 << left_position) or ex_mask & (1 << left_position):
            if in_mask & (1 << left_position):
                count += 1
                neighbor -= 90
            else:
                count += 1
                neighbor += 60
    return (-90 * count if introvert else 60 * count) + neighbor


def recursive(pos: int, introverts: int, extroverts: int, in_mask: int, ex_mask: int, row: int, col: int) -> int:
    new_in_mask = (in_mask << 1) & 63
    new_ex_mask = (ex_mask << 1) & 63
    if pos == (row * col):
        return 0
    if dp[pos][introverts][extroverts][in_mask][ex_mask] != -1:
        return dp[pos][introverts][extroverts][in_mask][ex_mask]

    option_a = recursive(pos + 1, introverts, extroverts,
                         new_in_mask, new_ex_mask, row, col)
    option_b = 0
    option_c = 0

    if introverts > 0:
        option_b = 360 + recursive(pos + 1, introverts - 1,
                                   extroverts, new_in_mask + 1, new_ex_mask, row, col)
        penalty = difference(in_mask, ex_mask, row, col, True, pos)
        option_b += penalty

    if extroverts > 0:
        penalty = difference(in_mask, ex_mask, row, col, False, pos)
        option_c = 120 + recursive(pos + 1, introverts, extroverts - 1,
                                   new_in_mask, new_ex_mask + 1, row, col) + penalty

    dp[pos][introverts][extroverts][in_mask][ex_mask] = max(
        option_a, option_b, option_c)
    return dp[pos][introverts][extroverts][in_mask][ex_mask]


if __name__ == "__main__":
    n, m, x, y = map(int, input().split())
    for i in range(25):
        for j in range(7):
            for k in range(7):
                for l in range(128):
                    for p in range(128):
                        dp[i][j][k][l][p] = -1

    print(recursive(0, x, y, 0, 0, m, n))
