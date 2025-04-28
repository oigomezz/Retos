n, m = map(int, input().strip().split())
best = -1
index = 0
for row in range(n):
    number = int(input().strip(), 2)
    if number > best:
        index = row + 1
        best = number

print(index)
