def is_true(s, r):
    l = 0
    po = 1
    for i in range(61, -1, -1):
        if s[i] == '1':
            l += po
        po *= 2
    return l <= r


def to_long(s):
    l = 0
    po = 1
    for i in range(61, -1, -1):
        if s[i] == '1':
            l += po
        po *= 2
    return l


def more_bit(l, r, k, l_bits):
    sl = f'{l:062b}'
    for i in range(61, -1, -1):
        if sl[i] == '0':
            sl = sl[:i] + '1' + sl[i+1:]
            l_bits += 1
        if is_true(sl, r) and l_bits == k:
            return to_long(sl)
    return -1


def less_bit(l, r, k, l_bits):
    co = 0
    sl = f'{l:062b}'
    for i in range(61, -1, -1):
        if sl[i] == '1':
            co += 1
        if sl[i] == '0':
            s = sl[:i] + '1' + '0' * (61 - i)
            if is_true(s, r) and l_bits - co + 1 == k:
                return to_long(s)
            if is_true(s, r) and l_bits - co + 1 < k:
                return more_bit(to_long(s), r, k, l_bits - co + 1)
    return -1


def fun(l, r, k):
    sl = f'{l:062b}'
    sr = f'{r:062b}'
    set_bit = 0
    for i in range(62):
        if sl[i] != sr[i]:
            break
        if sl[i] == '1':
            set_bit += 1
    if set_bit > k:
        return -1
    l_set_bit = sum(1 for bit in sl if bit == '1')
    if l_set_bit < k:
        return more_bit(l, r, k, l_set_bit)
    if l_set_bit == k:
        return l
    return less_bit(l, r, k, l_set_bit)


def solve():
    l, r, k = map(int, input().split())
    print(fun(l, r, k))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
