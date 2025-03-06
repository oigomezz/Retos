n, m = map(int, input().split())
d = {}
l1 = [0] * n
l2 = [0] * n
for i in range(n):
    d[i] = []
for i in range(m):
    a, b = map(int, input().split())
    l1[a - 1] += 1
    l2[b - 1] += 1

vis = [False] * n
c1 = c2 = 0
for i in range(n):
    if l1[i] == 0:
        c1 += 1
    if l2[i] == 0:
        c2 += 1
print(max(c1, c2))
