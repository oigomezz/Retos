from collections import defaultdict

MAXN = 200005
LGN = 18


class Event:
    def __init__(self, a, b, c, d=None):
        if d is None:
            self.type = 1
            self.v1 = b
            self.v2 = -1
            self.val = c
            self.index = a
        else:
            self.type = 2
            self.v1 = b
            self.v2 = c
            self.val = d
            self.index = a


sieve = [False] * MAXN
ans = [False] * MAXN
curr_time = 0
factor = [0] * MAXN
cval = [0] * MAXN
depth = [0] * MAXN
BIT = [0] * MAXN
subtree_start = [0] * MAXN
subtree_end = [0] * MAXN
par = [[0] * LGN for _ in range(MAXN)]
G = defaultdict(list)
to_process = defaultdict(list)


def factorise(x):
    ret = []
    while x > 1:
        ctr = 0
        cfact = factor[x]
        while factor[x] == cfact:
            ctr += 1
            x //= cfact
        ret.append((cfact, ctr))
    return ret


def bit_upd(pos, val):
    while pos < MAXN:
        BIT[pos] += val
        pos += (pos & -pos)


def bit_get(pos):
    ret = 0
    while pos > 0:
        ret += BIT[pos]
        pos -= (pos & -pos)
    return ret


def add_val_to_subtree(root, val):
    bit_upd(subtree_start[root], val)
    bit_upd(subtree_end[root] + 1, -val)


def get_path_val(pos):
    return bit_get(subtree_start[pos])


def dfs(pos, prev):
    global curr_time
    par[pos][0] = prev
    depth[pos] = depth[prev] + 1
    curr_time += 1
    subtree_start[pos] = curr_time
    for neighbor in G[pos]:
        if neighbor != prev:
            dfs(neighbor, pos)
    subtree_end[pos] = curr_time


def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    for i in range(LGN):
        if diff & (1 << i):
            u = par[u][i]
    if u == v:
        return u
    for i in range(LGN - 1, -1, -1):
        if par[u][i] != par[v][i]:
            u = par[u][i]
            v = par[v][i]
    return par[u][0]


for i in range(2, MAXN):
    if not sieve[i]:
        for j in range(i, MAXN, i):
            factor[j] = i
            sieve[j] = True

n, q = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(1, n + 1):
    cval[i] = arr[i - 1]
    pfact = factorise(arr[i - 1])
    for p, c in pfact:
        to_process[p].append(Event(0, i, c))

for _ in range(n - 1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

queries = []
for i in range(1, q + 1):
    line = list(map(int, input().split()))
    ty = line[0]
    if ty == 1:
        x, y = line[1], line[2]
        oldfact = factorise(cval[x])
        for p, _ in oldfact:
            to_process[p].append(Event(i, x, 0))
        cval[x] = y
        pfact = factorise(y)
        for p, c in pfact:
            to_process[p].append(Event(i, x, c))
    else:
        u, v, k = line[1], line[2], line[3]
        pfact = factorise(k)
        for p, c in pfact:
            to_process[p].append(Event(i, u, v, c))
        queries.append(i)
    ans[i] = True

dfs(1, 0)
for j in range(1, LGN):
    for i in range(1, n + 1):
        par[i][j] = par[par[i][j - 1]][j - 1]

cval = [0] * MAXN
for p in range(2, MAXN):
    changed = []
    for event in to_process[p]:
        if event.type == 1:
            set_to = event.val
            node = event.v1
            curr_val = cval[node]
            add_val_to_subtree(node, set_to - curr_val)
            cval[node] = set_to
            changed.append(node)
        else:
            u, v = event.v1, event.v2
            l = lca(u, v)
            path_sum = get_path_val(u) + get_path_val(v) - \
                get_path_val(l) - get_path_val(par[l][0])
            if path_sum < event.val:
                ans[event.index] = False
    changed = sorted(set(changed))

for i in queries:
    print("YES" if ans[i] else "NO")
