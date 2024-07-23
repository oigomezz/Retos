n = int(input())
m = int(input())

array = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    p, a, b, c, d = map(int, input().split())

    range1 = c - a
    range2 = d - b

    for i in range(a, a + range1 + 1):
        for j in range(b, b + range2 + 1):
            array[i][j] ^= p

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(array[i][j], end=" ")
    print()
