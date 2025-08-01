from collections import defaultdict

MOD = 1000000007
m = defaultdict(int)


def fpow(num, b):
    res = 1
    while b:
        if b & 1:
            res = (res * num) % MOD
        num = (num * num) % MOD
        b >>= 1
    return res


def rec(num):
    if num <= 2:
        return 1
    if num in m:
        return m[num]
    num -= 1
    ans = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i:
            continue
        x, y = i, num // i
        if num // x >= 2:
            ans = (ans + fpow(rec(x), num // x)) % MOD
        if x != y and (num // y) >= 2:
            ans = (ans + fpow(rec(y), num // y)) % MOD
    m[num + 1] = ans
    return ans


if __name__ == "__main__":
    n = int(input())
    m[1] = m[2] = 1
    print(rec(n))
