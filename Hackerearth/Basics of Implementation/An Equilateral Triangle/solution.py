M = 10**9 + 7
fact = [0] * 10001
fact[0] = 1


def factorial():
    for i in range(1, 10001):
        fact[i] = (fact[i-1] * i) % M


def inv(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return inv((x * x) % M, n // 2)
    else:
        return (x * inv((x * x) % M, (n-1) // 2)) % M


def ncr(n, r):
    if r > n:
        return 0
    ans = fact[n]
    x = (fact[r] * fact[n-r]) % M
    ans = (ans * inv(x, M-2)) % M
    return ans


def main():
    n = int(input())
    factorial()
    res = 0
    for i in range(n, 2, -1):
        for j in range(i-2, 0, -2):
            res = (res + ncr(j+1, 2)) % M
    print(res)


if __name__ == "__main__":
    main()
