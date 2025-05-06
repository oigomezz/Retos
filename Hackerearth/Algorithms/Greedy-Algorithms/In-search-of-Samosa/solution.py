n, k = map(int, input().strip().split())
a = sorted(map(int, input().strip().split()))
samosas = 0
for i in range(n):
    samosas += a[i]
    if samosas > k:
        print(i)
        break
else:
    print(n)
