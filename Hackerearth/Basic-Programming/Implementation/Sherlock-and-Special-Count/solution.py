t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    if (k % 2 or k > (n*n/2)):
        print("NO")
    else:
        print("YES")
