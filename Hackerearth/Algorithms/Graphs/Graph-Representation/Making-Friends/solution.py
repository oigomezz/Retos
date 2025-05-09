t = int(input())
for _ in range(t):
    nm = tuple(map(int, input().strip().split()))
    n = nm[0]
    if len(nm) == 2:
        m = nm[1]
    else:
        m = int(input())

    if not n % 2 and 2 * m <= n or m == 0:
        print('Yes')
    else:
        print('No')
