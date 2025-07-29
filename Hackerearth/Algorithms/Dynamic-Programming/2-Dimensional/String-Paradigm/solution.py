MOD = 1000000009


def modular_exponentiation(base, exponent):
    if base == 0:
        return 0
    if exponent == 0:
        return 1
    if exponent & 1:
        return (base * modular_exponentiation(base, exponent - 1)) % MOD
    half_power = modular_exponentiation(base, exponent >> 1)
    return (half_power * half_power) % MOD


if __name__ == "__main__":
    n = int(input())
    input_string = input()
    transformation_strings = []

    character_map = {}
    for i in range(n):
        character_map[input_string[i]] = i

    for i in range(n):
        transformation_strings.append(input())

    dp = [[0] * 15 for _ in range(500005)]
    for i in range(n):
        dp[0][i] = 1

    m = int(input())
    for i in range(1, m):
        for j in range(n):
            current_sum = 0
            for k in range(len(transformation_strings[j])):
                current_sum = (
                    current_sum + dp[i - 1][character_map[transformation_strings[j][k]]]) % MOD
            dp[i][j] = current_sum

    answer = 0
    for i in range(n):
        answer = (answer + dp[m - 1][i]) % MOD

    print((answer * (((modular_exponentiation(2, m) - 1) + MOD) % MOD)) % MOD)
