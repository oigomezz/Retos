T = int(input())

for ind in range(T):
    n, m = map(int, input().split())
    res = 0
    while n != 0:
        res += ((n+1)//2)**2
        n = n//2
    print(res % m)
