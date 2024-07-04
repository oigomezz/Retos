def solve(x, k):
    while x > 0:
        ans = x % k
        if ans > 1:
            return False
        else:
            x //= k
    return True


t = int(input())
for i in range(t):
    x, k = map(int, input().split())
    if solve(x, k):
        print("YES")
    else:
        print("NO")
