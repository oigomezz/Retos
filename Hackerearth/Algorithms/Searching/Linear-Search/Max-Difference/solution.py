t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n == 0 or n == 1:
        print("0")
    elif n == 2:
        print(a[1]-a[0])
    elif n == 3:
        print(a[2]-a[0])
    else:
        print(a[n-1]+a[n-2]-a[0]-a[1])
