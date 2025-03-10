def solve(n, arr):
    total_sum = 0
    max_element = 0

    for i in range(n):
        total_sum += arr[i]
        if arr[i] > max_element:
            max_element = arr[i]

    if total_sum % (n - 1) != 0:
        return -1

    target = total_sum // (n - 1)
    if max_element > target:
        return -1

    required_moves = 0
    for i in range(n):
        required_moves += (target - arr[i])

    return target if required_moves == target else -1


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    out_ = solve(N, A)
    print(out_)
