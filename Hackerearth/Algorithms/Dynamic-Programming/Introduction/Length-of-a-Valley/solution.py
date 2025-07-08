def area(array, length):
    stack = []
    right = [0]*length
    index = 0
    while index < length:
        if len(stack) == 0 or array[stack[-1]] < array[index]:
            stack.append(index)
            index += 1
        else:
            while len(stack) > 0:
                x = stack.pop()
                right[x] = index

    while len(stack) > 0:
        x = stack.pop()
        right[x] = index

    return right


def l_area(array, length):
    stack = []
    left = [0]*length
    index = 0
    while index < length:
        if len(stack) == 0 or array[stack[-1]] < array[index]:
            stack.append(index)
            index += 1
        else:
            while len(stack) > 0:
                x = stack.pop()
                left[x] = index

    while len(stack) > 0:
        x = stack.pop()
        left[x] = index

    return left


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    left_index = l_area(arr[::-1], n)
    left_index = left_index[::-1]
    for i in range(n):
        left_index[i] = n - left_index[i] + 1
    right_index = area(arr, n)
    ans = [0]*n
    for i in range(n):
        ans[i] = right_index[i] - left_index[i] + 1
    print(*ans, sep=' ')
