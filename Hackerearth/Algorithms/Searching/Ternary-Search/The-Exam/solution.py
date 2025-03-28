t = int(input())
for _ in range(t):
    x, l, n = tuple(map(int, input().split()))
    if n == 0 or x == 0:
        print(0)
    elif l == 0:
        print(x)
    elif n == 1:
        print(0 if x <= l else x - l)
    elif n > 55:
        print(x)
    else:
        d = x - (l // (2 ** (n - 1)))
        print(0 if d <= 0 else d)
