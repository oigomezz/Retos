n = int(input())
arr = list(map(int, input().strip().split()))

count = 0
swapped = True
while swapped:
    swapped = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
    count += 1
print(count)
