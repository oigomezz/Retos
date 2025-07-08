prime = [1] * 100005
count_prime = [0] * 100005


def auxiliar():
    prime[2] = 1
    count_prime[2] = 1
    for i in range(2, 100005):
        count_prime[i] = count_prime[i - 1] + prime[i]
        if prime[i] == '#':
            continue
        for j in range(2 * i, 100005, i):
            prime[j] = 0


def trap_sol(random1, random2, length, details):
    if details[0] == '*' or details[-1] == '*':
        return "No way!"
    dp = [100005] * (2 * length + 1)
    dp[length] = 0
    for i in range(length - 1, 0, -1):
        if details[i - 1] == '*':
            continue
        dp[i] = 1 + min(dp[i + 1], dp[i + 2])
        k = count_prime[i]
        if k * random2 >= random1 * i:
            dp[i] = min(dp[i], 1 + dp[i + k])
    if dp[1] > length:
        return "No way!"
    return str(dp[1])


T = int(input())
auxiliar()
for _ in range(T):
    r1, r2 = map(int, input().split())
    N = int(input())
    s = input()

    out_ = trap_sol(r1, r2, N, s)
    print(out_)
