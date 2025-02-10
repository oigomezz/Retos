from bisect import bisect_left

st = [0] * (1 << 18)


def update(pos, val, id=1, l=1, r=1 << 17):
    if pos < l or pos > r:
        return
    if l == r:
        st[id] = val
        return
    mid = (l + r) >> 1
    update(pos, val, id << 1, l, mid)
    update(pos, val, id << 1 | 1, mid + 1, r)
    st[id] = max(st[id << 1], st[id << 1 | 1])


def find_left(res, pos, k, id=1, l=1, r=1 << 17):
    if l > pos:
        return
    if res[0] != -1:
        return
    if l == r:
        if st[id] >= k:
            res[0] = l
        return
    mid = (l + r) >> 1
    if st[id << 1 | 1] >= k:
        find_left(res, pos, k, id << 1 | 1, mid + 1, r)
    if st[id << 1] >= k:
        find_left(res, pos, k, id << 1, l, mid)


def find_right(res, pos, k, id=1, l=1, r=1 << 17):
    if r < pos:
        return
    if res[0] != -1:
        return
    if l == r:
        if st[id] >= k:
            res[0] = l
        return
    mid = (l + r) >> 1
    if st[id << 1] >= k:
        find_right(res, pos, k, id << 1, l, mid)
    if st[id << 1 | 1] >= k:
        find_right(res, pos, k, id << 1 | 1, mid + 1, r)


n = int(input())
u = [tuple(map(int, input().split())) for _ in range(n)]
cc = []

for id, sz in u:
    cc.append(id)

nq = int(input())
q = [tuple(map(int, input().split())) for _ in range(nq)]

for pref, min_sz in q:
    cc.append(pref)

cc = sorted(set(cc))


def get_pos(val): return bisect_left(cc, val) + 1


for i in range(n):
    id, sz = u[i]
    u[i] = (get_pos(id), sz)

for i in range(nq):
    pref, min_sz = q[i]
    q[i] = (get_pos(pref), min_sz)

for id, sz in u:
    update(id, sz)

u.sort()


def get_val(id): return bisect_left(u, (id, 0)) - 1


for pref, min_sz in q:
    l = [-1]
    r = [-1]
    find_left(l, pref, min_sz)
    find_right(r, pref, min_sz)

    if l[0] == -1:
        if r[0] == -1:
            print(-1, end=' ')
        else:
            print(cc[r[0] - 1], end=' ')
    else:
        if r[0] == -1:
            print(cc[l[0] - 1], end=' ')
        else:
            if abs(cc[l[0] - 1] - cc[pref - 1]) <= abs(cc[r[0] - 1] - cc[pref - 1]):
                print(cc[l[0] - 1], end=' ')
            else:
                print(cc[r[0] - 1], end=' ')
