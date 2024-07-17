t = int(input())
while t > 0:
    n, p = list(map(int, input().split()))
    arr = [int(x) for x in input().split()]
    p -= arr[0]
    count = 0
    for i in range(1, n):
        if arr[i] % 2 == 0:
            count = i - 0
        else:
            count = i - 1
        diff = arr[i] - count
        if diff <= 0:
            p -= 0
        else:
            p -= diff
    if p >= 0:
        print("Yes", p)
    else:
        print("No")

    t -= 1
