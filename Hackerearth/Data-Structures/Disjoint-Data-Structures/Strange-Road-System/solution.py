class LinearBasis:
    def __init__(self, X: int):
        self.xs = [0] * X
        self.n = 0

    def add(self, x: int):
        for i in range(self.n):
            if (x ^ self.xs[i]) < x:
                x ^= self.xs[i]
        if x == 0:
            return

        self.xs[self.n] = x
        self.n += 1

        for i in range(self.n - 1):
            if self.xs[i] < self.xs[i + 1]:
                self.xs[i], self.xs[i + 1] = self.xs[i + 1], self.xs[i]

    def maximize(self, x: int) -> int:
        for i in range(self.n):
            if (x ^ self.xs[i]) > x:
                x ^= self.xs[i]
        return x

    def append(self, other):
        for i in range(other.n):
            self.add(other.xs[i])


class DisjointSet:
    def __init__(self, n: int = 0):
        self.N = n
        self.pars = [-1] * n
        self.lbs = [LinearBasis(32) for _ in range(n)]
        self.dis = [0] * n

    def init(self, n: int):
        self.N = n
        self.pars = [-1] * n
        self.lbs = [LinearBasis(32) for _ in range(n)]
        self.dis = [0] * n

    def find(self, x: int) -> int:
        p = self.pars[x]
        if p < 0:
            return x

        root = self.find(p)
        self.dis[x] ^= self.dis[p]
        self.pars[x] = root

        return root

    def merge(self, x: int, y: int, w: int) -> bool:
        b = self.distance(x) ^ self.distance(y) ^ w
        x = self.find(x)
        y = self.find(y)
        if x == y:
            self.lbs[x].add(b)
            return False

        if -self.pars[x] > -self.pars[y]:
            x, y = y, x
        self.dis[x] = b
        self.pars[y] += self.pars[x]
        self.pars[x] = y

        self.lbs[y].append(self.lbs[x])

        return True

    def distance(self, x: int) -> int:
        self.find(x)
        return self.dis[x]

    def query(self, x: int, y: int) -> int:
        if self.find(x) != self.find(y):
            return -1
        res = self.dis[x] ^ self.dis[y]
        return self.lbs[self.find(x)].maximize(res)


class Solution:
    def __init__(self):
        self.ds = DisjointSet()

    def init(self, n: int):
        self.ds.init(n)

    def update(self, x: int, y: int, w: int):
        self.ds.merge(x, y, w)

    def query(self, x: int, y: int) -> int:
        return self.ds.query(x, y)


if __name__ == "__main__":
    sol = Solution()
    n, q = map(int, input().split())
    sol.init(n)
    for i in range(q):
        line = list(map(int, input().split()))
        t = line[0]
        if t == 1:
            u, v, p = line[1:]
            u -= 1
            v -= 1
            sol.update(u, v, p)
        else:
            u, v = line[1:]
            u -= 1
            v -= 1
            print(sol.query(u, v))
