import sys


def upd(idx, bit):
    while idx < 100004:
        bit[idx] += 1
        idx += (idx & -idx)


def qry(idx, bit):
    sm = 0
    while idx > 0:
        sm += bit[idx]
        idx -= (idx & -idx)
    return sm


input = sys.stdin.read
data = input().split()
index = 0
t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    index += 1
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    c = [0] * (100005)
    bit = [0] * (100005)
    lft = [0] * (n + 1)
    rght = [0] * (n + 1)

    for i in range(1, n + 1):
        a[i] = int(data[index])
        c[a[i]] = i
        index += 1

    for i in range(1, n + 1):
        b[i] = c[int(data[index])]
        index += 1

    ans = 0
    for i in range(1, n + 1):
        lft[i] = qry(b[i] - 1, bit)
        upd(b[i], bit)

    bit = [0] * (100005)
    for i in range(n, 0, -1):
        rght[i] = qry(100002, bit) - qry(b[i], bit)
        upd(b[i], bit)

    for i in range(1, n + 1):
        ans += lft[i] * rght[i]

    print(ans)
