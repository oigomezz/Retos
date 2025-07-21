n = int(input())
ans = 1
b = []
arr = list(map(int, input().split()))
for i in range(n):
    x = arr[i]
    for y in b:
        x = min(x, x ^ y)
    if x:
        b.append(x)

for i in range(n - len(b)):
    ans = (2 * ans) % 1000000007

print(ans)
