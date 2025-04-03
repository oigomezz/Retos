def solve(arr):
    arr = sorted(arr)
    ans = 2
    for i in arr:
        if ans <= i:
            ans += 2
    return ans


t = int(input())
for _ in range(t):
    n = int(input())
    arr = map(int, input().split())

    out_ = solve(arr)
    print(out_)
