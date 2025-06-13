def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def link(x, y):
    if x == y:
        return
    if rank[x] > rank[y]:
        x, y = y, x
    if rank[x] == rank[y]:
        rank[y] += 1
    parent[x] = y


def union(x, y):
    return link(find(x), find(y))


n = get_number()
k = get_number()
arr = []
inp = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        inp[i][j] = get_number()


for i in range(n):
    for j in range(i+1, n):
        arr.append((i, j, inp[i][j]))

arr.sort(key=lambda x: -x[2])
rank = [0]*n
parent = []
for i in range(n):
    parent.append(i)
totake = max(len(arr)-k, n-1)
taken = [False]*len(arr)
req = n-1
for i in range(len(arr)):
    if req == 0:
        break
    u, v = arr[i][0], arr[i][1]
    if find(u) != find(v):
        taken[i] = True
        union(u, v)
        req -= 1
        totake -= 1
for i in range(len(arr)):
    if totake == 0:
        break
    if taken[i]:
        continue
    taken[i] = True
    totake -= 1
took = [[False]*n for _ in range(n)]
for i in range(len(arr)):
    if taken[i]:
        took[arr[i][0]][arr[i][1]] = True
ans = 0
ret = []
for i in range(n):
    for j in range(i+1, n):
        if not took[i][j]:
            ans += 1
            ret.append((i+1, j+1))

print(ans)
for i, j in ret:
    print(i, j)
