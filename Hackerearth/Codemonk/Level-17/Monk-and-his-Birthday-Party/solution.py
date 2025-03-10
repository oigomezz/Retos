c = [0 for _ in range(100000)]


def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            c[i], c[j] = c[j], c[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    c[i+1], c[high] = c[high], c[i+1]
    return (i+1)


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


a = [0 for _ in range(-1, 100000)]

for i in range(int(input())):

    n, m = map(int, input().split())
    a_input = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    if max(a_input) < max(b):
        print("-1")
    else:
        a_input.sort()
        d = [1 for _ in range(-1, m)]
        d[-1] = 0
        j = 0
        while (j < m-1):
            if a_input[j] == a_input[j+1]:
                d[j] += 1
                a_input.pop(j+1)
                m -= 1
            else:
                d[j+1] += d[j]
                j += 1

        j = 0
        for i in a_input:
            a[j] = i
            j += 1

        quick_sort(b, 0, n-1)

        j = 0
        while (j < n-1):
            if b[j] == b[j+1]:
                c[j] += c[j+1]
                b.pop(j+1)
                c.pop(j+1)
                n -= 1
            else:
                j += 1

        rem = 0
        tot_div = 1
        empty = 0
        prev_pos = m-1
        i = m-1
        j = n-1
        while (j >= 0):
            if a[i] < b[j]:
                space = d[prev_pos] - d[i]
                prev_pos = i
                empty += (space*tot_div)
                if empty >= c[j]:
                    empty -= c[j]
                else:
                    c[j] -= empty
                    space = d[m-1] - d[i]
                    div = c[j]//space
                    rem = c[j] % space
                    if rem > 0:
                        div += 1
                        empty = space - rem
                    else:
                        empty = 0
                    tot_div += div
                j -= 1
            else:
                i -= 1
        print(tot_div)
