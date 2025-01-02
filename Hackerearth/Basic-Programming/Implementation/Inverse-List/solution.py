t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    a = [0]*n
    for i in range(n):
        a[arr[i]-1] = i + 1
    if a == arr:
        print("inverse")
    else:
        print("not inverse")
