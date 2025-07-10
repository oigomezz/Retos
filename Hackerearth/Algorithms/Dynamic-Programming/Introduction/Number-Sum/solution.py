n = int(input())
arr = list(map(int, input().strip().split()))
if arr == sorted(arr):
    print(n * (n + 1))
else:
    print(n * (n + 1) // 2)
