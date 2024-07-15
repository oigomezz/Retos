t = int(input())
while t:
    t -= 1
    count = 0
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n-1):
        if (arr[i] > arr[i+1]) or ((arr[i+1] - arr[i]) > 1) or (arr[0] > 1):
            count = 1
            break
    if count == 1:
        print("-1")
    else:
        result = "a"
        for i in range(1, n):
            if arr[i-1] != arr[i]:
                result += chr(96 + arr[i])
            else:
                result += "a"
        print(result)
