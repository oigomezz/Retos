t = int(input())
for _ in range(t):
    n = int(input())
    a = []

    arr = [int(x) for x in input().split()]
    for i in range(n):
        first = int(arr[i])
        a.append((first, 0))  # Initialize second value to 0

    arr = [int(x) for x in input().split()]
    for i in range(n):
        second = int(arr[i])
        a[i] = (a[i][0], second)  # Update second value

    a.sort()
    ans = 0
    prev = 0

    for i in range(n):
        if a[i][0] > prev:
            prev = a[i][1]
            ans += 1
        else:
            prev = min(prev, a[i][1])

    print(str(ans))
