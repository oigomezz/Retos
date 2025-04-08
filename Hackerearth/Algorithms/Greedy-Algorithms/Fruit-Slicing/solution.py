def solve(num, arr):
    return len(set(arr))


test_cases = int(input())
for _ in range(test_cases):
    num = int(input())
    arr = list(map(int, input().split()))

    out_ = solve(num, arr)
    print(out_)
