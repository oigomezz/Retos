MOD = 1000000007


def solve(length):
    count = [0] * 10
    curr = [0] * 10
    res = 0
    for i in map(int, length):
        if i > 0:
            res += curr[i]
            res %= MOD
            curr[i] += (count[i - 1] * (count[i - 1] - 1)) // 2
            curr[i] %= MOD
        count[i] += 1
    return res


T = int(input())
for _ in range(T):
    N = input()

    out_ = solve(N)
    print(out_)
