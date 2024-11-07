n = 0
q = 0
index = [0] * 100001
bit = [0] * 100001
b = [0] * 100001
ans = [0] * 100001
v = []


def update(i, val):
    global n
    i += 1
    while i <= n:
        bit[i] += val
        i += i & (-i)


def query(i):
    s = 0
    i += 1
    while i > 0:
        s += bit[i]
        i -= i & (-i)
    return s


if __name__ == "__main__":
    n = int(input())
    arr_a = list(map(int, input().split()))
    for i in range(n):
        a = arr_a[i]
        index[a] = i

    arr_b = list(map(int, input().split()))
    for i in range(n):
        b[i] = arr_b[i]

    q = int(input())
    for i in range(q):
        line = list(map(int, input().split()))
        l1 = int(line[0]) - 1
        r1 = int(line[1]) - 1
        l2 = int(line[2]) - 1
        r2 = int(line[3]) - 1
        ans[i] = r1 - l1 + 1
        v.append([l2, l1, r1, 1, i])
        v.append([r2, l1, r1, -1, i])

    v.sort()
    j = 0

    for i in range(n):
        k = j
        while k < len(v):
            cur = v[k]
            if cur[0] != i:
                break
            if cur[3] == 1:
                ans[cur[4]] += query(cur[2]) - query(cur[1] - 1)
            k += 1

        update(index[b[i]], 1)

        k = j
        while k < len(v):
            cur = v[k]
            if cur[0] != i:
                break
            if cur[3] == -1:
                ans[cur[4]] -= query(cur[2]) - query(cur[1] - 1)
            k += 1

        j = k

    for i in range(q):
        print(ans[i])
