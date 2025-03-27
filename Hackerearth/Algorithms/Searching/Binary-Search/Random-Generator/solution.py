t = int(input())
for _ in range(t):
    n, k, p = map(int, input().strip().split())
    numbers = list(map(int, input().strip().split()))
    numbers.sort()
    worked = True
    for i in range(n - k + 1):
        if numbers[i + k - 1] - numbers[i] <= 2 * p:
            worked = False
            break
    print('YES' if worked else 'NO')
