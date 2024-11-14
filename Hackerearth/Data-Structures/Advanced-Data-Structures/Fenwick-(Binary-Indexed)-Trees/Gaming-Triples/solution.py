def clea(n):
    for i in range(1, n + 1):
        BIT[i] = 0


def upd(idx, n):
    while idx <= n:
        BIT[idx] += 1
        idx += (idx) & (-idx)


def query(l, r):
    ret = 0
    while r:
        ret += BIT[r]
        r -= (r) & (-r)
    while l:
        ret -= BIT[l]
        l -= (l) & (-l)
    return ret


t = int(input())

for _ in range(t):
    n = int(input())
    a = [(0, 0)] * (n + 1)
    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        a[i] = (arr[i-1], i)
    a[1:n + 1] = sorted(a[1:n + 1])

    ans1 = 0
    ans2 = 0
    BIT = [0] * (n + 1)

    i = 1
    while i <= n:
        val = a[i][0]
        cnt = 0
        while i <= n and a[i][0] == val:
            ans1 += query(0, a[i][1]) * query(a[i][1] - 1, n)
            cnt += 1
            i += 1
        idx = i
        while cnt > 0:
            idx -= 1
            upd(a[idx][1], n)
            cnt -= 1

    clea(n)
    i = n
    while i >= 1:
        val = a[i][0]
        cnt = 0
        while i >= 1 and a[i][0] == val:
            ans2 += query(0, a[i][1]) * query(a[i][1] - 1, n)
            cnt += 1
            i -= 1
        idx = i
        while cnt > 0:
            idx += 1
            upd(a[idx][1], n)
            cnt -= 1

    clea(n)
    mov = int(input())

    if mov:
        if ans1 > ans2:
            print("Sarika")
        else:
            print("Ananya")
    else:
        if ans1 > ans2:
            print("Ananya")
        else:
            print("Sarika")

    if ans1 <= ans2:
        print(f"{2 * ans1}")
    else:
        print(f"{2 * ans2 + 1}")
