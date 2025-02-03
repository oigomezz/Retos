t = int(input())
for _ in range(t):
    a = input().strip()
    q = int(input())
    for _ in range(q):
        kind, *query = input().strip().split()
        if kind == '0':
            l, r = map(int, query)
            print(int(a[l: r + 1], 2) % 5)
        elif kind == '1':
            x, v = query
            x = int(x)
            a = a[:x] + v + a[x + 1:]
