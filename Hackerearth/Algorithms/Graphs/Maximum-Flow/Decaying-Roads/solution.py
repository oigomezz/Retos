class Tee:
    def __init__(self, a=0, l=0, v=0):
        self.a = a
        self.l = l
        self.v = v


def rek(l):
    global b, voog
    if l == n + m + 1:
        b = 1
        voog += 1
        return
    kul[l] = 1
    for i in range(len(v[l])):
        o = v[l][i]
        if t[o].v and not kul[t[o].l]:
            rek(t[o].l)
        if not t[o].v and not kul[t[o].a]:
            rek(t[o].a)
        if b:
            if t[o].a == l:
                t[o].v -= 1
            else:
                t[o].v += 1
            return


n, m, k = map(int, input().split())

p = Tee(0, 0, 1)
voog = 0
v = [[] for _ in range(4005)]
b = True
kul = [False] * 4005
t = []

for i in range(1, n + 1):
    p.l = i
    t.append(Tee(p.a, p.l, p.v))
    v[0].append(len(t) - 1)
    v[i].append(len(t) - 1)

for i in range(k):
    x, y = map(int, input().split())
    p.a = x
    p.l = n + y
    t.append(Tee(p.a, p.l, p.v))
    v[x].append(len(t) - 1)
    v[n + y].append(len(t) - 1)

p.l = n + m + 1
capacity = list(map(int, input().split()))
for i in range(1, m + 1):
    x = capacity[i-1]
    p.a = n + i
    p.v = x
    t.append(Tee(p.a, p.l, p.v))
    v[n + i].append(len(t) - 1)
    v[n + m + 1].append(len(t) - 1)

b = True
while b:
    b = False
    kul = [False] * 4005
    rek(0)

z = int(input())
for i in range(z):
    print(voog)
    x, y = map(int, input().split())
    o = v[x + n][len(v[x + n]) - 1]
    if y > t[o].v:
        mit = y - t[o].v
        voog -= mit
        t[o].v = 0
        b = True
        while mit and b:
            b = False
            kul = [False] * 4005
            rek(n + x)
            mit -= 1
    else:
        t[o].v -= y
