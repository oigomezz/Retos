t = int(input())
for _ in range(t):
    n, a, b = map(int, input().strip().split())
    if a >= n:
        result = 1
    elif a > b:
        result = 2 * ((n - b - 1) // (a - b)) + 1
    else:
        result = -1
    print(result)
