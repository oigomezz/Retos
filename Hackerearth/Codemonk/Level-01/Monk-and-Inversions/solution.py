t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    arr = []
    for i in range(n):
        row = list(map(int, input().split()))
        arr.append(row)

    c = 0
    for i in range(n):
        for j in range(n):
            for x in range(i, n):
                for y in range(j, n):
                    if arr[x][y] < arr[i][j]:
                        c += 1

    print(c)
