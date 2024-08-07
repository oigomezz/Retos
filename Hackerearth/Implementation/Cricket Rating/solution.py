def max_sum(a, size):
    maxnow = 0
    maxup = 0

    for i in range(0, size):
        maxup = maxup + a[i]
        if (maxnow < maxup):
            maxnow = maxup
        if maxup < 0:
            maxup = 0
    return maxnow


n = int(input())
if n == 0:
    print("0")
else:
    a = list(map(int, input().split()))
    print(max_sum(a, len(a)))
