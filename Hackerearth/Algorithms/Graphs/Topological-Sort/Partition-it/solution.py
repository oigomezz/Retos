import math


def bpow(x, n, mod):
    ans = 1
    while n > 0:
        if n & 1:
            ans *= x
        x *= x
        ans %= mod
        x %= mod
        n //= 2
    return ans


if __name__ == "__main__":
    tests = int(input())
    for _ in range(tests):
        P, N = map(int, input().split())
        divs = []
        sz = int(math.sqrt(P - 1))
        num = P - 1
        maxLen = 0
        A = list(map(int, input().split()))
        dp = [0] * N
        for j in range(1, sz + 1):
            if num % j == 0:
                divs.append(j)
                if j != num // j:
                    divs.append(num // j)
        divs.sort()
        periods = []
        for i in range(N):
            cur = 1
            for d in divs:
                if bpow(A[i], d, P) == 1:
                    periods.append(d)
                    break

        periods.sort()
        for i in range(N - 1, -1, -1):
            dp[i] = 1
            for j in range(i + 1, N):
                if periods[j] % periods[i] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
            maxLen = max(maxLen, dp[i])

        print(maxLen)
