def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z


def sort_cyclic_shifts(s):
    n = len(s)
    alphabet = 256
    p, c = initialize_p_and_c(s, n, alphabet)
    classes = assign_classes(s, n, p, c)
    p = update_p_and_c(n, p, c, classes)
    return p


def initialize_p_and_c(s, n, alphabet):
    p = list(range(n))
    c = [0] * n
    cnt = [0] * max(alphabet, n)
    for i in range(n):
        cnt[ord(s[i])] += 1
    for i in range(1, alphabet):
        cnt[i] += cnt[i - 1]
    for i in range(n):
        p[cnt[ord(s[i])] - 1] = i
        cnt[ord(s[i])] -= 1
    return p, c


def assign_classes(s, n, p, c):
    c[p[0]] = 0
    classes = 1
    for i in range(1, n):
        if s[p[i]] != s[p[i - 1]]:
            classes += 1
        c[p[i]] = classes - 1
    return classes


def update_p_and_c(n, p, c, classes):
    pn = [0] * n
    cn = [0] * n
    for h in range(20):
        if (1 << h) >= n:
            break
        for i in range(n):
            pn[i] = (p[i] - (1 << h)) % n
        cnt = [0] * classes
        for i in range(n):
            cnt[c[pn[i]]] += 1
        for i in range(1, classes):
            cnt[i] += cnt[i - 1]
        for i in range(n - 1, -1, -1):
            p[cnt[c[pn[i]]] - 1] = pn[i]
            cnt[c[pn[i]]] -= 1
        cn[p[0]] = 0
        classes = 1
        for i in range(1, n):
            cur = (c[p[i]], c[(p[i] + (1 << h)) % n])
            prev = (c[p[i - 1]], c[(p[i - 1] + (1 << h)) % n])
            if cur != prev:
                classes += 1
            cn[p[i]] = classes - 1
        c, cn = cn, c
    return p


def flip(s):
    return ''.join('1' if x == '0' else '0' for x in s)


t = int(input())
results = []
for _ in range(t):
    n, p = map(int, input().split())
    s = input()
    s = flip(s)
    z = z_function(s)
    period = n
    for i in range(1, n):
        if i + z[i] == n and n % i == 0:
            period = i
            break
    A = s[:period]
    v = sort_cyclic_shifts(A)
    ans = v[0] + (p - 1) * period
    print(str(ans))
