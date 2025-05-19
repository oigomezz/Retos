L, B = map(int, input().split())
a = [list(input().strip()) for _ in range(L)]
bio = [[0] * B for _ in range(L)]
nakupina = []


def dfs(r, s):
    if r < 0 or r >= L:
        return
    if s < 0 or s >= B:
        return
    if a[r][s] == '.':
        return
    if bio[r][s]:
        return
    bio[r][s] = 1
    nakupina.append((r, s))
    dfs(r, s - 1)
    dfs(r, s + 1)
    dfs(r - 1, s)
    dfs(r + 1, s)


N = int(input())
arr = [int(x) for x in input().split()]
for i in range(N):
    h = arr[i]
    r = L - h
    if i % 2 == 0:
        for s in range(B):
            if a[r][s] == 'x':
                a[r][s] = '.'
                break
    else:
        for s in range(B - 1, -1, -1):
            if a[r][s] == 'x':
                a[r][s] = '.'
                break
    bio = [[0] * B for _ in range(L)]
    for r in range(L):
        for s in range(B):
            if a[r][s] == '.' or bio[r][s]:
                continue
            nakupina.clear()
            dfs(r, s)
            najniza = [-1] * B
            for (x, y) in nakupina:
                najniza[y] = max(najniza[y], x)
                a[x][y] = '.'
            padni = L
            for j in range(B):
                if najniza[j] == -1:
                    continue
                i = najniza[j] + 1
                while i < L and a[i][j] == '.':
                    i += 1
                padni = min(padni, i - najniza[j] - 1)
            for (x, y) in nakupina:
                a[x + padni][y] = 'x'
                bio[x + padni][y] = 1

for r in range(L):
    print(''.join(a[r]))
