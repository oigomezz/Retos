def minimumValue(N, A, B, C):
    li = [(val, 0) for val in A]
    li.extend([(val, 1) for val in B])
    li.extend([(val, 2) for val in C])
    li.sort()

    maxVals = [None]*3
    ans = float("inf")
    for val, typ in li:
        maxVals[typ] = val
        if all(maxVals):
            ans = min(ans, max(maxVals) - min(maxVals))
    return 2 * ans


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

out_ = minimumValue(N, A, B, C)
print(out_)
