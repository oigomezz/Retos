from heapq import heappush, heappop


n, k = map(int, input().split())
z = list(map(int, input().split()))

ans = [0 for _ in range(k)]
pq = []
for i in range(len(z)):
    heappush(pq, (-z[i], i))
for i in range(k):

    t = heappop(pq)
    ans[i] = t[1]+1
    if (abs(t[0]) > 1):
        heappush(pq, (-(abs(t[0])-1), t[1]))
print(*ans)
