def update(ind):
    while ind <= N:
        bt[ind] += 1
        ind += (ind & -ind)


def query(ind):
    ans = 0
    while ind > 0:
        ans += bt[ind]
        ind -= (ind & -ind)
    return ans


def func(a, b):
    return a[0][1] < b[0][1]


N, M, D = map(int, input().split())
bt = [0] * (N + 1)
ans = [0] * M
pos = [0] * (N + 1)
p = [0] * (N + 1)

permutation = list(map(int, input().split()))
for i in range(1, N + 1):
    p[i] = permutation[i-1]
    pos[p[i]] = i

Q = []
for i in range(M):
    l, r = map(int, input().split())
    Q.append(((l, r), i))

Q.sort()
j = 0

for i in range(1, N + 1):
    for k in range(max(1, p[i] - D), min(N, p[i] + D) + 1):
        if pos[k] <= i:
            update(pos[k])
    while j < len(Q) and Q[j][0][1] == i:
        ans[Q[j][1]] = query(Q[j][0][1]) - query(Q[j][0][0] - 1)
        j += 1

print('\n'.join(map(str, ans)))
