class F:
    maxn = int(1e4 + 14)
    maxm = 20 * maxn
    inf = int(1e9)
    so = maxn - 1
    si = maxn - 2
    ptr = [0] * maxn
    head = [-1] * maxn
    prv = [0] * maxm
    to = [0] * maxm
    cap = [0] * maxm
    d = [0] * maxn
    q = [0] * maxn
    ec = 0

    @staticmethod
    def init():
        F.head = [-1] * F.maxn
        F.ec = 0

    @staticmethod
    def add(v, u, vu, uv=0):
        F.to[F.ec] = u
        F.prv[F.ec] = F.head[v]
        F.cap[F.ec] = vu
        F.head[v] = F.ec
        F.ec += 1
        F.to[F.ec] = v
        F.prv[F.ec] = F.head[u]
        F.cap[F.ec] = uv
        F.head[u] = F.ec
        F.ec += 1

    @staticmethod
    def bfs():
        F.d = [float('inf')] * F.maxn
        F.d[F.so] = 0
        h = 0
        t = 0
        F.q[t] = F.so
        t += 1
        while h < t:
            v = F.q[h]
            h += 1
            e = F.head[v]
            while e >= 0:
                if F.cap[e] and F.d[F.to[e]] > F.d[v] + 1:
                    F.d[F.to[e]] = F.d[v] + 1
                    F.q[t] = F.to[e]
                    t += 1
                    if F.to[e] == F.si:
                        return True
                e = F.prv[e]
        return False

    @staticmethod
    def dfs(v, f=float('inf')):
        if v == F.si or f == 0:
            return f
        r = 0
        e = F.ptr[v]
        while e >= 0:
            if F.d[v] == F.d[F.to[e]] - 1:
                x = F.dfs(F.to[e], min(f, F.cap[e]))
                f -= x
                r += x
                F.cap[e] -= x
                F.cap[e ^ 1] += x
                if f == 0:
                    break
            e = F.prv[e]
        return r

    @staticmethod
    def mf():
        ans = 0
        while F.bfs():
            F.ptr = F.head[:]
            ans += F.dfs(F.so)
        return ans


MAX_N = int(1e2 + 14)

h = int(input().strip())

F.init()
for i in range(h):
    line = list(map(int, input().strip().split()))
    for j in range(h):
        x = line[j]
        x ^= x != 2 and (i + j) % 2
        if x == 0:
            F.add(F.so, i * h + j, F.inf)
        elif x == 1:
            F.add(i * h + j, F.si, F.inf)
        if i + 1 < h:
            F.add(i * h + j, i * h + h + j, 1)
            F.add(i * h + h + j, i * h + j, 1)
        if j + 1 < h:
            F.add(i * h + j, i * h + j + 1, 1)
            F.add(i * h + j + 1, i * h + j, 1)

print(h * (h - 1) * 2 - F.mf())
