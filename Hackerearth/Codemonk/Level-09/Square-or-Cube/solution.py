import math


def big_mod(b, p, m):
    r = 1
    while p > 0:
        if p % 2 == 1:
            r = (r * b) % m
        p //= 2
        b = (b * b) % m
    return r


n, q = map(int, input().split())
assert 1 <= n <= 300000 and 1 <= q <= 300000

ara = [0] * (n + 1)
zr = [0] * (n + 1)
neg = [0] * (n + 1)
h1 = [0] * (n + 1)
h2 = [0] * (n + 1)
cnt = [0] * 100005
stat = [False] * 100005
G = [[] for _ in range(100005)]

sq = int(math.sqrt(100000))
for i in range(4, 100001, 2):
    stat[i] = True
for i in range(3, sq + 1, 2):
    if not stat[i]:
        for j in range(i * i, 100001, 2 * i):
            stat[j] = True
for i in range(2, 100001):
    if not stat[i]:
        for j in range(i, 100001, i):
            temp = j
            count = 0
            while temp % i == 0:
                temp //= i
                count += 1
            count %= 6
            G[j].extend([i] * count)

base = 101
hsq = 0
hcb = 0

arr = list(map(int, input().split()))
for i in range(1, n + 1):
    ara[i] = int(arr[i - 1])
    assert -100000 <= ara[i] <= 100000
    zr[i] = zr[i - 1] + (ara[i] == 0)
    neg[i] = neg[i - 1] + (ara[i] < 0)
    ara[i] = abs(ara[i])
    for p in G[ara[i]]:
        val = big_mod(base, p, 1000000007)
        if cnt[p] % 2 == 0:
            hsq = (hsq + val) % 1000000007
        else:
            hsq = (hsq - val) % 1000000007
        if cnt[p] % 3 != 2:
            hcb = (hcb + val) % 1000000007
        else:
            hcb = (hcb - 2 * val) % 1000000007
        cnt[p] += 1
    hsq = (hsq + 1000000007) % 1000000007
    hcb = (hcb + 1000000007) % 1000000007
    h1[i] = hsq
    h2[i] = hcb

for _ in range(q):
    l, r = map(int, input().split())
    assert 1 <= l <= n and 1 <= r <= n and l <= r
    issq = False
    iscb = False
    sqhash = h1[r] - h1[l - 1]
    cbhash = h2[r] - h2[l - 1]
    if zr[r] - zr[l - 1] > 0:
        issq = iscb = True
    if (neg[r] - neg[l - 1]) % 2 == 0 and sqhash == 0:
        issq = True
    if cbhash == 0:
        iscb = True
    if issq and iscb:
        print("Both")
    elif issq:
        print("Square")
    elif iscb:
        print("Cube")
    else:
        print("None")
