def msb(x):
    return 63 - (x.bit_length() - 1)


def bitwise_and(l, r):
    return l & ~((1 << (msb(l ^ r) + 1)) - 1) if msb(l) == msb(r) else 0


def solve(l, r, k):
    if k == 1:
        return r
    m = 1 << msb(r)
    u = m - 1
    v = k - 1
    if r - l == v:
        return bitwise_and(l, r)
    ans = 0
    if u - l >= v:
        ans = max(ans, bitwise_and(u - v, u))
    if r - m >= v:
        ans = max(ans, bitwise_and(r - v, r))
    return ans


def main():
    Q = int(input())
    results = []
    for _ in range(Q):
        l, r, k = map(int, input().split())
        results.append(solve(l, r, k))
    print('\n'.join(map(str, results)))


if __name__ == "__main__":
    main()
