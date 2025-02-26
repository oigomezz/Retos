from bisect import bisect_left, bisect_right

n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()

k = int(input())
for _ in range(k):
    a, x = map(int, input().split())
    if a == 0:
        print(n - bisect_left(arr, x))
    else:
        print(n - bisect_right(arr, x))
