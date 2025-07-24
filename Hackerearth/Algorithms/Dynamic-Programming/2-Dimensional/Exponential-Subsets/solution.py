MX = 10000
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    dp = 1
    for i in a:
        dp |= dp << i
    for i in a:
        possible = False
        for j in range(2, 100):
            if i ** j > MX:
                break
            possible |= dp >> i ** j & 1
        print(1 if possible else 0, end=' ')
    print()
