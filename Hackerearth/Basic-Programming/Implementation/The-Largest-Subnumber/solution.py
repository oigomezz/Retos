def largest_sol(n, k, s):
    s = list(map(int, s))
    a = [s[0]] * n
    b = [1] * n
    for i in range(1, n):
        a[i] = a[i - 1] ^ s[i]
        j = n - i - 1
        b[j] = b[j + 1] * 10 % k
    x = -1
    y = z = 0
    for i in range(n - 1, 0, -1):
        z = (z + s[i] * b[i]) % k
        if s[i] and not z and x <= a[i - 1]:
            y = i
            x = a[i - 1]
    return x if x == -1 else ''.join(map(str, s[y:]))


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    out_ = largest_sol(n, k, s)
    print(out_)
