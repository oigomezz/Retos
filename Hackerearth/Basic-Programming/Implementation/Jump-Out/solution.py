n = (int(input()))
a = [int(x) for x in input().split()]
for i in range(n):
    if i+a[i] >= n:
        print(i+1)
        break
