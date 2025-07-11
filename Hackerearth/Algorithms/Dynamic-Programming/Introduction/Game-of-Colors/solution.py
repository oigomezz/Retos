tyms = [[[0] * 102 for _ in range(102)] for _ in range(102)]
freq = [[0] * 102 for _ in range(102)]
val = [0] * 3
m = {"R": 0, "G": 1, "B": 2}
n, q = map(int, input().split())
assert 1 <= n <= 100
assert 1 <= q <= 500000

for i in range(1, n+1):
    line = list(map(int, input().split()))
    for j in range(1, n + 1):
        freq[i][j] = line[j - 1]
        assert 1 <= freq[i][j] <= 100


for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, 101):
            tyms[i][j][k] = tyms[i - 1][j][k] + \
                tyms[i][j - 1][k] - tyms[i - 1][j - 1][k]
            tyms[i][j][k] += (freq[i][j] == k)

for _ in range(q):
    line = list(map(str, input().split()))
    tot = int(line[0])
    x1 = int(line[1])
    y1 = int(line[2])
    x2 = int(line[3])
    y2 = int(line[4])
    c = line[5]

    assert tot <= 100
    assert 1 <= x1 <= n
    assert 1 <= x2 <= n
    assert 1 <= y1 <= n
    assert 1 <= y2 <= n
    assert x2 >= x1 and y2 >= y1

    for i in range(3):
        val[i] = 0

    for i in range(1, 101):
        x = (tyms[x2][y2][i] - tyms[x1 - 1][y2][i] -
             tyms[x2][y1 - 1][i] + tyms[x1 - 1][y1 - 1][i])
        val[(tot // i) % 3] += x

    print(val[m[c]])
