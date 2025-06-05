class Unionfind:
    def __init__(self):
        self.parent = list(range(10**5 + 1))
        self.rank = [0] * (10**5 + 1)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        r_u, r_v = self.find(u), self.find(v)

        if r_u != r_v:
            if self.rank[r_u] < self.rank[r_v]:
                self.parent[r_u] = r_v
            elif self.rank[r_u] > self.rank[r_v]:
                self.parent[r_v] = r_u
            else:
                self.parent[r_u] = r_v
                self.rank[r_u] += 1
            return True
        return False


if __name__ == "__main__":
    adj = [[] for _ in range(10**5 + 1)]
    n = int(input())
    arr = list(map(int, str(input()).split(' ')))
    uf = Unionfind()

    for i in range(n):
        adj[arr[i]].append(i)

    ans = 0
    for i in range(10**5, 0, -1):
        v = -1
        for j in range(i, 10**5 + 1, i):
            for x in adj[j]:
                if v == -1:
                    v = x
                elif uf.union(v, x):
                    ans += i
    print(ans)
