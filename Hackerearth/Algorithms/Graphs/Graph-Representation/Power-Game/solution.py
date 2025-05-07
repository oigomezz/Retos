from collections import defaultdict


def go(x):
    low[x] = H[x]
    for y, eid in E[x]:
        if low[y] == -1:
            H[y] = H[x] + 1
            go(y)
            low[x] = min(low[x], low[y])
            if low[y] == H[y]:
                cands.append(W[eid])
        elif H[y] < H[x] - 1:
            low[x] = min(low[x], H[y])


n, m = map(int, input().split())
W = list(map(int, input().split()))
low = [-1] * n
H = [0] * n
cands = []
E = defaultdict(list)
for i in range(m):
    line = [int(x) - 1 for x in input().split()]
    a, b = line[0], line[1]
    E[a].append((b, i))
    E[b].append((a, i))

go(0)
cands.sort(reverse=True)
mn = 0
mx = 0
for i in range(len(cands)):
    if i % 2 == 1:
        mn += cands[i]
    else:
        mx += cands[i]

print(mx, mn)
