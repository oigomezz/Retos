t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    k = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if (arr[i] != arr[j] and (arr[i]+arr[j]) % 2 == 0):
                k += 1
    print(k)
    t -= 1
