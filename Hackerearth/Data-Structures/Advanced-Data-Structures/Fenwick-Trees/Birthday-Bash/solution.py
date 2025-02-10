def update(x, val, n):
    while x <= n:
        BIT[x] += val
        x += (x & -x)


def query(x):
    suma = 0
    while x > 0:
        suma += BIT[x]
        x -= (x & -x)
    return suma


BIT = [0] * 2000005
t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    s = list(input())

    for i in range(n + 1):
        BIT[i] = 0

    mid = n // 2
    for _ in range(q):
        type, x = map(int, input().split())
        if type == 1:
            x = max(x, n - 1 - x)
            update(mid, 1, n)
            if x != (n - 1):
                update(x + 1, -1, n)
        else:
            y = max(x, n - 1 - x)
            z = query(y) % 2
            if z == 1:
                x = n - 1 - x
            if s[x] == 'z':
                s[x] = 'a'
            else:
                s[x] = chr(ord(s[x]) + 1)

    for i in range(mid, n):
        k = query(i) % 2
        if k == 1:
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]

    print(''.join(s))
