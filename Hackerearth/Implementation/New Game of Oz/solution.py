t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]-1:
            arr[i+1] = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            count += 1
    print(count)
    t -= 1
