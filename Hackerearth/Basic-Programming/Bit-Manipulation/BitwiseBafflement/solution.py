t = int(input())
results = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    sg = 0
    x = [0] * (n + 1)
    s = [0] * (n + 1)

    for i in range(n):
        sg ^= a[i]
        x[i + 1] = bin(sg).count('1') % 2
        s[i + 1] = s[i] + x[i]

    ret = 0
    b = []
    c = [(0, 0)]

    for p in range(n):
        val = a[p]
        s0 = 0
        b.clear()
        b.append((val, p + 1))

        for t in c:
            new_val = (val & t[0])
            if new_val != val:
                val = new_val
                b.append((val, t[1]))

        c = b.copy()
        for i in range(len(c)):
            if bin(c[i][0]).count('1') % 2 == 1:
                j = (i + 1 < len(c) and c[i + 1][1]) or 0
                k = c[i][1]
                if x[p + 1] == 0:
                    s0 += (k - j) - (s[k] - s[j])
                else:
                    s0 += s[k] - s[j]
        ret += s0
    results.append(str(ret))
print("\n".join(results))
