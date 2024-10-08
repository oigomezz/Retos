def n_choose_2(n):
    return n * (n - 1) // 2


def n_choose_3(n):
    return n_choose_2(n) * (n - 2) // 3


n, m = map(int, input().split())
ans = 0
a = [0] * m
arr = list(map(int, input().split()))

for i in range(n):
    tmp = arr[i]
    a[tmp % m] += 1

for i in range(0, (2 * m) // 3 + 1):
    for j in range(i, (2 * m - i) // 2 + 1):
        trio = [i, j, (2 * m - j - i) % m]
        if trio[2] < j:
            continue
        if trio[0] == trio[1] == trio[2]:
            ans += n_choose_3(a[j])
        elif trio[0] == trio[1]:
            ans += n_choose_2(a[j]) * a[trio[2]]
        elif trio[1] == trio[2]:
            ans += n_choose_2(a[j]) * a[trio[0]]
        else:
            ans += a[trio[0]] * a[trio[1]] * a[trio[2]]

print(ans)
