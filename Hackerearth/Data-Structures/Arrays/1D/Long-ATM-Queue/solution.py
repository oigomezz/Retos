n = int(input())
h = list(map(int, input().strip().split()))
num = 1
for i in range(n - 1):
    if h[i] > h[i + 1]:
        num += 1
print(num)
