def possible(stack_nums, m):
    if m < 0:
        return False
    previous_stack_num = max(stack_nums[0] - m, 1)
    for i in range(1, len(stack_nums)):
        if previous_stack_num >= stack_nums[i] + m:
            return False
        if abs(previous_stack_num - stack_nums[i]) < m:
            previous_stack_num += 1
        else:
            previous_stack_num = max(stack_nums[i] - m, previous_stack_num + 1)
    return True


t = int(input())
for _ in range(t):
    n = int(input())
    stack_nums = list(map(int, input().split()))
    smallest = min(stack_nums)
    largest = max(stack_nums)
    low = 0
    high = max(largest, n)
    while low < high:
        m = (low + high)//2
        is_possible = possible(stack_nums, m)
        if is_possible and not possible(stack_nums, m - 1):
            print(m)
            break
        elif is_possible:
            high = m
        else:
            low = m + 1
