import heapq

graph = [[] for _ in range(200000)]
n, q, a, b, c = 0, 0, 0, 0, 0
wght = [0] * 400000
open = [0] * 200001
close = [0] * 200001
dist1 = [0] * 200001
count1 = 1
sc = [0] * 200001
ft = [0] * 400001


def lsone(n):
    return n & -n


def update(index, val):
    global count1
    ft[index] += val
    index += lsone(index)
    while index <= 400000:
        ft[index] += val
        index += lsone(index)


def query(index):
    ans = ft[index]
    index -= lsone(index)
    while index >= 1:
        ans += ft[index]
        index -= lsone(index)
    return ans


def traverse(index, d1):
    global count1
    update(count1, d1)
    open[index] = count1
    count1 += 1
    for i in range(len(graph[index])):
        traverse(graph[index][i][0], wght[graph[index][i][1]])
    close[index] = count1
    count1 += 1
    update(count1, -d1)


n, q = map(int, input().split())
for i in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, i + 1))
    wght[i + 1] = c
    sc[i + 1] = b

traverse(1, 0)

for i in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, n + i))

for i in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        if b >= n:
            wght[b] = c
        else:
            update(open[sc[b]], -wght[b])
            update(close[sc[b]], wght[b])
            update(open[sc[b]], c)
            update(close[sc[b]], -c)
            wght[b] = c
    else:
        if b == c:
            print(0)
            continue
        ans1 = 0
        c1 = c
        flag = 0
        beg = 2
        pq = []
        heapq.heappush(pq, (0, b))
        c = 1
        for j in range(len(graph[1])):
            node = graph[1][j][0]
            if open[node] <= open[c1] and close[c1] <= close[node]:
                beg = open[node]
                break
        while pq:
            temp = heapq.heappop(pq)
            node = temp[1]
            dist = temp[0]
            if node == c:
                ans1 = -dist
                break
            elif node == c1:
                ans1 = -dist
                flag = 1
                break
            for j in range(len(graph[node])):
                roadlen = wght[graph[node][j][1]]
                node1 = graph[node][j][0]
                heapq.heappush(pq, (dist - roadlen, node1))
        if flag == 0:
            ans1 += query(open[c1])
        if open[b] <= open[c1] and close[c1] <= close[b]:
            ans1 = min(ans1, (query(open[c1]) - query(open[b])))
        print(ans1)
