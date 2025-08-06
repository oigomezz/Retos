memo = [0] * (1 << 20)

n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n + 1):
    x = arr[i-1]
    memo[x] += x

for i in range(20):
    p = 1 << i
    for mask in range(1 << 20):
        if mask & p:
            memo[mask] += memo[mask ^ p]

q = int(input())
for _ in range(q):
    x = int(input())
    print(memo[x ^ ((1 << 20) - 1)])
