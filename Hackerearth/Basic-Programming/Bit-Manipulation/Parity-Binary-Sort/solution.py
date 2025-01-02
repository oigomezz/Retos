def bits(n):
    return 0 if n == 0 else 1 ^ bits(n & (n - 1))


test_cases = int(input())
for _ in range(test_cases):
    a = []
    b = []
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        t = arr[i]
        if bits(t):
            a.append(t)
        else:
            b.append(t)

    a.sort()
    b.sort()

    print(' '.join(map(str, b)), end=' ')
    print(' '.join(map(str, a)))
