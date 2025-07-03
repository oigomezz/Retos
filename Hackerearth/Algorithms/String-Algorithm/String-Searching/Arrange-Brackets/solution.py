n, k = map(int, input().split())
s = input().strip()

for i in range(1, k):
    print(i, end=" ")
print(n)

for i in range(k, 0, -1):
    print(i, end=" ")
print()

for i in range(1, k + 1):
    print(i, end=" ")
print()
