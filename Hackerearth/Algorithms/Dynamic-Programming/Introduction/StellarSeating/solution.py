t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    pa = [0] * (n + 1)
    pb = [0] * (n + 1)
    for i in range(n):
        pa[i + 1] += pa[i] + arr[i]
        pb[i + 1] += pb[i] + (arr[i] ^ x)
    minsofar = float('inf')
    maxdiff = 0
    for i in range(n + 1):
        maxdiff = max(maxdiff, pb[i] - pa[i] - minsofar)
        minsofar = min(minsofar, pb[i] - pa[i])
    print(sum(arr) + maxdiff)
