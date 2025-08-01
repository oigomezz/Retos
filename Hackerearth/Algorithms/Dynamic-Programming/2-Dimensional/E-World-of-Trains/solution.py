MOD = 1000000007


def add(a, b):
    return (a + b) % MOD


def mul(a, b):
    return (a * b) % MOD


if __name__ == "__main__":
    n, length, goal, k = map(int, input().split())
    even = [[0] * (goal + 1) for _ in range(n + 1)]
    slop = [[0] * (goal + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for t in range(goal + 1):
            x = mul(k - 1, add(even[i - 1][t], -even[max(0, i - length)][t]))
            if i < length and t == 0:
                x = add(x, k)
            elif t == i - length + 1:
                x = add(x, k)
            if t > 0:
                x = add(x, mul(k - 1, slop[max(0, i - length)][t - 1]))
            if i == n and t == goal:
                print(x)
            even[i][t] = add(x, even[i - 1][t])
            slop[i][t] = add(x, slop[i - 1][t - 1] if t > 0 else 0)
