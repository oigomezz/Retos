N = int(1e5 + 5)
a = [0] * N
pref = [0] * N
suf = [0] * N

t = int(input())
while t > 0:
    cnt = 0
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n+1):
        a[i] = arr[i-1]
        pref[i] = max(pref[i-1], a[i])
    suf[n+1] = int(1e9)
    for i in range(n, 0, -1):
        suf[i] = min(suf[i+1], a[i])
    for i in range(1, n):
        if pref[i] < suf[i+1]:
            cnt += 1
    if cnt % 2 != 0:
        print("Jeel")
    else:
        print("Ashish")
    t -= 1
