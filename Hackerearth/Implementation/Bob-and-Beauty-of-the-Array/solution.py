def binary_power(base, exponent):
    result = 1
    while exponent:
        if exponent % 2:
            result = (result * base) % 1000000007
        base = (base * base) % 1000000007
        exponent //= 2
    return result


def main():
    n = int(input())
    result = 0
    frequency = [0] * 1001
    accumulated = [0] * 1001
    array = list(map(int, input().split()))

    for i in range(n):
        frequency[array[i]] += 1

    values = []
    for i in range(1, 1001):
        if frequency[i] > 0:
            values.append(i)
        accumulated[i] = accumulated[i - 1] + frequency[i]

    for i in range(len(values)):
        x = values[i]
        result = (result + (x * (binary_power(2,
                  frequency[x]) - frequency[x] - 1 + 1000000007) % 1000000007) % 1000000007) % 1000000007
        for j in range(i + 1, len(values)):
            y = values[j]
            xy = accumulated[y - 1] - accumulated[x]
            amount_ij = binary_power(2, xy)
            amount_i = (binary_power(
                2, frequency[x]) - 1 + 1000000007) % 1000000007
            amount_j = (binary_power(
                2, frequency[y]) - 1 + 1000000007) % 1000000007
            flag = (amount_i * amount_j) % 1000000007
            flag = (flag * amount_ij) % 1000000007
            flag = (flag * (x | y)) % 1000000007
            result = (result + flag) % 1000000007

    print(result)


if __name__ == "__main__":
    main()
