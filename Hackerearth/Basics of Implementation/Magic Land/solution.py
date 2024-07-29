t = int(input())
results = []
for _ in range(t):
    n, m = map(int, input().split())
    mat = [[0] * (m + 1) for _ in range(n + 1)]
    row = [[0] * (m + 1) for _ in range(n + 1)]
    col = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        mat[i] = [int(x) for x in input().split()]

    colMax = 0
    rowMax = 0

    for i in range(1, n + 1):
        for j in range(m):
            col[i][j-1] = 1
            if i > 1 and mat[i][j-1] == mat[i - 1][j-1]:
                col[i][j-1] += col[i - 1][j-1]
            row[i][j-1] = 1
            if j-1 > 1 and mat[i][j-1] == mat[i][j - 2]:
                row[i][j-1] += row[i][j - 2]
            colMax = max(colMax, col[i][j-1])
            rowMax = max(rowMax, row[i][j-1])

    results.append(colMax * rowMax)

for result in results:
    print(result)
