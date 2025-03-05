import sys
from collections import defaultdict as dd


def ri(flag=0):
    if flag == 0:
        return [int(i) for i in input().split()]
    else:
        return int(input())


sys.setrecursionlimit(10**5)
mod = 10**9+7
n, d = ri()
par = [i for i in range(n)]
sz = [1 for _ in range(n)]
temp = 0


def f(x):
    if par[x] == x:
        return x
    else:
        par[x] = f(par[x])
        return par[x]


def union(x, y):
    a = f(x)
    b = f(y)
    global temp
    if sz[b] < sz[a]:
        x, y = y, x
    if a != b:
        sz[b] += sz[a]
        for i in range(-d, d+1):
            for j in get[a]:
                if j+i in get[b]:
                    temp += (get[a][j]*get[b][j+i])
        for i in get[a]:
            get[b][i] += get[a][i]
        get[a] = dd(int)
        par[a] = b
        return True
    else:
        return False


a = ri()
edges = []
for i in range(n-1):
    edges.append([int(i)-1 for i in input().split()])

get = [dd(int) for _ in a]
for i in range(n):
    get[i][a[i]] += 1

pro = []
for i in range(n-1):
    pro.append(ri(1)-1)
pro = pro[::-1]
new = []

for i in range(n-1):
    new.append(edges[pro[i]])

ans = []
for i, j in new:
    ans.append(temp)
    union(i, j)

ans = ans[::-1]
for i in ans:
    print(i)
