def solve(length, limit, array):
    cur = [0] * limit
    ans = float('inf')
    found = 0
    for j in range(length):
        array[j] -= 1
        if cur[array[j]] == 0:
            found += 1
        cur[array[j]] += 1

        if found != limit:
            continue

        i = 0
        while cur[array[i]] > 1:
            cur[array[i]] -= 1
            i += 1

        ans = min(ans, j - i + 1)
    return ans


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))
        out_ = solve(N, K, A)
        print(out_)
