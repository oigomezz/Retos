class disjoint:
    def __init__(self, n, t):
        self.rank = [1]*n
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.men = [0 for _ in range(n)]
        self.wen = [0 for _ in range(n)]
        for i in range(n):
            if (i < t):
                self.men[i] = 1
            if (i >= t):
                self.wen[i] = 1

    def find(self, x):
        if (self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xid = self.find(x)
        yid = self.find(y)

        if (xid == yid):
            return
        if (self.rank[xid] < self.rank[yid]):
            self.parent[xid] = yid
            self.men[yid] += self.men[xid]
            self.wen[yid] += self.wen[xid]

        elif (self.rank[xid] > self.rank[yid]):
            self.parent[yid] = xid  # merging y into x
            self.men[xid] += self.men[yid]
            self.wen[xid] += self.wen[yid]

        else:
            self.parent[yid] = xid
            self.rank[xid] += 1
            self.men[xid] += self.men[yid]
            self.wen[xid] += self.wen[yid]


n, m = map(int, input().split())
q1 = int(input())
obj = disjoint(n+m, n)
for i in range(q1):
    x, y = map(int, input().split())
    obj.union(x-1, y-1)

q2 = int(input())
for i in range(q2):
    x, y = map(int, input().split())
    obj.union(n+x-1, y-1+n)

q3 = int(input())
for i in range(q3):
    x, y = map(int, input().split())
    obj.union(x-1, n+y-1)
total = 0

for i in range(n+m):
    r = obj.find(i)
    total += (obj.men[r]*(m-obj.wen[r]))
    obj.men[r] = 0
    obj.wen[r] = 0
print(total)
