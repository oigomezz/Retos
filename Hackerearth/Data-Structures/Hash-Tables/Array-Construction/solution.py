import heapq


t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))

    q = []
    for value in v:
        if value:
            heapq.heappush(q, -value)

    ok = True
    if len(q) == 0:
        ok = False

    while len(q) > 1:
        z = -heapq.heappop(q)
        mx1 = -heapq.heappop(q)

        if len(q) == 0:
            if z == 1 and mx1 == 1:
                break
            if z % (mx1 + 1):
                ok = False
                break
            z //= (mx1 + 1)
            if z:
                heapq.heappush(q, -z)
            heapq.heappush(q, -mx1)
            continue

        mx2 = -q[0]
        if z - (mx1 * mx2) <= mx2:
            z -= (mx1 * mx2)
            if z:
                heapq.heappush(q, -z)
            heapq.heappush(q, -mx1)
        else:
            if z % (1 + mx1):
                ok = False
                break
            z //= (mx1 + 1)
            if z:
                heapq.heappush(q, -z)
            heapq.heappush(q, -mx1)

    if len(q):
        ok = False

    print("YES" if ok else "NO")
