t = int(input())
while t > 0:
    s, x, n = map(int, input().split())
    arr = list(map(int, input().split()))

    max_val = arr[0]
    ans = 0
    for i in range(n):
        if arr[i] >= max_val:
            max_val = arr[i]
            ans = i + 1

    arr.sort()
    if arr[-1] == arr[-2]:
        print("Many Roads")
    else:
        print(ans)

    t -= 1
