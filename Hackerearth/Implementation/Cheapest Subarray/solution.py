t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    sum_ = sum(arr[:2])
    minn = sum_

    for i in range(2, n):
        sum_ = sum_ + arr[i] - arr[i-2]
        minn = min(minn, sum_)

    print(minn)
    t -= 1
