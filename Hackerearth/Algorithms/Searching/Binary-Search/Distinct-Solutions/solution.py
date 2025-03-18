t = int(input())
index = 1
results = []
for _ in range(t):
    n, t1, t2 = map(int, input().split())
    lo = 0
    hi = 1100000000000000000
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid // t1 + mid // t2 < n:
            lo = mid
        else:
            hi = mid

    ans = hi
    results.append(f"{(ans + t1 - 1) // t1 + (ans + t2 - 1) // t2} ")
    if ans % t1:
        ans = (ans + t1 - 1) // t1 * t1
    else:
        ans = (ans + t2 - 1) // t2 * t2
    results[-1] += str(ans)

print("\n".join(results))
