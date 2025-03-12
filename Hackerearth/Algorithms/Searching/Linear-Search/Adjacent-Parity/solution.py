t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    even = 0
    odd = 0
    for value in arr:
        if value % 2 == 0:
            even += 1
        else:
            odd += 1
    if even == n:
        print("YES")
    elif odd == n:
        print("YES")
    elif odd-even == 1 or odd-even == -1 or odd == even:
        print("YES")
    else:
        print("NO")
