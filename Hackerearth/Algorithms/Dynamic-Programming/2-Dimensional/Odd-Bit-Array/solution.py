MOD = 1000000007
t = int(input())
for _ in range(t):
    n = int(input())
    odd = 0
    even = 1
    prefix = 0
    arr = list(map(int, input().split()))

    for i in range(1, n + 1):
        x = int(arr[i-1])
        bits = bin(x).count('1')
        ways = 0
        prefix += bits

        if prefix % 2:
            ways = even
        else:
            ways = odd

        if prefix % 2:
            odd = (odd + ways) % MOD
        else:
            even = (even + ways) % MOD

        if i == n:
            print(ways)
