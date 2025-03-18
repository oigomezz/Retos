from math import ceil, sqrt


def k(element):
    return element[1]


for i in range(int(input())):
    n, p = [int(x) for x in input().split()]
    X = [int(x) for x in input().split()]
    Y = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    arr = []

    for i in range(n):
        dist = sqrt(X[i]*X[i] + Y[i]*Y[i])
        val = A[i]
        arr.append((val, dist))

    arr.sort(key=k)
    running_sum = 0
    radius = -1
    for i in range(len(arr)):
        running_sum += arr[i][0]
        if running_sum >= p:
            radius = arr[i][1]
            break
    print(ceil(radius))
