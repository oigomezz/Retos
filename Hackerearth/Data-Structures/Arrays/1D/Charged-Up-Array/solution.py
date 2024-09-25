def solve(a, n):
    total = 0
    if n < 60:  # 2 ** 60 > 10 ** 18
        k = 2 ** (n - 1)
        total = sum(i for i in a if i >= k) % 1000000007
    return total


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().strip().split()))

    out_ = solve(A, N)
    print(out_)
