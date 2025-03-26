test_cases = int(input())
for _ in range(test_cases):
    a, b, c, k = map(int, input().split())
    lower_bound = 0
    upper_bound = 100000
    answer = -1
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        value = a * (mid ** 2) + b * mid + c

        if value >= k:
            answer = mid
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1

    print(answer)
