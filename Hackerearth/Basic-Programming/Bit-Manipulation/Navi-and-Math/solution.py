import sys


def power(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result


def main():
    t = int(input())
    assert 1 <= t <= 10
    for tt in range(1, t + 1):
        n = int(input())
        assert 2 <= n <= 16
        a = list(map(int, input().split()))
        for i in a:
            assert 1 <= i <= 10000000
        p = 1 << n
        ans = -sys.maxsize - 1
        for i in range(1, p):
            mul = 1
            add = 0
            ctr = 0
            for j in range(n):
                if i & (1 << j):
                    ctr += 1
                    add = (add + a[j]) % 1000000007
                    mul = (mul * a[j]) % 1000000007
            if ctr >= 2:
                temp = power(add, 1000000005, 1000000007)
                temp = (temp * mul) % 1000000007
                ans = max(ans, temp)
        print(f"Case #{tt}: {ans}")


if __name__ == "__main__":
    main()
