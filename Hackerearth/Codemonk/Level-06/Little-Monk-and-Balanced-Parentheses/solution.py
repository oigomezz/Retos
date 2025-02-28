n = int(input())
a = [int(x) for x in input().split()]
l = [0 for _ in range(n)]
l[0] = 0

for i in range(1, n):
    if a[i] > 0:
        l[i] = 0
    else:
        if a[i-1]+a[i] == 0:
            if i-2 >= 0:
                l[i] = l[i-2]+2
            else:
                l[i] = 2
        elif a[i-1] > 0:
            l[i] = l[i-1]
        elif a[i-1] < 0 and l[i-1] > 0 and a[i-l[i-1]-1] == -a[i]:
            if i-l[i-1]-2 >= 0:
                l[i] = l[i-l[i-1]-2]+2+l[i-1]
            else:
                l[i] = l[i-1]+2
print(max(l))
