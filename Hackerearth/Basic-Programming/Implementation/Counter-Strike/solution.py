t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    N, M, D = tuple(l)
    pos = []
    for n in range(N):
        l = list(map(int, input().split()))
        pos.append(l)

    target = []
    for m in range(M):
        nl = list(map(int, input().split()))
        target.append(nl)
    shot = 0
    temptarget = target
    for p in pos:
        for t in temptarget:
            md = abs(p[0]-t[0]) + abs(p[1]-t[1])
            if md <= D:
                shot += 1
                temptarget.remove(t)
    if int(shot) >= int(M / 2):
        print('YES')
    else:
        print('NO')
