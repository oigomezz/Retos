n = int(input())
grf_1 = {}
grf_2 = {}
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            grf_1[(i, j)] = []
            if j-1 >= 0 and a[i][j-1] == 1:
                grf_1[(i, j)].append((i, j-1))
            if j+1 < n and a[i][j+1] == 1:
                grf_1[(i, j)].append((i, j+1))
            if i-1 >= 0:
                if j-1 >= 0 and a[i-1][j-1] == 1:
                    grf_1[(i, j)].append((i-1, j-1))
                if a[i-1][j] == 1:
                    grf_1[(i, j)].append((i-1, j))
                if j+1 < n and a[i-1][j+1] == 1:
                    grf_1[(i, j)].append((i-1, j+1))
            if i+1 < n:
                if j-1 >= 0 and a[i+1][j-1] == 1:
                    grf_1[(i, j)].append((i+1, j-1))
                if a[i+1][j] == 1:
                    grf_1[(i, j)].append((i+1, j))
                if j+1 < n and a[i+1][j+1] == 1:
                    grf_1[(i, j)].append((i+1, j+1))
        elif a[i][j] == 2:
            grf_2[(i, j)] = []
            if j-1 >= 0 and a[i][j-1] == 2:
                grf_2[(i, j)].append((i, j-1))
            if j+1 < n and a[i][j+1] == 2:
                grf_2[(i, j)].append((i, j+1))
            if i-1 >= 0:
                if j-1 >= 0 and a[i-1][j-1] == 2:
                    grf_2[(i, j)].append((i-1, j-1))
                if a[i-1][j] == 2:
                    grf_2[(i, j)].append((i-1, j))
                if j+1 < n and a[i-1][j+1] == 2:
                    grf_2[(i, j)].append((i-1, j+1))
            if i+1 < n:
                if j-1 >= 0 and a[i+1][j-1] == 2:
                    grf_2[(i, j)].append((i+1, j-1))
                if a[i+1][j] == 2:
                    grf_2[(i, j)].append((i+1, j))
                if j+1 < n and a[i+1][j+1] == 2:
                    grf_2[(i, j)].append((i+1, j+1))

pa = 0
for i in range(n):
    if a[0][i] == 1:
        vis = [[False for _ in range(n)]for _ in range(n)]
        st = [(0, i)]
        while (st):
            cur = st.pop(0)
            vis[cur[0]][cur[1]] = True
            for g in grf_1[cur]:
                if g[0] == n-1:
                    pa = 1
                    break
                if not vis[g[0]][g[1]]:
                    st.insert(0, g)
            if pa:
                break
        if pa:
            break
pb = 0
for i in range(n):
    if a[i][0] == 2:
        vis = [[False for _ in range(n)]for _ in range(n)]
        st = [(i, 0)]
        while (st):
            cur = st.pop(0)
            vis[cur[0]][cur[1]] = True
            for g in grf_2[cur]:
                if g[1] == n-1:
                    pb = 1
                    break
                if not vis[g[0]][g[1]]:
                    st.insert(0, g)
            if pb:
                break
        if pb:
            break

if pa and pb:
    print("AMBIGUOUS")
elif pa:
    print(1)
elif pb:
    print(2)
else:
    print(0)
