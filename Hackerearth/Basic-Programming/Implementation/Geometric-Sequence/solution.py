def max_for_given_ratio(arr, n, r):
    numbers = [0] * 200000
    maxx = 1
    for i in range(n):
        x = arr[i]
        if numbers[100000 + x] == 0:
            numbers[100000 + x] = 1
            if -100000 < r * x < 100000:
                numbers[100000 + r * x] = -1
        elif numbers[100000 + x] == -1:
            numbers[100000 + x] = numbers[100000 + x // r] + 1
            maxx = max(maxx, numbers[100000 + x])
            if -100000 < r * x < 100000:
                numbers[100000 + r * x] = -1
    return maxx


def for_one_zero(arr, n):
    arr.sort()
    maxx = 0
    maxx_elem = arr[0]
    i = 0
    while i < n:
        x = 0
        elem = arr[i]
        while i < n and arr[i] == elem:
            x += 1
            i += 1
        if x > maxx:
            maxx = x
            maxx_elem = arr[i - 1]
    if maxx_elem == 0:
        return min(maxx + 1, n)
    else:
        return maxx


n = int(input())
arr = list(map(int, input().split()))
maxx = 1
for r in range(2, 100):
    maxx = max(maxx, max_for_given_ratio(arr, n, r))
for r in range(-1, -100, -1):
    maxx = max(maxx, max_for_given_ratio(arr, n, r))
maxx = max(maxx, for_one_zero(arr, n))
print(maxx)
