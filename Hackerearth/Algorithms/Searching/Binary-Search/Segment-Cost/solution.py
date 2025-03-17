n = int(input())
a = [0] + [int(x) for x in input().split()]
x, y = map(int, input().split())
pre = [0] * (n+5)
xor = [0] * (n+5)
for i in range(1, n+1):
    pre[i] = pre[i-1] + a[i]
    xor[i] = xor[i-1] ^ a[i]

tot = -1
xx = -1
ll = -1
for i in range(x, y+1):
    st = i
    cost = (pre[y] - pre[st-1]) - (xor[y] ^ xor[st-1])
    if cost:
        lo = i
        hi = y
        while hi > lo + 1:
            mid = (lo + hi)//2
            cur = (pre[mid] - pre[st-1]) - (xor[mid] ^ xor[st-1])
            if cur == cost:
                hi = mid
            else:
                lo = mid

        if cost > tot:
            tot = cost
            xx = i
            yy = hi
        elif cost == tot and hi-i < yy - xx:
            xx = i
            yy = hi
    else:
        if cost > tot:
            tot = cost
            xx = i
            yy = i

print(xx, yy)
