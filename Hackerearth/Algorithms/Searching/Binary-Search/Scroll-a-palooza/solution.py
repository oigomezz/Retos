from bisect import bisect_left

test_cases = int(input())
for _ in range(test_cases):
    N = int(input())
    X = list(map(int, input().split()))
    M = int(input())
    qs = [int(input()) for _ in range(M)]

    maxL = [0]
    cur = 0
    for x in X:
        cur += x
        maxL.append(max(maxL[-1], abs(cur)))

    maxR = [abs(cur)]
    for x in reversed(X):
        cur -= x
        maxR.append(max(maxR[-1], abs(cur)))
    assert cur == 0
    for W in qs:
        assert W >= 1
        l = bisect_left(maxL, W)
        assert l != 0
        if l == len(maxL):
            print(-1)
            continue
        r = bisect_left(maxR, W)
        print(l, N-r)
