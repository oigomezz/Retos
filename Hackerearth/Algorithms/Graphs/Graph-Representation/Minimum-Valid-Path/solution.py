import heapq


class State:
    def __init__(self, index_, flag, dist_):
        self.index = index_
        self.isspecial = flag
        self.dist = dist_

    def __lt__(self, other):
        return self.dist > other.dist


pb = []
edges = []


def iscompatible(index1, index2):
    if index1 == m:
        return True
    a = edges[index1][1]
    b = edges[index2][1]
    if a > b:
        a, b = b, a
    return 2 * a >= b


def dijkstrascheck(s):
    if s.dist < dist[s.index][s.isspecial]:
        dist[s.index][s.isspecial] = s.dist
        heapq.heappush(pb, s)


def dijkstras():
    for i in range(len(dist)):
        dist[i] = [float('inf')] * 2
    s = State(m, special[x], 0)
    dijkstrascheck(s)
    while pb:
        curr = heapq.heappop(pb)
        vertex = edges[curr.index][0]
        if vertex == y and curr.isspecial:
            return curr.dist
        for index in adj[vertex]:
            if not iscompatible(curr.index, index):
                continue
            if special[edges[index][0]] and curr.isspecial:
                continue
            s1 = State(
                index, (special[edges[index][0]] or curr.isspecial), curr.dist + edges[index][1])
            dijkstrascheck(s1)
    return -1


n, m = map(int, input().split())
adj = [[] for _ in range(500007)]
special = [False] * 500007
dist = [[float('inf')] * 2 for _ in range(500007)]

for i in range(m):
    u, v, w = map(int, input().split())
    adj[u].append(len(edges))
    edges.append((v, w, len(edges)))

k = int(input())
for _ in range(k):
    x = int(input())
    special[x] = True

x, y = map(int, input().split())
edges.append((x, 0, m))
print(dijkstras())
