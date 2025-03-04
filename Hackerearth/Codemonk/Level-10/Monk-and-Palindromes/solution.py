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

        elif (self.rank[xid] > self.rank[yid]):
            self.parent[yid] = xid  # merging y into x
            self.size[xid] += self.size[yid]
        else:
            self.parent[yid] = xid
            self.rank[xid] += 1
            self.size[xid] += self.size[yid]


n = int(input())
obj = disjoint(n)
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    length = y-x+1
    le = y-x
    for i in range(x-1, x-1+(length//2)):
        obj.union(i, i+le)
        le -= 2
ans = 1
pri = 10**9+7
for i in range(n):
    r = obj.find(i)
    if (obj.size[r] != 0):
        obj.size[r] = 0

        ans = ans*10
        ans %= pri
print(ans)
