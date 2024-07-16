n, m = map(int, input().split())
t = [input() for _ in range(n)]

b = [False] * 2000
l = []

ans = 0
for j in range(m):
    l.clear()
    er = False
    for i in range(1, n):
        if not b[i] and ord(t[i][j]) < ord(t[i-1][j]):
            ans += 1
            er = True
            break
        elif not b[i] and ord(t[i][j]) > ord(t[i-1][j]):
            l.append(i)
    if not er:
        for x in l:
            b[x] = True
print(ans)
