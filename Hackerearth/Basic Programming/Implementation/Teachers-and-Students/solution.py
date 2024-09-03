t = int(input())
mod = 7 + pow(10, 9)

for _ in range(t):
    n = int(input())
    k = int(input())
    arr = list(map(int, input().split()))
    print(pow(4, n) % mod)
