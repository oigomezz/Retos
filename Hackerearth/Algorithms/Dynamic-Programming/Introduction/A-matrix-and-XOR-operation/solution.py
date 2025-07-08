t = int(input())
for _ in range(t):
    n, m, k = map(int, input().strip().split())
    for i in range(n + 1):
        a = k - m * (n - i)
        b = 2 * i - n
        if b != 0 and a % b == 0 and 0 <= a / b <= m:
            print('Yes')
            break
    else:
        print('No')
