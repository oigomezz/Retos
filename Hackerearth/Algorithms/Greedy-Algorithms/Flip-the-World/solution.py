t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().strip().strip())))
    states = [0] * m
    res = 0
    for row in reversed(matrix):
        state = 0
        for i in range(m - 1, -1, -1):
            state ^= states[i]
            if row[i] == state:
                res += 1
                states[i] ^= 1
                state ^= 1
    print(res)
