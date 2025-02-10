from collections import defaultdict

n, k, q = 0, 0, 0
fen = [float('inf')] * 500017
sp = [[0] * 500017 for _ in range(19)]
r = [0] * 500017
ans = [0] * 500017
vec = defaultdict(list)


def update(index, value):
    index += 1
    while index < 500017:
        fen[index] = min(value, fen[index])
        index += index & -index


def get_min(index):
    result = float('inf')
    index += 1
    while index:
        result = min(result, fen[index])
        index ^= index & -index
    return result


def main():
    global n, k, q
    n, k, q = map(int, input().split())
    line = list(map(int, input().split()))
    for i in range(n):
        sp[0][i] = line[i] % k
    for level in range(1, 19):
        for i in range(n - (1 << level) + 1):
            sp[level][i] = (sp[level - 1][i] * sp[level - 1]
                            [i + (1 << (level - 1))]) % k
    for i in range(q):
        l, r[i] = map(int, input().split())
        r[i] -= 1
        vec[l - 1].append(i)
    for i in range(n - 1, -1, -1):
        j = i
        current_product = 1
        for level in range(18, -1, -1):
            if j + (1 << level) < n and (current_product * sp[level][j]) % k:
                current_product = (current_product * sp[level][j]) % k
                j += 1 << level
        if (current_product * sp[0][j]) % k == 0:
            update(j, j - i + 1)
        for query_index in vec[i]:
            ans[query_index] = get_min(r[query_index])
    for i in range(q):
        print(-1 if ans[i] >= 500017 else ans[i], end=' ')
    print()


if __name__ == "__main__":
    main()
