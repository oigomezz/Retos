from collections import defaultdict

n, m, k = map(int, input().split())
gr = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    gr[a - 1].append(b - 1)
    gr[b - 1].append(a - 1)

q = int(input())
vis = [-1] * n
cou = [0] * n
co = 0

for i in range(1, q + 1):
    a, b = map(int, input().split())
    a -= 1

    if cou[a] < k:
        cou[a] += b
        for c in gr[a]:
            if vis[c] == -1:
                tot = 0
                bo = False
                for d in gr[c]:
                    tot += cou[d]
                    if tot >= k:
                        bo = True
                        break
                if bo:
                    vis[c] = i
                    co += 1
    if co == n:
        break

print(" ".join(map(str, vis)))
