import heapq

n = int(input())
m = int(input())
l = []
for i in range(m):
    a = list(map(int, input().split()))
    l.append(a)

hp = [[0, 0]]
heapq.heapify(hp)
l.sort(key=lambda x: x[0])
flg = 0
for i in range(m):
    ele = heapq.heappop(hp)
    while (len(hp) > 0 and ele[1] < l[i][0]-1):
        ele = heapq.heappop(hp)
    if (ele[1] >= l[i][0]-1):
        heapq.heappush(hp, ele)
        if (l[i][1] > ele[1]):
            heapq.heappush(hp, [max(ele[0], l[i][2]), l[i][1]])
    else:
        flg = 1
        print(-1)
        break

if (flg == 0):
    ele = heapq.heappop(hp)
    while (ele[1] != n):
        ele = heapq.heappop(hp)
    if (ele[1] == n):
        print(ele[0])
