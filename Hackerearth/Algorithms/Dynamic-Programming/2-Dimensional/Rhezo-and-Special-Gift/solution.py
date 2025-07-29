MOD = 1000000007


def multiply(res, a, b, length):
    for row in range(length):
        for col in range(length):
            result_value = 0
            for idx in range(length):
                result_value += (a[row * length + idx] *
                                 b[idx * length + col]) % MOD
            res[row * length + col] = result_value % MOD


if __name__ == "__main__":
    n, m = map(int, input().split())
    size = 100
    initial = [0] * (size * size)
    transition = [0] * (size * size)
    result = [0] * (size * size)

    for i in range(1, size):
        initial[(i - 1) * size + i] = 1

    line = list(map(int, input().split()))
    for i in range(m):
        k = line[i]
        initial[size * size - k] += 1

    for i in range(size):
        transition[i * size + i] = 1

    while n:
        if n % 2:
            multiply(result, transition, initial, size)
            transition, result = result, transition
        multiply(result, initial, initial, size)
        initial, result = result, initial
        n //= 2

    print(transition[size * size - 1])
