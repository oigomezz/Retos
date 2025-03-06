n = int(input())
for i in range(n):
    a, b = map(int, input().split(" "))
    vis = [-1 for _ in range(a+1)]
    adjl = [[] for _ in range(a+1)]
    for j in range(b):
        c, d = map(int, input().split(" "))
        adjl[c].append(d)
        adjl[d].append(c)

    res = 0
    flag = True
    for j in range(1, a+1):
        if vis[j] == -1:
            count0 = 0
            count1 = 1
            q = [j]
            vis[j] = 1
            while q != []:
                r = q[0]
                q.pop(0)
                for k in adjl[r]:
                    if vis[k] == -1:
                        q.append(k)
                        if vis[r] == 0:
                            count1 = count1 + 1
                        else:
                            count0 = count0 + 1
                    if vis[k] == vis[r]:
                        flag = False
                        break
                    if vis[r] == 0:
                        vis[k] = 1
                    else:
                        vis[k] = 0
            res = res + max(count0, count1)

    if flag:
        print(res)
    else:
        print("NO")
