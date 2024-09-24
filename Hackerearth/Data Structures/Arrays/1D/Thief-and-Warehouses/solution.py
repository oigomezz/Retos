def solve(arr, n):
    warehouses = list(arr)
    warehouses.append(0)
    stolen_stack = []
    steal_info = (0, 0, 0, 0)
    for i, sacks in enumerate(warehouses):
        j = i
        while stolen_stack and stolen_stack[-1][-1] >= sacks:
            j, prev_sacks = stolen_stack.pop()
            segment = (i - j) * prev_sacks
            if segment > steal_info[0]:
                steal_info = (segment, j, i, prev_sacks)
        stolen_stack.append((j, sacks))
    return steal_info[0]


T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().strip().split()))

    out_ = solve(arr, n)
    print(out_)
