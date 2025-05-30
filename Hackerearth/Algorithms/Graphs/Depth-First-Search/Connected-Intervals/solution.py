import sys

n, m = map(int, sys.stdin.readline().split())
p = list(range(100500))
rk = [0] * 100500
ox = [0] * 100500
ork = [0] * 100500
ptr = 0
nc = n
cnt1 = 0
cnt2 = 0
u = [0] * 100500
v = [0] * 100500
res = [-1] * 100500
cnt = 0
b = [False] * 100500
used = []


def clear():
    global ptr, nc
    for i in used:
        p[i] = i
        rk[i] = 0
        b[i] = False
    ptr = 0
    nc = n
    used.clear()


def get(x):
    while x != p[x]:
        x = p[x]
    return x


def getf(x):
    if x != p[x]:
        p[x] = getf(p[x])
    return p[x]


def unite(x, y):
    global cnt1, ptr, nc
    cnt1 += 1
    x = get(x)
    y = get(y)
    if x == y:
        return
    if rk[x] > rk[y]:
        x, y = y, x
    ox[ptr] = x
    ork[ptr] = rk[y]
    if rk[x] == rk[y]:
        rk[y] += 1
    p[x] = y
    nc -= 1
    ptr += 1


def unitef(x, y):
    global cnt2, nc
    cnt2 += 1
    if not b[x]:
        b[x] = True
        used.append(x)
    if not b[y]:
        b[y] = True
        used.append(y)
    x = getf(x)
    y = getf(y)
    if x == y:
        return
    if rk[x] > rk[y]:
        x, y = y, x
    if rk[x] == rk[y]:
        rk[y] += 1
    p[x] = y
    nc -= 1


for i in range(m):
    u[i], v[i] = map(int, sys.stdin.readline().split())
    u[i] -= 1
    v[i] -= 1

for i in range(n):
    p[i] = i
    rk[i] = 0
    b[i] = False

ptr = 0
nc = n

for L in range(0, m, 400):
    assert ptr == 0
    clear()
    R = min(m, L + 400)
    r = R
    for l in range(L, R):
        for i in range(l, R):
            unite(u[i], v[i])
            if nc == 1:
                res[l] = i
                break
        if res[l] != -1 and r > R:
            res[l] = r - 1
        r1 = r
        if res[l] == -1:
            while r1 < m:
                unite(u[r1], v[r1])
                if nc == 1:
                    res[l] = r1
                    r1 += 1
                    break
                r1 += 1
        if res[l] == -1:
            break
        while ptr:
            nc += 1
            ptr -= 1
            x = ox[ptr]
            y = p[x]
            rk[y] = ork[ptr]
            p[x] = x
        while r < r1:
            unitef(u[r], v[r])
            r += 1

ans = sum(m - res[i] for i in range(m) if res[i] != -1)
print(ans)
