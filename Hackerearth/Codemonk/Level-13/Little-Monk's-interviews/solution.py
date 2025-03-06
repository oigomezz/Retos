def get(x):
    if x == w[x]:
        return x
    w[x] = get(w[x])
    return w[x]


def merge(a, b):
    w[a] = b


tests = int(input())
for _ in range(tests):
    n, m = map(int, input().split())
    a = [0] * (m + 1)
    b = [0] * (m + 1)
    c = [0] * (m + 1)
    v = []

    for i in range(1, m + 1):
        arr = list(map(int, input().split()))
        a[i] = arr[0]
        b[i] = arr[1]
        c[i] = arr[2]
        v.append((c[i], i))

    v.sort(reverse=True, key=lambda x: x[0])

    w = list(range(n + 1))
    ans = 0
    for i in range(len(v)):
        id = v[i][1]
        q = a[id]
        w_id = b[id]
        q = get(q)
        w_id = get(w_id)

        if q != w_id:
            ans += c[id]
            merge(q, w_id)

    print(str(ans))
