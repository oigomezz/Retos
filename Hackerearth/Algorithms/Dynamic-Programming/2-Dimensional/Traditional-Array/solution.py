def fix_mod(value):
    if value < 0:
        value += 1000000007
    elif value >= 1000000007:
        value -= 1000000007
    return value


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        n, m = map(int, input().split())
        dp = [1] * (m + 1)
        for i in range(1, n):
            aux = [0] * (m + 1)
            for j in range(1, m + 1):
                aux[j] = fix_mod(aux[j] + dp[j])
                for k in range(j * 2, m + 1, j):
                    aux[k] = fix_mod(aux[k] + dp[j])
                    aux[j] = fix_mod(aux[j] + dp[k])
            dp = aux

        answer = 0
        for i in range(1, m + 1):
            answer = fix_mod(answer + dp[i])
        print(answer)
