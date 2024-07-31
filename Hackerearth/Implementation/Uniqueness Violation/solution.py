def solve(a, u, n):
    ans = 0
    i = 0
    while i < n:
        j = i
        maxval = a[i]
        while j < n and u[i] == u[j]:
            maxval = max(maxval, a[j])
            j += 1
        i = j
        ans += maxval
    return ans


T = int(input())
for _ in range(T):
    N = int(input())
    U = list(map(int, input().split()))
    A = list(map(int, input().split()))

    out_ = solve(A, U, N)
    print(out_)
