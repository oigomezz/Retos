test_cases = int(input())
for _ in range(test_cases):
    index = 0
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    arr12 = [0] * (2 * n)

    for i in range(n):
        arr12[i] = a[i]

    for i in range(n):
        arr12[i + n] = b[i]

    arr12.sort()
    a.sort()
    b.sort()

    if arr12[n - 1] != arr12[n]:
        print(-1)
        continue

    prev = 0
    for i in range(n - 1, 0, -1):
        if arr12[i] == arr12[i - 1]:
            prev += 1
        else:
            break

    last = 0
    for i in range(n, 2 * n - 1):
        if arr12[i] == arr12[i + 1]:
            last += 1
        else:
            break

    min_moves = n
    k = 0
    h = 0

    for i in range(n):
        if a[i] == arr12[n - 1]:
            k += 1
            if k == 1:
                y = i
            if b[(n - 1 - i)] == arr12[n - 1] and min_moves > abs(n // 2 - i):
                min_moves = abs(n // 2 - i)
                index = i

    if k > 1:
        for i in range(y, n - 1):
            if min_moves > abs(n // 2 - i):
                min_moves = abs(n // 2 - i)
                index = i
            if a[i + 1] != a[i]:
                break

        y_count = a.count(arr12[n - 1])
        t = 1
        if y_count > prev:
            t = 0
            min_moves += y_count - prev

        if t:
            y_count = b[index + 1:n].count(arr12[n - 1])
            if y_count > last:
                min_moves += y_count - last

    else:
        for i in range(n - 1):
            if b[i] == b[i + 1] and b[i] == arr12[n - 1]:
                if min_moves >= abs(n // 2 - i):
                    h = 1
                    min_moves = abs(n // 2 - i)
                    index = i
                    if i < n // 2:
                        min_moves -= 1
                        index += 1

        y_count = b[:index].count(arr12[n - 1])
        t = 1
        if h:
            if y_count > prev:
                t = 0
                min_moves += y_count - prev

            if t:
                y_count = b[index + 1:n].count(arr12[n - 1])
                if y_count > last:
                    min_moves += y_count - last

    print(min_moves)
