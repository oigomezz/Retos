n, m = map(int, input().split())
l = [[] for _ in range(n)]
for i in range(n):
    l[i] = [int(x) for x in input().split()]
v = [int(x) for x in input().split()]

ans = 0
for i in range(n):
    k1 = 0
    k3 = 0
    k2 = abs(v[1]*len(l[i]))
    for j in l[i]:
        k1 += abs(j)
        k3 += abs(j+v[0])
    ans += max(k1, k2, k3)

ans2 = 0
for i in range(m):
    k1 = 0
    k3 = 0
    k2 = abs(v[3]*n)
    for j in range(n):
        k1 += abs(l[j][i])
        k3 += abs(l[j][i]+v[2])
    ans2 += max(k1, k2, k3)

print(max(ans, ans2))
