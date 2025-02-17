N = 100005
n = 0
a = [[0] * N for _ in range(5)]
tree = [[[0] * N for _ in range(5)] for _ in range(5)]


def update(i, v, tree):
    while i <= n:
        tree[i] += v
        i += i & -i


def query(i, tree):
    ret = 0
    while i > 0:
        ret += tree[i]
        i -= i & -i
    return ret


n = int(input().strip())
for j in range(5):
    a[j] = [0] + list(map(int, input().strip().split()))

str_input = input().strip()
str_input = ' ' + str_input

p = [0, 1, 2, 3, 4]
for k in range(5):
    for j in range(5):
        for i in range(1, n + 1):
            if ord(str_input[i]) - ord('A') == k:
                update(i, a[j][i], tree[k][j])

q = int(input().strip())

for _ in range(q):
    ch, *line = input().strip().split()
    if ch == 'Qe':
        x, y = line
        p[ord(x) - ord('A')], p[ord(y) - ord('A')
                                ] = p[ord(y) - ord('A')], p[ord(x) - ord('A')]
    elif ch == 'Qc':
        x, y = line
        x = int(x)
        for i in range(5):
            update(x, -a[i][x], tree[ord(str_input[x]) - ord('A')][i])
        for i in range(5):
            update(x, a[i][x], tree[ord(y) - ord('A')][i])
        str_input = str_input[:x] + y + str_input[x + 1:]
    else:
        x, y = line
        x = int(x)
        y = int(y)
        ans = 0
        for i in range(5):
            ans += query(y, tree[i][p[i]]) - query(x - 1, tree[i][p[i]])
        print(ans)
