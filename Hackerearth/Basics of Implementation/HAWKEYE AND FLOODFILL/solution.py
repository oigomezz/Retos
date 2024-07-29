n = int(input())
x, y, p = map(int, input().split())
for i in range(n):
    for j in range(n):
        print(max(0, p - max(abs(x-i), abs(y-j))), end=' ')
    print()
