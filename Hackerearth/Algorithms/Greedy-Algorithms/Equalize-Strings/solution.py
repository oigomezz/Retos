n = int(input())
a = list(input().strip())
b = list(input().strip())
cost = 0
for i in range(1, n):
    if a[i - 1] != b[i - 1]:
        if a[i - 1] == b[i] and a[i] == b[i - 1]:
            a[i - 1], a[i] = a[i], a[i - 1]
        else:
            a[i - 1] = b[i - 1]
        cost += 1
cost += (a[-1] != b[-1])
print(cost)
