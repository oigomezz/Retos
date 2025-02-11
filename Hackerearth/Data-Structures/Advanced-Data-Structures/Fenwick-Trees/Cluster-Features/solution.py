MAXX = 150005
N = 20005
x = [0] * MAXX
y = [0] * MAXX
queryx1 = [0] * MAXX
queryx2 = [0] * MAXX
queryy1 = [0] * MAXX
queryy2 = [0] * MAXX


class BorderState:
    OPEN = 0
    POINT = 1
    CLOSE = 2


class SegmentBorder:
    def __init__(self, state, yd, yu, x, idx):
        self.state = state
        self.yd = yd
        self.yu = yu
        self.x = x
        self.idx = idx

    def __lt__(self, other):
        return (self.x < other.x) or (self.x == other.x and self.state < other.state)


class BIT:
    def __init__(self):
        self.n = 0
        self.ls = 0
        self.ss = 0

    def __add__(self, other):
        return BIT().set(self.n + other.n, self.ls + other.ls, self.ss + other.ss)

    def __sub__(self, other):
        return BIT().set(self.n - other.n, self.ls - other.ls, self.ss - other.ss)

    def set(self, n, ls, ss):
        self.n = n
        self.ls = ls
        self.ss = ss
        return self


B = [BIT() for _ in range(N)]
ans = [[BIT() for _ in range(MAXX)] for _ in range(2)]


def update_bit(idx, val):
    valss = val * val
    while idx < N:
        B[idx].n += 1
        B[idx].ls += val
        B[idx].ss += valss
        idx += idx & -idx


def get_bit(idx):
    ret = BIT().set(0, 0, 0)
    while idx > 0:
        ret.n += B[idx].n
        ret.ls += B[idx].ls
        ret.ss += B[idx].ss
        idx -= idx & -idx
    return ret


def get(l, r):
    return get_bit(r) - get_bit(l - 1)


def solve(p, q, turn):
    borders = []
    for i in range(p):
        borders.append(SegmentBorder(BorderState.POINT, y[i], -1, x[i], -1))

    for i in range(q):
        left_border = SegmentBorder(
            BorderState.OPEN, queryy1[i], queryy2[i], queryx1[i], i)
        right_border = SegmentBorder(
            BorderState.CLOSE, queryy1[i], queryy2[i], queryx2[i], i)

        borders.append(left_border)
        borders.append(right_border)

    borders.sort()

    for border in borders:
        if border.state == BorderState.POINT:
            update_bit(border.yd, border.x)
        elif border.state == BorderState.OPEN:
            val = get(border.yd, border.yu)
            ans[turn][border.idx] = ans[turn][border.idx] - val
        elif border.state == BorderState.CLOSE:
            val = get(border.yd, border.yu)
            ans[turn][border.idx] = ans[turn][border.idx] + val


def magic(t):
    ret = t.n * t.ss - t.ls * t.ls
    ret *= 3
    ret += t.ls
    return ret


def main():
    p, q = map(int, input().split())
    for i in range(p):
        x[i], y[i] = map(int, input().split())
    for i in range(q):
        queryx1[i], queryx2[i], queryy1[i], queryy2[i] = map(
            int, input().split())

    solve(p, q, 0)

    for i in range(p):
        x[i], y[i] = y[i], x[i]

    for i in range(q):
        queryx1[i], queryy1[i] = queryy1[i], queryx1[i]
        queryx2[i], queryy2[i] = queryy2[i], queryx2[i]

    for i in range(N):
        B[i] = BIT()

    solve(p, q, 1)

    for i in range(q):
        val = magic(ans[0][i]) + magic(ans[1][i])
        print(val)


if __name__ == "__main__":
    main()
