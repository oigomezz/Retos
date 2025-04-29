n = int(input())
a = list(map(int, input().strip().split()))
exist = False
for i in range(n - 1, 0, -1):
    j = 0
    while not exist and j < n - i:
        if a[j] == a[j + i]:
            print(i + 1)
            exist = True
        else:
            j += 1
    if exist:
        break
else:
    print(0)
