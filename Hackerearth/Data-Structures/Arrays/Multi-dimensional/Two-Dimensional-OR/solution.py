n, m = map(int, input().split())
grid = []
for i in range(n):
    row = []
    for x in input().split():
        row.append(int(x))
    grid.append(row)

pref = [[[0] * m for _ in range(n)] for _ in range(30)]
for bit in range(30):
    for i in range(n):
        for j in range(m):
            if grid[i][j] & (1 << bit):
                pref[bit][i][j] += 1

    for i in range(1, n):
        pref[bit][i][0] += pref[bit][i - 1][0]
    for i in range(1, m):
        pref[bit][0][i] += pref[bit][0][i - 1]
    for i in range(1, n):
        for j in range(1, m):
            pref[bit][i][j] += pref[bit][i][j - 1] + \
                pref[bit][i - 1][j] - pref[bit][i - 1][j - 1]

q = int(input())
for _ in range(q):
    arr = list(map(int, input().split()))
    x1 = arr[0] - 1
    y1 = arr[1] - 1
    x2 = arr[2] - 1
    y2 = arr[3] - 1

    def query(bit):
        cur = pref[bit][x2][y2]
        if x1 > 0:
            cur -= pref[bit][x1 - 1][y2]
        if y1 > 0:
            cur -= pref[bit][x2][y1 - 1]
        if x1 > 0 and y1 > 0:
            cur += pref[bit][x1 - 1][y1 - 1]
        return cur

    res = 0
    for bit in range(30):
        if query(bit):
            res |= (1 << bit)

    print(res)

