t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = 1 << n
    res = [0] * n
    vec = [[False] * n for _ in range(x)]
    mpp = {}

    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        mpp[(x, y)] = mpp[(y, x)] = True

    for i in range(n):
        vec[1 << i][i] = True

    for i in range(x):
        length = bin(i).count('1')
        for j in range(n):
            if i & (1 << j):
                for k in range(n):
                    if k != j and (i & (1 << k)) and (k, j) in mpp and vec[i ^ (1 << j)][k]:
                        vec[i][j] = True
                        res[j] = max(res[j], length - 1)

    print(" ".join(map(str, res)))
