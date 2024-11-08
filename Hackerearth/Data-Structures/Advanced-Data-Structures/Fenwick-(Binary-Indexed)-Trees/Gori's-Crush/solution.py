bit = [0] * 600050


def up(j, x):
    while j <= 600010:
        bit[j] += x
        j += j & (-j)


def query(j):
    x = 0
    while j > 0:
        x += bit[j]
        j -= j & (-j)
    return x


def main():
    n, q, m = map(int, input().split())
    v = list(map(int, input().split()))
    vp = []
    for i in range(n):
        vp.append((v[i], (i, -1)))

    que = []
    for i in range(q):
        line = list(map(int, input().split()))
        t = line[0]
        if t == 0:
            x = line[1] - 1
            y = line[2]
            que.append(((x, y), (0, 0)))
            vp.append((y, (i, 0)))
        else:
            a = line[1]
            b = line[2]
            c = line[3]
            d = line[4]
            que.append(((a, b), (c, d)))
            vp.append((a, (i, 1)))
            vp.append((b, (i, 2)))
            vp.append((c, (i, 3)))
            vp.append((d, (i, 4)))

    vp.sort()
    d = len(vp)
    i = 0
    k = 1
    j = 0

    while i < d:
        while j < d and vp[i][0] == vp[j][0]:
            if vp[j][1][1] == -1:
                v[vp[j][1][0]] = k
            elif vp[j][1][1] == 0:
                que[vp[j][1][0]][0][1] = k
            elif vp[j][1][1] == 1:
                que[vp[j][1][0]][0][0] = k
            elif vp[j][1][1] == 2:
                que[vp[j][1][0]][0][1] = k
            elif vp[j][1][1] == 3:
                que[vp[j][1][0]][1][0] = k
            elif vp[j][1][1] == 4:
                que[vp[j][1][0]][1][1] = k
            j += 1
        i = j
        k += 1

    for i in range(n):
        up(v[i], 1)

    output = []
    for i in range(q):
        if que[i][1][0] == 0:
            up(v[que[i][0][0]], -1)
            up(que[i][0][1], 1)
            v[que[i][0][0]] = que[i][0][1]
        else:
            c = 0
            a = max(que[i][0][0], que[i][1][0])
            b = min(que[i][0][1], que[i][1][1])
            if a <= b:
                c = query(b) - query(a - 1)
            if c < m:
                output.append("Do not propose")
            else:
                output.append("Propose")

    print("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
