class disjoint:
    def __init__(self, n):
        self.rank = [1]*n
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

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
            self.size[yid] += self.size[xid]
            self.size[xid] = 1

        elif (self.rank[xid] > self.rank[yid]):
            self.parent[yid] = xid  # merging y into x
            self.size[xid] += self.size[yid]
            self.size[yid] = 1

        else:
            self.parent[yid] = xid
            self.rank[xid] += 1
            self.size[xid] += self.size[yid]
            self.size[yid] = 1


n, m = map(int, input().split())
obj = disjoint(n)
for i in range(m):
    x, y = map(int, input().split())
    obj.union(x-1, y-1)
ans = []

for i in range(n):
    ans.append(obj.size[obj.find(i)])
total = 1
for i in range(len(obj.size)):
    total = total*obj.size[i]
    total %= 10**9+7
print(total)
