n, q = map(int, input().split())
sum_array = [[[0 for _ in range(2)] for _ in range(30)] for _ in range(n)]
xs = [0] * n
x = 0

arr = list(map(int, input().split()))
for i in range(n):
    v = arr[i]
    x ^= v
    xs[i] = x
    for j in range(30):
        sum_array[i][j][(x & (1 << j)) != 0] = 1
    if i > 0:
        for j in range(30):
            for k in range(2):
                sum_array[i][j][k] += sum_array[i - 1][j][k]

for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    pre = xs[l - 1] if l > 0 else 0
    ans = 0
    for i in range(30):
        f = not (pre & (1 << i))
        now = sum_array[r][i][f] - (sum_array[l - 1][i][f] if l > 0 else 0)
        ans += now * (1 << i)
    print(ans)
