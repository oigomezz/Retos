def power(base, exponent):
    if exponent == 0:
        return 1
    result = 1
    value = base
    while exponent:
        if exponent % 2:
            result *= value
            result %= 1000000007
        value *= value
        value %= 1000000007
        exponent //= 2
    return result


def ncr(n, r):
    if n < r or n < 0 or r < 0:
        return 0
    result = factorial[n]
    result *= inv_factorial[n - r]
    result %= 1000000007
    result *= inv_factorial[r]
    result %= 1000000007
    return result


def solve(x, total_sum):
    count = 0
    for i in range(x + 1):
        value = ncr(x, i) * ncr(total_sum + x - 1, x - 1)
        value %= 1000000007
        total_sum -= 10
        if i % 2 == 0:
            count += value
            count %= 1000000007
        else:
            count -= value
            count += 1000000007
            count %= 1000000007
    return count


factorial = [0] * 100005
inv_factorial = [0] * 100005
factorial[0] = factorial[1] = 1
inv_factorial[0] = inv_factorial[1] = 1

for i in range(2, 100001):
    factorial[i] = factorial[i - 1] * i
    factorial[i] %= 1000000007
    inv_factorial[i] = inv_factorial[i - 1] * power(i, 1000000005)
    inv_factorial[i] %= 1000000007

t = int(input())
for _ in range(t):
    s = int(input())
    temp = s
    value = 1
    answer = 0
    count = 0
    while temp:
        count += 1
        temp //= 10
    for i in range(1, count + 1):
        if s % value == 0:
            total_sum = s // value
            if 0 <= total_sum <= 9 * i:
                answer += solve(i, total_sum)
                answer %= 1000000007
        value *= 10
        value += 1
    print(answer)
