def solve(a, n):
    total = 0
    # 2 ** 60 > 10 ** 18
    if n < 60:
        k = 2 ** (n - 1)
        total = sum(i for i in a if i >= k) % 1000000007
    return total


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))

    out_ = solve(arr, n)
    print(out_)
