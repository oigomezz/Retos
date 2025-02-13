def update(x, y, z, val):
    global global_n
    i = x
    while i <= global_n:
        j = y
        while j <= global_n:
            k = z
            while k <= global_n:
                dp[i][j][k] += val
                k += k & -k
            j += j & -j
        i += i & -i


def query(x, y, z):
    ret = 0
    i = x
    while i > 0:
        j = y
        while j > 0:
            k = z
            while k > 0:
                ret += dp[i][j][k]
                k -= k & -k
            j -= j & -j
        i -= i & -i
    return ret


global_n = 0
dp = []

n, q = map(int, input().strip().split())
total_players = 0
n += 1
global_n = n
dp = [[[0] * (n + 2) for _ in range(n + 2)] for _ in range(n + 2)]

while q > 0:
    q -= 1
    type_query, *line = map(int, input().strip().split())
    if type_query == 1:
        x, y, z, val = line
        x += 1
        y += 1
        z += 1
        total_players += val
        update(x, y, z, val)
    else:
        x0, y0, z0, x, y, z = line
        x0 += 1
        y0 += 1
        z0 += 1
        x += 1
        y += 1
        z += 1

        value1 = query(x, y, z) - query(x0 - 1, y, z) - \
            query(x, y0 - 1, z) + query(x0 - 1, y0 - 1, z)
        value2 = query(x, y, z0 - 1) - query(x0 - 1, y, z0 - 1) - \
            query(x, y0 - 1, z0 - 1) + query(x0 - 1, y0 - 1, z0 - 1)
        final_answer = total_players - (value1 - value2)
        print(final_answer)
