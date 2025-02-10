from sortedcontainers import SortedSet

t = int(input())
for xt in range(1, t + 1):
    se = SortedSet()
    pq = SortedSet()
    print(f"Case {xt}:")

    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for y in A:
        se.add(y)
        it = se.irange(maximum=y, reverse=True)
        x = next(it, None)
        if x is not None and x != y:
            pq.add((y - x, (x, y)))

    q = int(input())
    for _ in range(q):
        line = list(map(int, input().split()))
        c = line[0]
        if c == 1:
            x = line[1]
            se.add(x)
            it = se.irange(maximum=x, reverse=True)
            a = next(it, None)
            it = se.irange(minimum=x)
            b = next(it, None)

            if a is not None and b is not None:
                pq.discard((b - a, (a, b)))
            if a is not None:
                pq.add((x - a, (a, x)))
            if b is not None:
                pq.add((b - x, (x, b)))
        elif c == 2:
            p = pq[-1]
            print(p[0], p[1][0], p[1][1])
        elif c == 3:
            x = line[0]
            it = se.irange(maximum=x, reverse=True)
            a = next(it, None)
            it = se.irange(minimum=x)
            b = next(it, None)

            if a is not None:
                pq.discard((x - a, (a, x)))
            if b is not None:
                pq.discard((b - x, (x, b)))
            if a is not None and b is not None:
                pq.add((b - a, (a, b)))
            se.discard(x)
