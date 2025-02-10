f = [[0] * 10 for _ in range(1000002)]
s = ""
n = 0


def update(i, j, val):
    k = i
    while k <= n:
        f[k][j] += val
        k += (k & -k)


def suma(i, j):
    k = i
    ret = 0
    while k > 0:
        ret += f[k][j]
        k -= (k & -k)
    return ret


s = input()
n = len(s)

for i in range(n):
    update(i + 1, int(s[i]), 1)

q = int(input())
for _ in range(q):
    line = list(map(int, input().split()))
    t = int(line[0])
    if t == 1:
        x, y = line[1], line[2]
        update(x, int(s[x - 1]), -1)
        s = s[:x - 1] + str(y) + s[x:]
        update(x, y, 1)
    else:
        l, r, x = line[1], line[2], line[3]
        vals = [suma(r, i) - suma(l - 1, i) for i in range(10)]
        mod = sum(i * vals[i] for i in range(10)) % 9
        vals[9 - mod] += 1
        for i in range(9, -1, -1):
            if x <= vals[i]:
                print(i)
                break
            x -= vals[i]
