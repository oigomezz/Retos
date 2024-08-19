import math


def ceil_number(x, y):
    x = abs(x)
    y = abs(y)
    root = math.sqrt((x * x) + (y * y))
    root = math.ceil(root)
    return int(root)


n, k = map(int, input().split())
x_arr = list(map(int, input().split()))
y_arr = list(map(int, input().split()))

distance = [ceil_number(x_arr[i], y_arr[i]) for i in range(n)]
distance.sort()
print(distance[k - 1])
