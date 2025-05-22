from collections import deque

n, m = map(int, input().split())
sizes = [0] * (1000005)
comp = [[0] * 1005 for _ in range(1005)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
s = [input().strip() for _ in range(n)]

len_comp = 0
for i in range(n):
    for j in range(m):
        if s[i][j] == '#':
            continue
        if comp[i][j]:
            continue
        Q = deque()
        cnt = 0
        len_comp += 1
        comp[i][j] = len_comp
        Q.append((i, j))
        while Q:
            ux, uy = Q.popleft()
            cnt += s[ux][uy] == '*'
            for k in range(4):
                vx, vy = ux + dx[k], uy + dy[k]
                if vx < 0 or vy < 0 or vx >= n or vy >= m:
                    continue
                if s[vx][vy] == '#':
                    continue
                if comp[vx][vy]:
                    continue
                Q.append((vx, vy))
                comp[vx][vy] = len_comp
        sizes[len_comp] = cnt

ans = max(sizes[:len_comp + 1])
for i in range(n):
    for j in range(m):
        if s[i][j] != '#':
            continue
        used = set()
        for k in range(4):
            vx, vy = i + dx[k], j + dy[k]
            if vx < 0 or vy < 0 or vx >= n or vy >= m:
                continue
            used.add(comp[vx][vy])
        cur = 0
        maxi1 = 0
        maxi2 = 0
        for x in used:
            if maxi2 < sizes[x]:
                maxi2 = sizes[x]
            if maxi1 < maxi2:
                maxi1, maxi2 = maxi2, maxi1
        ans = max(ans, maxi2 + maxi1)

print(ans)
