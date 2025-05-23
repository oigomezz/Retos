class Query:
    def __init__(self, x, id):
        self.x = x
        self.id = id


class Main:
    def __init__(self):
        self.depth = 0

    def run(self):
        n, q = map(int, input().strip().split())
        g = [[] for _ in range(n)]

        for i in range(n - 1):
            u, v = map(int, input().strip().split())
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)

        qu = [[] for _ in range(n)]

        for i in range(q):
            x, y = map(int, input().strip().split())
            x -= 1
            qu[x].append(Query(y, i))

        ans = [0] * (n + 5)
        sol = [0] * q
        self.depth = 0
        self.dfs(g, qu, 0, -1, ans, sol)

        for i in range(q):
            print(sol[i] + 1)

    def dfs(self, g, qu, s, par, ans, sol):
        ans[self.depth] = s
        self.depth += 1

        for query in qu[s]:
            if (self.depth - query.x - 1) < 0:
                sol[query.id] = -2
            else:
                sol[query.id] = ans[self.depth - query.x - 1]

        for neighbor in g[s]:
            if neighbor != par:
                self.dfs(g, qu, neighbor, s, ans, sol)

        self.depth -= 1


if __name__ == "__main__":
    Main().run()
