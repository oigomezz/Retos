a = [0] * 1005
b = [0] * 1005
t = int(input())
for i in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[j] = arr[j-1]
    solution = 0
    for j in range(1, n + 1):
        b[j] = -2000000000000000000
    for j in range(1, n + 1):
        for h in range(j - 1, 0, -1):
            if b[h + 1] < b[h] + (h + 1) * a[j]:
                b[h + 1] = b[h] + (h + 1) * a[j]
        if b[1] < a[j]:
            b[1] = a[j]
    for j in range(1, n + 1):
        if b[j] > solution:
            solution = b[j]
    print(solution)
