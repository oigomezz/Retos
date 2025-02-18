import sys

T = [''] * 1000005
sa = [0] * 1000005
tsa = [0] * 1000005
ra = [0] * 1000005
tra = [0] * 1000005
lcp = [0] * 1000005
plcp = [0] * 1000005
phi = [0] * 1000005
c = [0] * 1000005
K, n, N = 0, 0, 0


def sort(k):
    global N
    c[:] = [0] * len(c)
    for i in range(N):
        c[ra[i + k] if i + k < N else 0] += 1
    suma = 0
    maxi = max(300, N)
    for i in range(maxi):
        t = c[i]
        c[i] = suma
        suma += t
    for i in range(N):
        cur = ra[sa[i] + k] if sa[i] + k < N else 0
        tsa[c[cur]] = sa[i]
        c[cur] += 1
    sa[:] = tsa[:N]


def build_sa():
    global N
    for i in range(N):
        ra[i] = ord(T[i])
        sa[i] = i
    k = 1
    while k < N:
        sort(k)
        sort(0)
        r = tra[sa[0]] = 0
        for i in range(1, N):
            if ra[sa[i]] == ra[sa[i - 1]]:
                cur = ra[sa[i] + k] if sa[i] + k < N else 0
                prev = ra[sa[i - 1] + k] if sa[i - 1] + k < N else 0
                tra[sa[i]] = r if cur == prev else r + 1
                if cur != prev:
                    r += 1
            else:
                tra[sa[i]] = r + 1
                r += 1
        if tra[sa[N - 1]] == N - 1:
            break
        ra[:] = tra[:N]


def build_lcp():
    phi[sa[0]] = -1
    for i in range(1, N):
        phi[sa[i]] = sa[i - 1]
    l = 0
    for i in range(N):
        if phi[i] == -1:
            plcp[i] = 0
            continue
        while T[i + l] == T[phi[i] + l]:
            l += 1
        plcp[i] = l
        l = max(l - 1, 0)
    for i in range(N):
        lcp[i] = plcp[sa[i]]


if __name__ == "__main__":
    K, n = map(int, input().split())
    T = list(input().strip())
    N = len(T)
    if K == 1:
        print(N)
        sys.exit(0)
    T.append('$')
    N += 1
    build_sa()
    build_lcp()
    ms = sorted(lcp[1:K])
    ans = max(1, ms[0])
    for i in range(K, N):
        ms.remove(lcp[i - K + 1])
        ms.append(lcp[i])
        ms.sort()
        ans = max(ans, ms[0])
    print(ans)
