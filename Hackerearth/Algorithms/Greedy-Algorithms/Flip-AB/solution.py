t = int(input())
flip = {'A': 'B', 'B': 'A'}
for _ in range(t):
    n, m = map(int, input().strip().split())
    grid1 = []
    for _ in range(n):
        grid1.append(list(input().strip()))
    # input()
    grid2 = []
    for _ in range(n):
        grid2.append(list(input().strip()))
    for j in range(m):
        if grid1[0][j] != grid2[0][j]:
            for i in range(n):
                grid1[i][j] = flip[grid1[i][j]]
    for i in range(n):
        if grid1[i][0] != grid2[i][0]:
            for j in range(m):
                grid1[i][j] = flip[grid1[i][j]]
        if grid1[i] != grid2[i]:
            print('NO')
            break
    else:
        print('YES')
