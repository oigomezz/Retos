import math

t = int(input())
for _ in range(t):
    N, Q = map(int, input().split())
    even = [0] * (N + 1)
    odd = [0] * (N + 1)
    even[0] = 0
    odd[0] = 0
    arr = list(map(int, input().split()))
    for i in range(N):
        if (arr[i] & 1):
            odd[i + 1] = odd[i] + 1
            even[i + 1] = even[i]
        else:
            even[i + 1] = even[i] + 1
            odd[i + 1] = odd[i]

    for i in range(Q):
        k, l, r = map(int, input().split())
        p = 0
        q = r - l + 1

        if k:
            p = odd[r] - odd[l - 1]
        else:
            p = even[r] - even[l - 1]

        if (not p):
            print("0")
        elif (p == q):
            print("1")
        else:
            g = math.gcd(p, q)
            print((p // g), (q // g))
