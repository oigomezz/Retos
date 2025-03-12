t = int(input())
for t_ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mn = a[0]  # min (a)
    nok = True
    while nok:
        ops = 0
        nok = False
        for v in a:
            ops += v // mn - 1
            rest = v % mn
            if rest:
                mn = rest
                nok = True
                break
    print(ops)
