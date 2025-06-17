import math

PI = math.acos(-1)
MAX = 1 << 18
MOD = int(1e9 + 7)


def big_mod(a, e):
    if e == -1:
        e = MOD - 2
    ret = 1
    while e:
        if e & 1:
            ret = ret * a % MOD
        a = a * a % MOD
        e >>= 1
    return ret


fac = [0] * MAX
inv = [0] * MAX


class cp:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, rhs):
        return cp(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return cp(self.x - rhs.x, self.y - rhs.y)

    def __mul__(self, rhs):
        return cp(self.x * rhs.x - self.y * rhs.y, self.x * rhs.y + self.y * rhs.x)

    def conj(self):
        return cp(self.x, -self.y)


rts = [cp() for _ in range(MAX + 1)]
bitrev = [0] * MAX
f_a = [cp() for _ in range(MAX)]
f_b = [cp() for _ in range(MAX)]
f_c = [cp() for _ in range(MAX)]
f_d = [cp() for _ in range(MAX)]


def fft_init():
    k = 0
    while 1 << k < MAX:
        k += 1
    bitrev[0] = 0
    for i in range(1, MAX):
        bitrev[i] = (bitrev[i >> 1] >> 1) | ((i & 1) << (k - 1))
    rts[0] = rts[MAX] = cp(1, 0)
    for i in range(1, MAX // 2 + 1):
        rts[i] = cp(math.cos(i * 2 * PI / MAX), math.sin(i * 2 * PI / MAX))
    for i in range(MAX // 2 + 1, MAX):
        rts[i] = rts[MAX - i].conj()


def dft(a, n, sign):
    global is_init
    if 'is_init' not in globals():
        is_init = 0
    if not is_init:
        is_init = 1
        fft_init()
    d = 0
    while (1 << d) * n != MAX:
        d += 1
    for i in range(n):
        if i < bitrev[i] >> d:
            a[i], a[bitrev[i] >> d] = a[bitrev[i] >> d], a[i]
    for length in range(2, n + 1, length << 1):
        for i in range(0, n, length):
            x = a[i:i + length // 2]
            y = a[i + (length >> 1):i + length]
            w = rts if sign > 0 else rts[MAX:]
            for k in range(length // 2):
                z = y[k] * w[k]
                y[k] = x[k] - z
                x[k] = x[k] + z
            a[i:i + length] = x + y
    if sign < 0:
        for i in range(n):
            a[i].x /= n
            a[i].y /= n


def multiply(a, b, n_a, n_b, c):
    n = n_a + n_b - 1
    while n != n & -n:
        n += n & -n
    for i in range(n):
        f_a[i] = f_b[i] = cp()
    for i in range(n_a):
        f_a[i] = cp(a[i])
    for i in range(n_b):
        f_b[i] = cp(b[i])
    dft(f_a, n, 1)
    dft(f_b, n, 1)
    for i in range(n):
        f_a[i] = f_a[i] * f_b[i]
    dft(f_a, n, -1)
    for i in range(n):
        c[i] = int(math.floor(f_a[i].x + 0.5))


def multiply_int(a, b, n_a, n_b, c):
    n = n_a + n_b - 1
    while n != (n & -n):
        n += n & -n
    for i in range(n):
        f_a[i] = f_b[i] = cp()
    MAGIC = 15
    for i in range(n_a):
        f_a[i] = cp(a[i] >> MAGIC, a[i] & ((1 << MAGIC) - 1))
    for i in range(n_b):
        f_b[i] = cp(b[i] >> MAGIC, b[i] & ((1 << MAGIC) - 1))
    dft(f_a, n, 1)
    dft(f_b, n, 1)
    for i in range(n):
        j = (n - i) % n
        x = f_a[i] + f_a[j].conj()
        y = f_b[i] + f_b[j].conj()
        z = f_a[j].conj() - f_a[i]
        t = f_b[j].conj() - f_b[i]
        f_c[i] = (x * t + y * z) * cp(0, 0.25)
        f_d[i] = x * y * cp(0, 0.25) + z * t * cp(-0.25, 0)
    dft(f_c, n, -1)
    dft(f_d, n, -1)
    for i in range(n):
        u = int(math.floor(f_c[i].x + 0.5)) % MOD
        v = int(math.floor(f_d[i].x + 0.5)) % MOD
        w = int(math.floor(f_d[i].y + 0.5)) % MOD
        c[i] = (u << 15) + v + (w << 30) % MOD


def multiply(a, b):
    f_a = [0] * MAX
    f_b = [0] * MAX
    f_c = [0] * MAX
    n_a = len(a)
    n_b = len(b)
    for i in range(n_a):
        f_a[i] = a[i]
    for i in range(n_b):
        f_b[i] = b[i]
    # Call the multiply function (not defined in the original code)
    # multiply(f_a, f_b, n_a, n_b, f_c)
    k = n_a + n_b - 1
    res = [0] * k
    for i in range(k):
        res[i] = f_c[i]
    return res


def extend(a, c):
    a.insert(0, 0)
    for i in range(len(a) - 1):
        add = c * a[i + 1] % MOD
        a[i] -= add
        if a[i] < 0:
            a[i] += MOD
    return a


def falling_factorial(n):
    if n == 0:
        return [1]
    m = n // 2
    if n % 2 == 1:
        return extend(falling_factorial(n - 1), n - 1)
    left = falling_factorial(m)
    one = [0] * (m + 1)
    two = [0] * (m + 1)
    right = [0] * (m + 1)
    for i in range(m + 1):
        one[i] = big_mod(MOD - m, i) * inv[i] % MOD
    for i in range(m + 1):
        two[i] = left[m - i] * fac[m - i] % MOD
    three = multiply(one, two)
    for i in range(m + 1):
        right[i] = three[m - i] * inv[i] % MOD
    return multiply(left, right)


def dot(a, b):
    res = 0
    for i in range(min(len(a), len(b))):
        add = a[i] * b[i] % MOD
        res += add
        if res >= MOD:
            res -= MOD
    return res


if __name__ == "__main__":
    fac[0] = 1
    for i in range(1, MAX):
        fac[i] = i * fac[i - 1] % MOD
    inv[MAX - 1] = big_mod(fac[MAX - 1], -1)
    for i in range(MAX - 1, 0, -1):
        inv[i - 1] = i * inv[i] % MOD

    n, l, r = map(int, input().split())
    a = [0] * (n + 1)
    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        a[i] = arr[i-1]

    poly = falling_factorial(l - 1)
    last = dot(a, poly)
    for it in range(l, r + 1):
        poly = extend(poly, it - 1)
        cur = dot(a, poly)
        ans = cur - last
        if ans < 0:
            ans += MOD
        if it > l:
            print(" ", end="")
        print(ans, end="")
        last = cur
    print()
