n, k = map(int, input().split())
cg = {}

for group in range(k):
    row = list(map(int, input().split()))
    numcity = row[0]
    if numcity > 0:
        for seq in range(numcity):
            city = row[seq + 1]
            cg[city] = group

q = int(input())
for j in range(q):
    x, y = list(map(int, input().split()))
    xloc = cg.get(x)
    yloc = cg.get(y)

    if xloc == yloc:
        print(0)
    else:
        forward = abs(xloc - yloc)
        backward = k - forward
        print(min(forward, backward))
