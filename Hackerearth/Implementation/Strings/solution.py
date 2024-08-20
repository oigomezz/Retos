t = int(input())
for _ in range(t):
    n, m = map(str, input().split())
    if (n == m or (n == "2" and m == "4") or (n == "4" and m == "2")):
        print("YES")
    elif len(n) != 1 or len(m) != 1:
        print("NO")
    else:
        print("NO")
