M = {}
que = [[] for _ in range(200005)]
intervals = []
l = [0] * 200005
r = [0] * 200005
k = [0] * 200005
x = [0] * 200005
lo = [0] * 200005
hi = [0] * 200005
mid = [0] * 200005
BIT = [0] * 600015


def bit_upd(pos, val):
    while pos < 600015:
        BIT[pos] += val
        pos += (pos & -pos)


def bit_get(pos):
    ret = 0
    while pos > 0:
        ret += BIT[pos]
        pos -= (pos & -pos)
    return ret


n = int(input())
nums = []
for i in range(n):
    l[i], r[i] = map(int, input().split())
    nums.append(l[i])
    nums.append(r[i])

q = int(input())
for i in range(q):
    k[i], x[i] = map(int, input().split())
    nums.append(x[i])

nums = sorted(set(nums))
for i in range(len(nums)):
    M[nums[i]] = i + 1

for i in range(n):
    intervals.append((r[i] + 1 - l[i], (M[l[i]], M[r[i]])))

intervals.sort()
for i in range(q):
    lo[i] = 0
    hi[i] = n
    mid[i] = (lo[i] + hi[i]) // 2
    que[mid[i]].append(i)

changed = True
while changed:
    changed = False
    BIT[:] = [0] * 600015
    for i in range(n):
        l = intervals[i][1][0]
        r = intervals[i][1][1]
        bit_upd(l, 1)
        bit_upd(r + 1, -1)
        while que[i]:
            qnum = que[i].pop()
            pos = M[x[qnum]]
            if bit_get(pos) >= k[qnum]:
                hi[qnum] = mid[qnum]
            else:
                lo[qnum] = mid[qnum] + 1
            if lo[qnum] < hi[qnum]:
                changed = True
                mid[qnum] = (lo[qnum] + hi[qnum]) // 2
                que[mid[qnum]].append(qnum)

for i in range(q):
    if lo[i] >= n:
        print(-1)
    else:
        print(intervals[lo[i]][0])
