class Dsu:
    def __init__(self):
        self.par = [-1] * 100014

    def root(self, v):
        if self.par[v] < 0:
            return v
        self.par[v] = self.root(self.par[v])
        return self.par[v]

    def fri(self, v, u):
        return self.root(v) == self.root(u)

    def merge(self, v, u):
        v = self.root(v)
        u = self.root(u)
        if v == u:
            return False
        self.par[u] += self.par[v]
        self.par[v] = u
        return True


dsu = Dsu()


if __name__ == "__main__":
    n = int(input())
    have = [[] for _ in range(100014)]
    arr = list(map(int, input().split()))
    for i in range(n):
        x = arr[i]
        have[x].append(i)

    ans = 0
    for w in range(100013, 0, -1):
        r = -1
        for i in range(w, 100014, w):
            for x in have[i]:
                if r == -1:
                    r = x
                elif dsu.merge(r, x):
                    ans += w

    print(ans)
