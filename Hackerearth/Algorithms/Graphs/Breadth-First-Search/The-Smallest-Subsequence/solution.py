import sys


class Solution:
    def Solve(self):
        self.MAX = 1_000_005
        lp = [0] * self.MAX
        self.pr = []
        self.pid = {1: 0}
        for i in range(2, self.MAX):
            if not lp[i]:
                lp[i] = i
                self.pr.append(i)
                self.pid[i] = len(self.pr)
            for p in self.pr:
                if p > lp[i] or i * p >= self.MAX:
                    break
                lp[i * p] = p

        self.n = int(input())
        a = list(map(int, input().split()))

        self.g = [[] for _ in range(len(self.pid))]
        e = set()
        for x in a:
            f = []
            while x > 1:
                p, c = lp[x], 0
                while lp[x] == p:
                    x //= p
                    c ^= 1
                if c:
                    f.append(p)
            if not f:
                print(1)
                sys.exit(0)
            f += [1] * (2 - len(f))
            u, v = self.pid[f[0]], self.pid[f[1]]
            if (u, v) in e or (v, u) in e:
                print(2)
                sys.exit(0)
            self.g[u].append(v)
            self.g[v].append(u)

    def bfs(self, s):
        d = [-1] * len(self.pid)
        d[s] = 0
        q = [(s, -1)]
        while q:
            q2 = []
            for u, p in q:
                for v in self.g[u]:
                    if d[v] != -1:
                        if v != p:
                            return d[u] + d[v] + 1
                    else:
                        d[v] = d[u] + 1
                        q2.append((v, u))
            q = q2

    def print(self):
        ans = self.n + 1
        for i in range(len(self.pid)):
            if i > 0 and self.pr[i - 1] ** 2 >= self.MAX:
                break
            ans = min(ans, self.bfs(i) or ans)
        print(ans if ans <= self.n else -1)


if __name__ == '__main__':
    s = Solution()
    s.Solve()
    s.print()
