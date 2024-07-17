def actual_sum(a, b):
    return a + b


def without_carry(a, b):
    result = 0
    multiplier = 1
    while a != 0 or b != 0:
        sums = (a % 10) + (b % 10)
        sums = sums % 10
        result = (sums * multiplier) + result
        a //= 10
        b //= 10
        multiplier *= 10
    return result


T = int(input())
for _ in range(T):
    a = int(input())
    b = int(input())
    sum1 = actual_sum(a, b)
    sum2 = without_carry(a, b)
    error = sum1 - sum2
    print(error)
