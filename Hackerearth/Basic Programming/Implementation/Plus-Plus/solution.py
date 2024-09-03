n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

sum = 0
mac = -1

for a in range(1, n - 1):
    for b in range(1, m - 1):
        for c in range(a, n - 1):
            for d in range(1, m - 1):
                if (a == c and abs(b - d) < 3) or (b == d and abs(a - c) < 3) or (c == a + 1 and abs(b - d) <= 1):
                    continue
                else:
                    sum = (arr[a - 1][b] * arr[c - 1][d] +
                           arr[a + 1][b] * arr[c + 1][d] +
                           arr[a][b - 1] * arr[c][d - 1] +
                           arr[a][b + 1] * arr[c][d + 1] +
                           arr[a][b] * arr[c][d])
                    if sum > mac:
                        mac = sum

print(mac)
